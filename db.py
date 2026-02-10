import sqlite3

def inicializar_db():
    conn = sqlite3.connect('red_admin.db')
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
        cursor.execute("INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)", 
                       ('admin', "admin123"))
    
    conn.commit()
    conn.close()


if __name__ == "__main__":
    inicializar_db()