# Inventario/main.py
import tkinter as tk
import tkinter.font as tkfont
from app.views.login import login


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def main():

    # Configuracion
    root = tk.Tk()
    root.title("Sistema Inventario")
    # root.geometry("300x450")
    root.resizable(False, False)

    # Tipo de letra
    custom_font = tkfont.Font(family="monospace", size=11, weight="normal")
    root.option_add("*Font", custom_font)

    # Views
    login(root)

    # Centrar ventana
    window_width = 300
    window_height = 450
    center_window(root, window_width, window_height)

    # Run
    root.mainloop()


# Run
if __name__ == '__main__':
    main()
