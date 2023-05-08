import requests
from tkinter import *

# Okno
window = Tk()
window.minsize(300, 300)
window.resizable(False, False)
window.title("Aplikace na urážky")
window.config(bg="#2F47AD")


# Funkce
def insult_me():
    user_language = drop_down_lang.get()
    my_parameters = {
        "lang": user_language,
        "type": "json"
    }

    response = requests.get(f"https://evilinsult.com/generate_insult.php", params=my_parameters)
    response.raise_for_status()
    data = response.json()
    insult_label.config(text=data["insult"])


# Roletka - jazyk urážek
drop_down_lang = StringVar(window)
drop_down_lang.set("en")
drop_down_lang_options = OptionMenu(window, drop_down_lang, "en", "cs", "es", "fr")
drop_down_lang_options.config(bg="white", fg="#AD4728", font=("Arial", 12, "bold"))
drop_down_lang_options.pack(pady=(15, 0))

# Tlačítko
insult_button = Button(text="Chci urazit", command=insult_me, bg="#31AFE0", font=("Arial", 12, "bold"))
insult_button.pack(pady=15)

# Label
insult_label = Label(wraplength=250, bg="#2F47AD", fg="#E47632", font=("Arial", 16, "bold"))
insult_label.pack()

# Hlavní cyklus
window.mainloop()
