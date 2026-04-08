import sqlite3

class ColegioModel:
    def __init__(self, db_name="colegio.db"):
        self.conn = sqlite3.connect(db_name)
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                edad INTEGER,
                curso TEXT
            )
        """)
        self.conn.commit()

    def agregar_estudiante(self, nombre, edad, curso):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estudiantes (nombre, edad, curso) VALUES (?, ?, ?)",
            (nombre, edad, curso)
        )
        self.conn.commit()

    def obtener_estudiantes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        return cursor.fetchall()

    def eliminar_estudiante(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id = ?", (id,))
        self.conn.commit()

    def actualizar_estudiante(self, id, nombre, edad, curso):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE estudiantes
            SET nombre = ?, edad = ?, curso = ?
            WHERE id = ?
        """, (nombre, edad, curso, id))
        self.conn.commit()