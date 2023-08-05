# Inventario/app/views/menu.py
import tkinter as tk


def principal_menu(principal_window, user, root):
    def cerrar_sesion():
        principal_window.destroy()
        root.deiconify()

    user = tk.Label(principal_window, text=f"{user}")
    user.pack()

    user_boton = tk.Button(principal_window, text="Cerrar Ventana", command=cerrar_sesion)
    user_boton.pack()


def main(user, root):

    # Configuracion
    principal_window = tk.Tk()
    principal_window.title("Menu Principal")
    principal_window.geometry("800x600")

    principal_menu(principal_window, user, root)

    # Ventana Loop
    principal_window.mainloop()
