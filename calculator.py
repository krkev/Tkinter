from tkinter import *

root = Tk()
root.title("Simple Calculator")

# class Calculator:
#     def __init__(self):
#         self.first_number = 0
    
#     def add(self, number):
#         self.first_number = number
    
#     def equals(self, number):
#         return self.first_number + int(number)

    
f_num = 0
# s_num = 0
operation = ""
        
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan= 3)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equals():
     second_number = e.get()
     e.delete(0, END)
    #  global operation
    #  print(f_num + int(second_number))
     if operation == "addition":
        e.insert(0, f_num + int(second_number))

     if operation == "substraction":
        e.insert(0, f_num - int(second_number))

     if operation == "multiplication":
        e.insert(0, f_num * int(second_number))

     if operation == "division":
        e.insert(0, f_num / int(second_number))

def button_add():
    global operation
    global f_num
    operation = "addition"
    first_number = e.get()
    # global f_num 
    f_num= int(first_number)
    e.delete(0, END)
    

def button_substract():
    global operation
    global f_num
    operation = "substraction"
    first_number = e.get()
    f_num= int(first_number)
    e.delete(0, END)
    

def button_multiply():
    global operation
    global f_num
    operation = "multiplication"
    first_number = e.get()
    # global f_num 
    f_num= int(first_number)
    e.delete(0, END)
   

def button_divide():
    global operation
    global f_num
    operation = "division"
    first_number = e.get()
    # global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    
def button_clear():
    e.delete(0, END)

button_1 = Button(root, text="1", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2",  bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3",  bg="#212121", fg="#f2f2f2",padx=45, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4",  bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8",  bg="#212121", fg="#f2f2f2",padx=45, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9",  bg="#212121", fg="#f2f2f2",padx=45, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0",  bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", bg="#212121", fg="#f2f2f2", padx=95, pady=20, command=button_add)
button_substract = Button(root, text="-", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=button_substract)
button_multiply = Button(root, text="*",  bg="#212121", fg="#f2f2f2",padx=45, pady=20, command=button_multiply)
button_divide = Button(root, text="/", bg="#212121", fg="#f2f2f2", padx=45, pady=20, command=button_divide)
button_clear = Button(root, text="C",  bg="#212121", fg="#f2f2f2",padx=45, pady=20, command=button_clear)
button_equals = Button(root, text="=", bg="orangered", fg="#f2f2f2", padx=95, pady=20, command= button_equals)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1, columnspan=2)

button_clear.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2)

button_substract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()