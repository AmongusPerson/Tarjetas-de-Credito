from tkinter import *
from PIL import ImageTk, Image
pg = Tk()
pg.geometry("500x500")
pg.title("Imagen")
pg.configure(background="lightgreen")

def fn1():
    try:
        var = int(ip1.get())
        messagebox.showinfo("Aceptado","El codigo fue aceptado")
    except(ValueError):
        messagebox.showinfo("Error","El codigo no es compatible")

img = ImageTk.PhotoImage(Image.open("tarjeta2.png"))

lb1 = Label(pg, text="Comprobar Tarjetas de Credito", font=124142526)
lb1.place(relx=0.5, rely=0.1, anchor=CENTER)

ip1 = Entry(pg, font=200)
ip1.place(relx=0.5, rely=0.2, anchor=CENTER)

bt1 = Button(pg, text="Comprobar", command=fn1)
bt1.place(relx=0.5, rely=0.3, anchor=CENTER)

lb1 = Label(pg, image=img)
lb1.place(relx=0.5, rely=0.6, anchor=CENTER)

pg.mainloop()