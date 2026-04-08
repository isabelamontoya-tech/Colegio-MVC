import tkinter as tk
from tkinter import messagebox
from controller import ColegioController

class ColegioView:
    def __init__(self, root):
        self.controller = ColegioController()
        self.root = root
        self.root.title("Sistema Colegio")

        # CAMPOS
        tk.Label(root, text="Nombre").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(root, text="Edad").grid(row=1, column=0)
        self.entry_edad = tk.Entry(root)
        self.entry_edad.grid(row=1, column=1)

        tk.Label(root, text="Curso").grid(row=2, column=0)
        self.entry_curso = tk.Entry(root)
        self.entry_curso.grid(row=2, column=1)

        # BOTONES
        tk.Button(root, text="Agregar", command=self.agregar_estudiante).grid(row=3, column=0)
        tk.Button(root, text="Mostrar", command=self.mostrar_estudiantes).grid(row=3, column=1)

        # LISTA
        self.lista = tk.Listbox(root, width=60)
        self.lista.grid(row=4, column=0, columnspan=2)
        self.lista.bind("<<ListboxSelect>>", self.seleccionar_estudiante)

        # BOTONES ABAJO
        tk.Button(root, text="Actualizar", command=self.actualizar_estudiante).grid(row=5, column=0)
        tk.Button(root, text="Eliminar", command=self.eliminar_estudiante).grid(row=5, column=1)
        tk.Button(root, text="Limpiar", command=self.limpiar_campos).grid(row=6, column=0, columnspan=2)

    # FUNCIONES

    def agregar_estudiante(self):
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()
        curso = self.entry_curso.get()

        self.controller.agregar_estudiante(nombre, edad, curso)
        self.mostrar_estudiantes()
        self.limpiar_campos()

    def mostrar_estudiantes(self):
        self.lista.delete(0, tk.END)

        for estudiante in self.controller.obtener_estudiantes():
            texto = f"{estudiante[0]} - {estudiante[1]} - {estudiante[2]} - {estudiante[3]}"
            self.lista.insert(tk.END, texto)

    def seleccionar_estudiante(self, event):
        try:
            seleccion = self.lista.curselection()
            if not seleccion:
                return

            dato = self.lista.get(seleccion[0])
            partes = dato.split(" - ")

            if len(partes) < 4:
                return

            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, partes[1])

            self.entry_edad.delete(0, tk.END)
            self.entry_edad.insert(0, partes[2])

            self.entry_curso.delete(0, tk.END)
            self.entry_curso.insert(0, partes[3])

        except:
            pass

    def actualizar_estudiante(self):
        try:
            seleccion = self.lista.curselection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione un estudiante")
                return

            dato = self.lista.get(seleccion[0])
            partes = dato.split(" - ")

            if len(partes) < 4:
                return

            id_estudiante = int(partes[0])

            nombre = self.entry_nombre.get()
            edad = self.entry_edad.get()
            curso = self.entry_curso.get()

            self.controller.actualizar_estudiante(id_estudiante, nombre, edad, curso)

            self.mostrar_estudiantes()
            self.limpiar_campos()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_estudiante(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un estudiante")
            return

        dato = self.lista.get(seleccion[0])
        id_estudiante = int(dato.split(" - ")[0])

        self.controller.eliminar_estudiante(id_estudiante)

        self.mostrar_estudiantes()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_curso.delete(0, tk.END)

        self.lista.selection_clear(0, tk.END)