from tkinter import *
import customtkinter

# Okno
window = customtkinter.CTk()
window.title("Seznam úkolů")
window.geometry("400x420")
window.iconbitmap("icon2.ico")
window.resizable(False, False)

# Definujeme fonty a barvy
main_font = ("Times New Roman", 12)
main_color = "#72be34"
button_color = "#ff9122"


# Funkce
def ad_text():
    # přidání textového úkolu
    # Důležité u insertu napsat odkud to chci vkládat př. 0 nebo END
    list_box.insert(END, user_input.get())
    # Vyčistí to zadávací pole kam píšeme
    user_input.delete(0, END)


def remove_item():
    # Odstraní jednu položku ze seznamu
    list_box.delete(ANCHOR)


def clear_list():
    # Odstraní celý seznam
    list_box.delete(0, END)


def save_tasks():
    # uloží úkoly do textového souboru
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            # Pokud končí one_task \n tak ho tam nedá
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")


def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba při otevírání souboru")


# Framy
input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
input_frame.pack(pady=5)
text_frame.pack(pady=5)
button_frame.pack(pady=5)

# Input frame - obsah
user_input = customtkinter.CTkEntry(input_frame, width=290, height=30, border_width=3, corner_radius=10)
add_button = customtkinter.CTkButton(input_frame, text="Přidat", width=2, command=ad_text)
user_input.grid(row=0, column=0, pady=5)
# pad je vnější okraj a ipad je vnitřní okraj
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=15)

# Scrollbar
text_scrollbar = customtkinter.CTkScrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N + S)

# Text frame - obsah
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

# Button frame - obsah
remove_button = customtkinter.CTkButton(button_frame, text="Odstranit položku", width=2,
                                        command=remove_item)
clear_button = customtkinter.CTkButton(button_frame, text="Smazat seznam", width=2,
                                       command=clear_list)
save_button = customtkinter.CTkButton(button_frame, text="Uložit seznam", width=2,
                                      command=save_tasks)
quit_button = customtkinter.CTkButton(button_frame, text="Zavřít", width=2,
                                      command=window.destroy)
remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10)
quit_button.grid(row=0, column=3, padx=2, pady=10)

# Načteme seznam uložných dat
open_tasks()

window.mainloop()
