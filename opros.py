from tkinter import *

def entry_and_change():
    lab2["text"] = a+ent1.get()
    lab1['text'] = "сосал?"

a="Ваш ответ: "

window = Tk()
lab1 = Label(window, text="ответь мне на вопрос:\n бьется ли у тебя сердце\nв данный момент?", width = 50, height = 12, bg = "aquamarine4", font="arial 24")
but1 = Button(window, text="отправить", width=35, height = 3, bg = "grey70")
ent1 = Entry(window, width = 100)
lab2 = Label(window, text=a, width= 50, height = 12, bg = "aquamarine4", font="arial 14")
but1.config(command=entry_and_change)

lab1.pack()
ent1.pack()
but1.pack()
lab2.pack()

window.mainloop()
