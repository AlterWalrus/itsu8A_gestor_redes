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
            password_hash TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dispositivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            ip TEXT,
            mac TEXT,
            tipo TEXT,
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

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS archivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            tipo TEXT,
            ruta TEXT
        )
    ''')

    #Si no hay admin crea uno por defecto
    cursor.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)", ('admin', generar_hash("admin123")))
    
    conn.commit()
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