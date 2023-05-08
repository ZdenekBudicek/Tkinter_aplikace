import requests
from tkinter import *

window = Tk()
window.minsize(700, 400)
window.resizable(False, False)
window.title("ISS")


# Funkce
def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = (data["iss_position"]["longitude"])
    latitude = (data["iss_position"]["latitude"])
    longitude_labe.config(text=f"Zeměpisná délka ISS je: {longitude}")
    latitude_label.config(text=f"Zeměpisná šířka ISS je: {latitude}")


# Vytvoření canvasu
canvas = Canvas(window, width=500, height=280)
canvas.pack()
iss_img = PhotoImage(file="img/giphy.gif")
canvas.create_image(0, 0, anchor="nw", image=iss_img)

# Framy
coordinates_frame = Frame(window)
coordinates_frame.pack()

# Tlačítko
recount_button = Button(coordinates_frame, text="Současná souřadnice ISS", command=iss_coordinates)
recount_button.pack()

# Labels
latitude_label = Label()
latitude_label.pack()

longitude_labe = Label()
longitude_labe.pack()

# Hlavní cyklus
window.mainloop()
