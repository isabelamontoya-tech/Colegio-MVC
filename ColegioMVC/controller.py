from tkinter import messagebox
from model import ColegioModel

class ColegioController:
    def __init__(self):
        self.model = ColegioModel()

    def agregar_estudiante(self, nombre, edad, curso):
        if not nombre or not edad or not curso:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número")
            return

        edad = int(edad)
        self.model.agregar_estudiante(nombre, edad, curso)

    def obtener_estudiantes(self):
        return self.model.obtener_estudiantes()

    def eliminar_estudiante(self, id):
        self.model.eliminar_estudiante(id)

    def actualizar_estudiante(self, id, nombre, edad, curso):
        if not nombre or not edad or not curso:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número")
            return

        edad = int(edad)
        self.model.actualizar_estudiante(id, nombre, edad, curso)