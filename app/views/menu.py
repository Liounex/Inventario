# Inventario/app/views/menu.py
import tkinter as tk
import tkinter.ttk as ttk


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def principal_menu(principal_window, user, root):
    def cerrar_sesion():
        principal_window.destroy()
        root.deiconify()

    global frame_elegido

    def frame_ventana(menu_resultado):

        global frame_elegido

        if frame_elegido:
            frame_elegido.destroy()

        frame_elegido = ttk.Frame(principal_window)
        frame_elegido.pack(fill=tk.BOTH, expand=True)

        if menu_resultado == "Usuarios":
            label = ttk.Label(frame_elegido, text="Contenido de la Opción 1", font=("Helvetica", 20))
            label.pack(pady=20)
        elif menu_resultado == "Productos":
            label = ttk.Label(frame_elegido, text="Contenido de la Opción 2", font=("Helvetica", 20))
            label.pack(pady=20)
        elif menu_resultado == "Categorias":
            label = ttk.Label(frame_elegido, text="Contenido de la Opción 3", font=("Helvetica", 20))
            label.pack(pady=20)
        elif menu_resultado == "Cerrar Sesion":
            cerrar_sesion()

        # mas opciones

    frame_menu = tk.Frame(principal_window, bg='gray')
    frame_menu.pack(fill=tk.Y, side=tk.LEFT)

    opciones_menu = [
        "Usuarios",
        "Productos",
        "Categorias",
        "",
        "",
        "",
        "",
        "",
        "Cerrar Sesion",
    ]

    for menu in opciones_menu:
        (tk.Button(frame_menu, text=menu,
                   width=20,
                   height=2,
                   command=lambda op=menu: frame_ventana(op),
                   )
         .pack(fill=tk.X, padx=10, pady=8))

    frame_elegido = None


def main(user, root):

    # Configuracion
    principal_window = tk.Tk()
    principal_window.title("Menu Principal")
    # principal_window.geometry("1080x720")

    principal_menu(principal_window, user, root)

    window_width = 1441
    window_height = 720
    center_window(principal_window, window_width, window_height)

    # Ventana Loop
    principal_window.mainloop()
