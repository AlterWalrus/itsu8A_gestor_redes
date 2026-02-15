import sqlite3
import hashlib

DB_NOMBRE = 'red_admin.db'

def inicializar_db():
    conn = sqlite3.connect(DB_NOMBRE)
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            correo TEXT UNIQUE,
            password_hash TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dispositivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            ip TEXT UNIQUE,
            mac TEXT UNIQUE,
            fabricante TEXT,
            tipo TEXT DEFAULT 'DESCONOCIDO',
            ubicacion TEXT DEFAULT 'NO ASIGNADA',
            estado TEXT DEFAULT 'OFFLINE'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fallas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dispositivo_id INTEGER,
            descripcion TEXT,
            severidad TEXT,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
            estado TEXT DEFAULT 'ABIERTA',
            FOREIGN KEY (dispositivo_id) REFERENCES dispositivos (id) ON DELETE CASCADE
        )
    ''')

    #Si no hay admin crea uno por defecto
    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)", ('admin', generar_hash("admin123")))
    
    conn.commit()
    conn.close()


def actualizar_tabla_dispositivos(lista_dispositivos):
    conn = sqlite3.connect('red_admin.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE dispositivos SET estado = 'OFFLINE'")
    
    agregados = 0
    actualizados = 0
    
    for d in lista_dispositivos:
        identificador = d['mac'] if d['mac'] != '00:00:00:00:00:00' else d['ip']
        
        try:
            cursor.execute('''
                INSERT INTO dispositivos (nombre, ip, mac, fabricante, estado)
                VALUES (?, ?, ?, ?, 'ONLINE')
            ''', (d['nombre'], d['ip'], d['mac'], d['fabricante']))
            agregados += 1
        except sqlite3.IntegrityError:
            cursor.execute('''
                UPDATE dispositivos 
                SET ip = ?, estado = 'ONLINE' 
                WHERE mac = ? OR ip = ?
            ''', (d['ip'], d['mac'], d['ip']))
            actualizados += 1
            
    conn.commit()
    conn.close()
    return agregados, actualizados


def cargar_tabla_dispositivos():
    conn = sqlite3.connect('red_admin.db')
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM dispositivos")
        rows = cursor.fetchall()
        
        dispositivos = [dict(row) for row in rows]
        return dispositivos
    except sqlite3.Error as e:
        print(f"Error al obtener dispositivos: {e}")
        return []
    finally:
        conn.close()


def generar_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verificar_usuario(user, password):
    conn = sqlite3.connect(DB_NOMBRE)
    cursor = conn.cursor()
    hash_intento = generar_hash(password)
    
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND password_hash = ?", (user, hash_intento))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


if __name__ == "__main__":
    inicializar_db()