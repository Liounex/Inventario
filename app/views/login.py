# app/views/login.py
from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkImage
from PIL import Image
# import tkinter as tk
from CTkMessagebox import CTkMessagebox


def iniciar_sesion():
    # logica para el inicio de sesion
    CTkMessagebox(title="Info", message="Boton Para Acceder")


def registrarse():
    CTkMessagebox(title="Info", message="Abre una Nueva Ventana para Registrarse")


class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Iniciar Sesion")

        logo = CTkImage(dark_image=Image.open("./app/views/image/inventario.png"),
                        size=(200, 190))

        self.logomostrar = CTkLabel(root, image=logo, text="")
        self.logomostrar.pack(pady=10)

        self.label_username = CTkLabel(root, text="Usuario", font=("Arial", 16))
        self.label_username.pack()

        self.entry_username = CTkEntry(root, width=200)
        self.entry_username.pack(pady=10)

        self.label_password = CTkLabel(root, text="Contraseña", font=("Arial", 16))
        self.label_password.pack()

        self.entry_password = CTkEntry(root, show="*", width=200)
        self.entry_password.pack(pady=10)

        self.button_login = CTkButton(root, text="Acceder", command=iniciar_sesion)
        self.button_login.pack(pady=8)

        self.button_registrarse = CTkButton(root, text="Nuevo Usuario", command=registrarse)
        self.button_registrarse.pack(side="left", padx=25)

        self.button_login = CTkButton(root, text="Facebook")
        self.button_login.pack(side="right", padx=25)
