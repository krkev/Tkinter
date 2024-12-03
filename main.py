from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.configure(bg="#212121")
# root.geometry("200x100")


myLabel = Label(root, text="Calculator", font=("Helvetical", 15, "bold"), bg="#212121", fg="orange")
myLabel.grid(row=0, column=0, columnspan=5, pady=8)

e = Entry(root, width=40, borderwidth=4, font=("Arial", 10, "bold"))
e.grid(row=1, column=0, columnspan=5, pady=10)

f_num = 0
operation = ""

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_math(op):
    first_number = e.get()
    e.delete(0, END)
    global f_num
    global operation
    operation = f"{op}"
    f_num = int(first_number)


def button_equal():
    second_number  = e.get()
    e.delete(0, END)
    if operation == "addition":
        e.insert(0, math.floor(f_num + int(second_number)))
    if operation == "substraction":
        e.insert(0, math.floor(f_num - int(second_number)))
    if operation == "multiplication":
        e.insert(0, math.floor(f_num * int(second_number)))
    if operation == "division":
        e.insert(0, math.floor(f_num / int(second_number)))

def button_clear():
    e.delete(0, END)


button_0 = Button(root, text="0", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(9))
button_add = Button(root, text="+", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_math("addition"))
button_substract = Button(root, text="-", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_math("substraction"))
button_multiply = Button(root, text="*", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_math("multiplication"))
button_divide = Button(root, text="/", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_math("division"))
button_equal = Button(root, text="=", bg="orange", fg="#212121", padx=45, pady=20, command=button_equal)
button_clear = Button(root, text="c", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=button_clear)

button_9.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_7.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_6.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_4.grid(row=3, column=2)
button_substract.grid(row=3, column=3)

button_3.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_1.grid(row=4, column=2)
button_multiply.grid(row=4, column=3)

button_0.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_clear.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()