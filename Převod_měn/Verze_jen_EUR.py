from tkinter import *
from bs4 import BeautifulSoup
import requests

# Okno
window = Tk()
window.title("Převod měn z CZK na Eura")
window.minsize(400, 320)
window.resizable(False, False)
window.config(bg="#896fc1")
window.iconbitmap("../icons/icon3.ico")

# Web_Scraping
response = requests.get("https://www.kurzy.cz/kurzy-men/nejlepsi-kurzy/EUR-euro/")
soup = BeautifulSoup(response.text, "html.parser")
exchange_rate = soup.find_all(class_="clrred")
euro = float(exchange_rate[0].text)


# Funkce
def count_currency():
    try:
        if float(amount_imput.get()) > 0:
            amount_eur = float(amount_imput.get()) / euro
            result_label["text"] = round(amount_eur, 2)
            imput_label["text"] = amount_imput.get()
            amount_imput.delete(0, END)
        else:
            error_label["text"] = "Vložte kladné číslo"
            imput_label["text"] = ""
            amount_imput.delete(0, END)
    except ValueError:
        error_label["text"] = "Vložte prosím číslo"
        imput_label["text"] = ""
        amount_imput.delete(0, END)


# Vstup od uživatele
amount_imput = Entry(width=10, font=("Halvetica", 15))
amount_imput.grid(row=0, column=0, padx=30, pady=20)

# Label
czk_label = Label(text="CZK", font=("Helvetica", 15), bg="#896fc1", fg="white")
czk_label.grid(row=0, column=1)

imput_label = Label(text="0", font=("Helvetica", 15, "bold"), bg="#896fc1", fg="white")
imput_label.grid(row=1, column=0, pady=(65, 0), padx=(30, 0))

imput_label_czk = Label(text="CZK", font=("Helvetica", 15), bg="#896fc1", fg="white")
imput_label_czk.grid(row=1, column=1, pady=(75, 15))

result_label = Label(text="0", font=("Helvetica", 15, "bold"), bg="#896fc1", fg="white")
result_label.grid(row=2, column=0, padx=(30, 0))

eur_label = Label(text="EUR", font=("Helvetica", 15), bg="#896fc1", fg="white")
eur_label.grid(row=2, column=1)

error_label = Label(text="", font=("Helvetica", 15), bg="#896fc1", fg="white")
error_label.grid(row=4, column=0, pady=(20, 0))

# Tlačítko
count_button = Button(text="Převést", font=("Helvestica", 15), command=count_currency)
count_button.grid(row=0, column=2, padx=50, pady=20)

# Hlavní cyklus
window.mainloop()
