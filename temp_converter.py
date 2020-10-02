from tkinter import *
from functools import partial 

tempVal = "Celsius"

# getting drop down value
def store_temp(set_temp):
    global tempVal
    tempVal = set_temp

def converter(rl1, rl2, inputn):
    temp = inputn.get()
    if tempVal == 'Celsius':
        f = float((float(temp) * 9 / 5) + 32)
        k = float((float(temp) + 273.15))
        rl1.config(text="%f °F" % f,font="times 10 italic")
        rl2.config(text="%f °K" % k,font="times 10 italic")
    if tempVal == 'Fahrenheit':
        c = float((float(temp) - 32) * 5 / 9)
        k = c + 273
        rl1.config(text="%f °C" % c,font="times 10 italic")
        rl2.config(text="%f °K" % k,font="times 10 italic")
    if tempVal == 'Kelvin':
        c = float((float(temp) - 273.15))
        f = float((float(temp) - 273.15) * 1.1000 + 32.00)
        rl1.config(text="%f °C" % c,font="times 10 italic")
        rl2.config(text="%f °F" % f,font="times 10 italic")
    return

root = Tk()

root.geometry("500x400")
root.maxsize(415,300)
root.minsize(415,300)
root.title(27*" "+"Temperature Converter")
root.configure(bg="dark orange")


tempvalue =StringVar()
var = StringVar()
temp_label = Label(root,text="Enter Temperature",bg="dark orange",fg="white",font="times 12 bold italic").place(x=10,y=100)

temp_entry = Entry(root,textvariable=tempvalue,relief=SUNKEN,borderwidth=6).place(x=150,y=100)

result_label1 =Label(root,bg="dark orange",fg="white")
result_label1.place(x=160,y=200)
result_label2 = Label(root,bg="dark orange",fg="white")
result_label2.place(x=160,y=230)

#dropdown list
list1= ["Celsius", "Fahrenheit", "Kelvin"]
droplist = OptionMenu(root,var,*list1,command=store_temp)
var.set(list1[0])
droplist.config(width=10,relief=RAISED,bg="dark orange",fg="white")
droplist.place(x=295,y=100)

#conversion
converter = partial(converter,result_label1,result_label2,tempvalue)
result = Button(root,text="Convert",width=12,fg="dark orange",bg="white",relief=RAISED,borderwidth=3,font="times 10 bold", command=converter).place(x=170,y=150)

root.mainloop()