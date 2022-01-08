from tkinter import *

window = Tk()
window.title("Message box title")
window.geometry("300x75")
label = Label(window, text="My message content!")
label.pack()
button = Button(window, text="Ok", width=10, command=window.destroy)
button.pack(side=RIGHT)
window.mainloop()
