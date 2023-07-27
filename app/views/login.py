# app/views/login.py

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
# from app.views.custom import custom_entry_style


class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Iniciar Sesion")

        style = Style(theme="cosmo")

        self.label_username = ttk.Label(self.root, text="Usuario", style="primary.TLabel")
        self.label_username.pack()

        self.entry_username = ttk.Entry(self.root, style="primary.TEntry")
        self.entry_username.pack()

        self.label_password = ttk.Label(self.root, text="Contraseña", style="primary.TLabel")
        self.label_password.pack()

        self.entry_password = ttk.Entry(self.root, show="*", style="primary.TEntry")
        self.entry_password.pack()

        self.button_login = ttk.Button(self.root, text="Acceder", style="primary.TButton")
        self.button_login.pack()

    def login(self):
        # logica para el inicio de sesion
        pass
