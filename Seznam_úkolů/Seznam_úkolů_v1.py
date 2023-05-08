from tkinter import *

# Okno
window = Tk()
window.title("Seznam úkolů")
window.minsize(400, 400)
window.iconbitmap("icon2.ico")
window.resizable(False, False)

# Definujeme fonty a barvy
main_font = ("Times New Roman", 12)
main_color = "#72be34"
button_color = "#ff9122"
window.config(bg=main_color)


# Funkce
def ad_text():
    # přidání textového úkolu
    # Důležité u insertu napsat odkud to chci vkládat př. 0 nebo END
    list_box.insert(END, user_input.get())
    # Vyčistí zadávací pole kam píšeme
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
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Input frame - obsah
user_input = Entry(input_frame, width=30, borderwidth=3, font=main_font)
add_button = Button(input_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_color, command=ad_text)
user_input.grid(row=0, column=0, pady=5)
# pad je vnější okraj a ipad je vnitřní okraj
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=15)

# Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N + S)

# Text frame - obsah
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

# Propojíme scrollbar s list_boxem
text_scrollbar.config(command=list_box.yview)

# Button frame - obsah
remove_button = Button(button_frame, text="Odstranit položku", borderwidth=2, font=main_font, bg=button_color,
                       command=remove_item)
clear_button = Button(button_frame, text="Smazat seznam", borderwidth=2, font=main_font, bg=button_color,
                      command=clear_list)
save_button = Button(button_frame, text="Uložit seznam", borderwidth=2, font=main_font, bg=button_color,
                     command=save_tasks)
quit_button = Button(button_frame, text="Zavřít", borderwidth=2, font=main_font, bg=button_color,
                     command=window.destroy)
remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button.grid(row=0, column=1, padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10)
quit_button.grid(row=0, column=3, padx=2, pady=10)

# Načteme seznam uložných dat
open_tasks()

window.mainloop()
