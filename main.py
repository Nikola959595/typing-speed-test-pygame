from tkinter import *
from words import words


root = Tk()
root.title("Typing speed test")
root.geometry("800x500")

bg = PhotoImage(file = "background.png")

canvas = Canvas(width=800,height=500)
canvas.pack(fill = 'both', expand=True)
canvas.create_image(0, 0, image = bg, anchor = "nw")


start_button = Button(text="Start", width=10)

start_button_canvas = canvas.create_window(350, 400, anchor ="nw", window= start_button)

root.mainloop()