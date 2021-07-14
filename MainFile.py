from tkinter import *
import tkinter as tk
root=Tk()
root.title("Simple Calculator")
e=tk.Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
global  f_num
global operation
def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)
    f_num=0
    operation=' '

def button_add():
    global f_num
    global operation
    first_number=e.get()
    f_num=int(first_number)
    e.delete(0,END)
    operation='+'
    e.insert(0,str(f_num )+"+")

def button_sub():
    global f_num
    global operation
    first_number=e.get()
    f_num=int(first_number)
    e.delete(0,END)
    operation='-'
    e.insert(0,str(f_num )+"-")

def button_Mul():
    global f_num
    global operation
    first_number=e.get()
    f_num=int(first_number)
    e.delete(0,END)
    operation='*'
    e.insert(0,str(f_num )+"*")

def button_Divide():
    global f_num
    global operation
    first_number=e.get()
    f_num=int(first_number)
    e.delete(0,END)
    operation='/'
    e.insert(0,str(f_num )+"/")

def button_equal():
    second_num=e.get()
    index=second_num.find(operation)
    num=second_num[index+1:len(second_num)]
    e.delete(0,END)
    if operation=="+":
        e.insert(0,str(f_num + int(num)))
    elif operation =="-":
        e.insert(0, str(f_num - int(num)))
    elif operation=='*':
        e.insert(0, str(f_num * int(num)))
    elif operation=='/':
        e.insert(0, str(f_num / int(num)))



#Define Buttons
button_0=Button(root,bg='blue',text='0',padx=40,pady=20,command=lambda: button_click(0))
button_1=Button(root,bg='blue',text='1',padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root,bg='blue',text='2',padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,bg='blue',text='3',padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root,bg='blue',text='4',padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root,bg='blue',text='5',padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root,bg='blue',text='6',padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root,bg='blue',text='7',padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,bg='blue',text='8',padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root,bg='blue',text='9',padx=40,pady=20,command=lambda: button_click(9))

button_add=Button(root,bg='red',text='+',padx=39,pady=20,command=button_add)
button_subtract=Button(root,bg='red',text='-',padx=39,pady=20,command=button_sub)
button_Multiply=Button(root,bg='red',text='*',padx=45,pady=20,command=button_Mul)
Button_Div=Button(root,bg='red',text='/',padx=39,pady=20,command=button_Divide)
button_equal=Button(root,bg='#54FA9B',text='=',padx=91,pady=20,command=button_equal)
button_clear =Button(root,bg='white',text='Clear',padx=79,pady=20,command=button_clear)

# Put the buttons on the screen
button_0.grid(row=4,column=0)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_subtract.grid(row=6,column=0)
button_Multiply.grid(row=6,column=1)
Button_Div.grid(row=6,column=2)
button_equal.grid(row=5,column=1,columnspan=2)


root.mainloop()