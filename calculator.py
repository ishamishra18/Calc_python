from tkinter import *

root = Tk()
root.minsize(900,900)
root.title("Calculator")
root.anchor("center")
root.configure(background="black")

txtInput=StringVar()
operator=" "

def btnclick(number):
    global operator
    operator = operator+str(number)
    txtInput.set(operator)

def btnDisplayClear():
    global operator
    operator = ""
    txtInput.set("")

def btnEqualsTo():
    global operator
    result=str(eval(operator))
    txtInput.set(result)
    operator = ""

txtDisplay= Entry(root, font=("arial",20,"bold"), textvariable=txtInput, bd=30, insertwidth=4, bg="powder blue", justify="right")
txtInput.set(0)
txtDisplay.grid(columnspan=4)

btn7= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="7", bg="powder blue",
            command=lambda: btnclick(7)).grid(row=2,column=0)
btn8= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="8", bg="powder blue",
             command=lambda: btnclick(8)).grid(row=2,column=1)
btn9= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="9", bg="powder blue",
             command=lambda: btnclick(9)).grid(row=2,column=2)
addition= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="+", bg="powder blue",
             command=lambda: btnclick("+")).grid(row=2,column=3)
#--------------------------------------------------------------------------------------------------------------
btn6= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="6", bg="powder blue",
             command=lambda: btnclick(6)).grid(row=3,column=0)
btn5= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="5", bg="powder blue",
             command=lambda: btnclick(5)).grid(row=3,column=1)
btn4= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="4", bg="powder blue",
             command=lambda: btnclick(4)).grid(row=3,column=2)
subtraction= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",22,"bold"), text="-", bg="powder blue",
             command=lambda: btnclick("-")).grid(row=3,column=3)
#----------------------------------------------------------------------------------------------------------------
btn3= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="3", bg="powder blue",
             command=lambda: btnclick(3)).grid(row=4,column=0)
btn2= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="2", bg="powder blue",
             command=lambda: btnclick(2)).grid(row=4,column=1)
btn1= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="1", bg="powder blue",
             command=lambda: btnclick(1)).grid(row=4,column=2)
multiply= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",22,"bold"), text="*", bg="powder blue",
             command=lambda: btnclick("*")).grid(row=4,column=3)
#-----------------------------------------------------------------------------------------------------------------
btn0= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="0", bg="powder blue",
             command=lambda: btnclick(0)).grid(row=5,column=0)
btnClear= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="C", bg="powder blue",
             command=lambda: btnDisplayClear()).grid(row=5,column=1)
btnEqual= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="=", bg="powder blue",
             command=lambda: btnEqualsTo()).grid(row=5,column=2)
division= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="/", bg="powder blue",
             command=lambda: btnclick("/")).grid(row=5,column=3)
#-----------------------------------------------------------------------------------------------------------------
btnbkt1= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text="(", bg="powder blue",
             command=lambda: btnclick("(")).grid(row=6,column=0)
btnbkt2= Button(root, padx=16, pady=16, bd=8, fg="black", font=("arial",20,"bold"), text=")", bg="powder blue",
             command=lambda: btnclick(")")).grid(row=6,column=2)

mainloop()