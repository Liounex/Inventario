import tkinter as ttk
from app.views.login import Login


def center_windows(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def main():
    root = ttk.Tk()
    root.title("Inventario")
    # root.geometry("400x650")

    window_width = 400
    window_height = 600

    center_windows(root, window_width, window_height)

    Login(root)

    root.mainloop()


if __name__ == "__main__":
    main()
