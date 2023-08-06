# Inventario/app/views/login.py
import tkinter as tk
import tkinter.messagebox as msg
from app.views.menu import main


def login(root):

    def on_acceder():

        # Data temporal
        usuario = 'admin'
        passwd = '1234'

        # datos de usuario
        user = entry_user.get()
        user_pas = entry_passw.get()

        # Validations
        if user == '' or user_pas == '':
            msg.showerror("Error", "Campos Vacios Favor de Completar")
        elif user != usuario or user_pas != passwd:
            msg.showerror("Error", "usuario o cotraseña Incorrecto")
        else:
            root.withdraw()
            main(user, root)

    head = tk.Label(root, text="Inventariado", font=30)
    head.grid(row=0, column=0, columnspan=2, padx=65, pady=7)

    username = tk.Label(root, text="Usuario")
    username.grid(row=1, column=0, columnspan=2, padx=65, pady=7)

    entry_user = tk.Entry(root,
                          width=20,
                          )
    entry_user.grid(row=2, column=0, columnspan=2, padx=65, pady=7)
    entry_user.focus_set()

    password = tk.Label(root, text="Contraseña")
    password.grid(row=3, column=0, columnspan=2, padx=65, pady=7)

    entry_passw = tk.Entry(root, show="*",
                           width=20,
                           )
    entry_passw.grid(row=4, column=0, columnspan=2, padx=65, pady=10)

    button_login = tk.Button(root, text="Acceder",
                             width=15,
                             bg="blue",
                             fg="white",
                             command=on_acceder
                             )
    button_login.grid(row=5, column=0, columnspan=2, padx=65, pady=9)


