# Inventario/main.py
import tkinter as tk
import tkinter.font as tkfont
from app.views.login import login


def main():

    # Configuracion
    root = tk.Tk()
    root.title("Sistema Inventario")
    root.geometry("300x450")
    root.resizable(False, False)

    # Tipo de letra
    custom_font = tkfont.Font(family="monospace", size=11, weight="normal")
    root.option_add("*Font", custom_font)

    # Views
    login(root)

    # Run
    root.mainloop()


# Run
if __name__ == '__main__':
    main()
