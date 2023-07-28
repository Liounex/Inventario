
from app.views.login import Login
from customtkinter import CTk


def center_windows(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def main():
    root = CTk()
    root.title("Inventario")
    root.resizable(False, False)

    window_width = 400
    window_height = 520

    center_windows(root, window_width, window_height)

    Login(root)

    root.mainloop()


if __name__ == "__main__":
    main()
