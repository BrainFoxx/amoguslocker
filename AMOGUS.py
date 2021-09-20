from playsound import *
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pyautogui

amogus = Tk()
amogus.title("AMOGUS")
amogus.geometry("400x250")
amogus["bg"] = "black"
stan_width = 1920
stan_height = 1080


def clicked():
    amog = format(txt.get())
    if amog == "SUGOMA":  # Пароль
        amogus.destroy()
    else:
        pyautogui.alert(
            text="ПАРОЛЬ НЕ ВЕРНЫЙ", title="AMOGUS"
        )  # Уведомление если пользователь ввёл неправильный пароль, и запуск музыки


def play(test):
    playsound("sound.mp3", False)


def block():
    amogus.protocol("WM_DELETE_WINDOW", block)
    amogus.update()


def fullscreen():
    amogus.attributes("-fullscreen", True, "-topmost", True)


fullscreen()

img = Image.open("../Github/amogus-lock/amogus.png")  # Путь к вашей картинке
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo).place(x=425, y=0)

amog = Label(
    amogus, text="AMOGUS", font=("Arial Bold", 48), fg="white", bg="black"
)  # Надпись AMOGUS
amog.grid(column=0, row=0)
amog.place(x=850, y=150)

txt = ttk.Entry(amogus)
btn = ttk.Button(amogus, text="AMOGUS?", command=clicked)  # Кнопка подтверждения пароля
txt.place(x=743, y=686, width=100, height=60)
btn.place(x=850, y=684, width=110, height=62)


block()
play("sound.mp3")
amogus.mainloop()
