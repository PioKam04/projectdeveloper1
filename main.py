from tkinter import *
import requests
from bs4 import BeautifulSoup
import tkintermapview
import logging
from tkinter import messagebox

logging.basicConfig(filename='logowanie.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

uzytkownicy = {
    'geomatykajestsuper' : 'geomatykalove',

}

def zaloguj():
    username = entry_username.get()
    password = entry_password.get()

    if username in uzytkownicy and uzytkownicy[username] == password:
        messagebox.showinfo("status logowania", "zalogowano pomyślnie" )
        okno_logowania.destroy()
    else:
        messagebox.showerror("status logowania", "Błąd logowania" )
        entry_username.delete(0, END)
        entry_password.delete(0, END)

okno_logowania = Tk()
okno_logowania.title('Okno logowania')
okno_logowania.geometry('500x500')

Label(okno_logowania,text="login").pack()
entry_username = Entry(okno_logowania,width=20)
entry_username.pack()

Label(okno_logowania,text="Hasło").pack()
entry_password = Entry(okno_logowania, show="*")
entry_password.pack()

Button(okno_logowania,text="zaloguj", command=zaloguj).pack()

okno_logowania.mainloop()