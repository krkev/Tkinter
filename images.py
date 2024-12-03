from tkinter import * 
from PIL import ImageTk, Image

root = Tk()
root.title('Gallery')
root.iconbitmap('C:/Users/kevin/OneDrive/Bureau/python/icons/Gallery.ico')
root.geometry('420x500')
root.config(bg="#212121")


my_image_1 = ImageTk.PhotoImage( Image.open("images/Img_1.jpg").resize((400, 400)))
my_image_2 = ImageTk.PhotoImage( Image.open("images/Img_2.jpg").resize((400, 400)))
my_image_3 = ImageTk.PhotoImage( Image.open("images/Img_3.jpg").resize((400, 400)))
my_image_4 = ImageTk.PhotoImage( Image.open("images/Img_4.jpg").resize((400, 400)))
my_image_5 = ImageTk.PhotoImage( Image.open("images/Img_5.png").resize((400, 400)))
my_image_6 = ImageTk.PhotoImage( Image.open("images/Img_6.jpg").resize((400, 400)))

my_label = Label(image=my_image_1, border=0)
image_list = [my_image_1, my_image_2, my_image_3, my_image_4, my_image_5, my_image_6]
my_label.grid(row=0, column=0, columnspan=3, pady=10)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    button_forward = Button(
            root, 
            text=">>",  
            width=8, 
            height=3, 
            bg="#212121",
            fg="#f2f2f2",
            border=0,
            activebackground="#20a8a2",
            highlightthickness=2,
            command=lambda: forward(image_number + 1)
        )
    
    button_back = Button(
        root, 
        text="<<", 
        width=8, 
        height=3,
        bg="#212121",
        fg="#f2f2f2",
        border=0,
        activebackground="#20a8a2",
        highlightthickness=2, 
        command=lambda: back(image_number -1)
    )

    if image_number == (len(image_list) - 1):
        button_forward = Button(root, text=">>",  width=8, height=3, border=0, state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3, pady=10)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)



def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    button_forward = Button(
            root, 
            text=">>",  
            width=8, 
            height=3, 
            bg="#212121",
            fg="#f2f2f2",
            border=0,
            activebackground="#20a8a2",
            highlightthickness=2,
            command=lambda: forward(image_number + 1)
        )
    button_back = Button(
        root, 
        text="<<", 
        width=8, 
        height=3,
        bg="#212121",
        fg="#f2f2f2",
        border=0,
        activebackground="#20a8a2",
        highlightthickness=2, 
        command=lambda: back(image_number -1)
    )

    if image_number == (-len(image_list)):
        button_back = Button(root, text="<<", width=8, height=3, border=0, state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3, pady=10)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    
    


button_back = Button(
        root, 
        text="<<", 
        width=8, 
        height=3, 
        bg="#212121",
        fg="#f2f2f2",
        border=0,
        activebackground="#20a8a2",
        highlightthickness=2,
        command=back
    )
button_exit = Button(
        root, 
        text="Exit", 
        width=8, 
        height=3, 
        bg="#20a8a2",
        fg="#f2f2f2",
        border=0,
        activebackground="#20a8a2",
        activeforeground="#20a8a2",
        # highlightbackground="#20a8a2",
        highlightthickness=2,
        command=root.quit
    )

button_forward = Button(
        root, 
        text=">>",  
        width=8, 
        height=3,
        bg="#212121",
        fg="#f2f2f2", 
        border=0,
        highlightbackground="#20a8a2",
        highlightthickness=2,
        command=lambda: forward(1)
    )

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop() 