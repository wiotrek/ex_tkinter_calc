from tkinter import *

root = Tk()
root.title('Simple Calculator')
root.configure(background='white', borderwidth=10)
e = Entry(root, width=40, borderwidth=5, font=("Arial", 12), fg='grey', bg='white')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=15)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add_f():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)


def button_equal_f():
    second_number = e.get()
    e.delete(0, END)
    if math == 'subtraction':
        e.insert(0, f_num + int(second_number))
    elif math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    elif math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    elif math == 'division':
        e.insert(0, f_num / int(second_number))


def button_subtract_f():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply_f():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)


def button_divide_f():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)


# create buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg='white')
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg='white')
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg='white')
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg='white')
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg='white')
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg='white')
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg='white')
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg='white')
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg='white')
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg='white')

button_add = Button(root, text="+", padx=40, pady=20, command=button_add_f, bg='white')
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal_f, bg='white')
button_clear = Button(root, text="C", padx=40, pady=20, command=button_clear, bg='white')

button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract_f, bg='white')
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply_f, bg='white')
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide_f, bg='white')

# GRID
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_clear.grid(row=1, column=3)


button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_multiply.grid(row=4, column=2)
button_divide.grid(row=4, column=3)


root.mainloop()
