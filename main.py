from tkinter import *

root = Tk()
root.geometry("300x445")
root.title("E-Math")

bar = Entry(root,width=50,font=("Nunito",40,"normal"),fg="#000000",bg="#131313", justify=RIGHT)
bar.place(x=0,y=3, width=300, height=120)

X = 75
Y = 100

###################################################################################################

def insert(num):
    bar['fg']="white"
    text = bar.get()
    if (text.split() == []) and (num=="/" or num=="*" or num==")"):
        num = ''
        
    elif (text.endswith('')) and (num=="+" or num=="-" or num=="/" or num==""):
        BackSpace()
    elif (text.endswith('/')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        BackSpace()
    elif (text.endswith('+')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        BackSpace()
    elif (text.endswith('-')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        BackSpace()

    elif (text.endswith('.')) and (num=="." or num=="+" or num=="-" or num=="/" or num=="*"):
        num=''
    bar.insert(END,num)

def BackSpace():
    bar['fg']="white"
    try:
        text = bar.get()
        l = list(text)
        l.pop()
        Text = ""
        for i in range(len(l)):
            Text += l[i]
        bar.delete(0,END)
        bar.insert(0,Text)
    except:
        None
        
def Delete():
    bar['fg']="white"
    bar.delete(0,END)

def BracketCheck():
    text = str(bar.get())
    Text = list(text)
    a=0
    for i in range(len(Text)):
        if Text[i] == "(":
            a+=1
    b=0
    for i in range(len(Text)):
        if Text[i] == ")":
            b+=1
    Add = a-b
    return Add

def Answer():
    text = str(bar.get())

    Add = BracketCheck()
    if Add>0:
        bar.insert(END,Add*")")
    
    else:
        try:
            answer = eval(text)
            Delete()
            bar.insert(0,answer)
            bar['fg'] = "white"
        except:
            bar['fg'] = "red"

###################################################################################################

n1 = Button(root,text="1",font=("Nunito",16,"bold"),padx = 27, pady = 20, bd =0,bg="#000000", fg='white', command=lambda:insert("1"))
n1.place(x=0,y=Y+45)

n2 = Button(root,text="2",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("2"))
n2.place(x=X,y=Y+45)

n3 = Button(root,text="3",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("3"))
n3.place(x=2*X,y=Y+45)

n4 = Button(root,text="4",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("4"))
n4.place(x=0,y=(2*Y)+20)

n5 = Button(root,text="5",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("5"))
n5.place(x=X,y=(2*Y)+20)

n6 = Button(root,text="6",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("6"))
n6.place(x=2*X,y=(2*Y)+20)

n7 = Button(root,text="7",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("7"))
n7.place(x=0,y=(3*Y)-5)

n8 = Button(root,text="8",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("8"))
n8.place(x=X,y=(3*Y)-5)

n9 = Button(root,text="9",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("9"))
n9.place(x=2*X,y=(3*Y)-5)

n0 = Button(root,text="0",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='white',command=lambda:insert("0"))
n0.place(x=X,y=(4*Y)-30)

####################################################################################################

dot = Button(root,text=".",font=("Nunito",16,"bold"),padx = 28, pady = 20, bd =0,bg="#000000", fg='#ffffff',command=lambda:insert("."))
dot.place(x=0,y=(4*Y)-30)

equal = Button(root,text="=",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#FF9D0C",command=Answer)
equal.place(x=2*X,y=(4*Y)-30)

####################################################################################################

mult = Button(root,text="X",font=("Nunito",16,"bold"),padx = 24, pady = 20, bd =0,bg="#000000", fg='#FF9D0C', command=lambda:insert("*"))
mult.place(x=3*X,y=Y+45)

div = Button(root,text="/",font=("Nunito",16,"bold"),padx = 28, pady = 20, bd =0,bg="#000000", fg='#FF9D0C',command=lambda:insert("/"))
div.place(x=3*X,y=(2*Y)+20)

plus = Button(root,text="+",font=("Nunito",16,"bold"),padx = 26, pady = 20, bd =0,bg="#000000", fg='#FF9D0C',command=lambda:insert("+"))
plus.place(x=3*X,y=(3*Y)-5)

minus = Button(root,text="-",font=("Nunito",16,"bold"),padx = 28, pady = 20, bd =0,bg="#000000", fg='#FF9D0C',command=lambda:insert("-"))
minus.place(x=3*X,y=(4*Y)-30)

#####################################################################################################

AC = Button(root,text="AC",font=("Nunito",16,"bold"),padx = 24,pady = 8,bd =0,bg="#000000", fg='#FF9D0C',command=Delete)
AC.place(x=0,y=Y-6)

back = Button(root,text=u"\u2190",font=("Nunito",16,"bold"),padx = 24,pady = 8,bd =0,bg="#000000", fg='#FF9D0C',command=BackSpace)
back.place(x=X,y=Y-6)

Open = Button(root,text="(",font=("Nunito",16,"bold"),padx = 28,pady = 8,bd =0,bg="#000000", fg='#FF9D0C',command=lambda:insert("("))
Open.place(x=2*X,y=Y-6)

Close = Button(root,text=")",font=("Nunito",16,"bold"),padx = 28,pady = 8,bd =0,bg="#000000", fg='#FF9D0C',command=lambda:insert(")"))
Close.place(x=3*X,y=Y-6)

root.mainloop()