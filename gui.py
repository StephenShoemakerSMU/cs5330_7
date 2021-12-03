from tkinter import *
from tkinter.ttk import *

mainMenuWindow = Tk()
mainMenuWindow.title("Main Menu")
mainMenuWindow.geometry('300x300')

def clickedPaper():
    print("clicked paper input")
    inputPaperInfoWindow.deiconify()


paperButton = Button(mainMenuWindow, text="Enter Paper Info", command=clickedPaper)
paperButton.grid(column=99, row=1)

inputPaperInfoWindow = Tk()
inputPaperInfoWindow.withdraw()
inputPaperInfoWindow.title("Enter Paper Info")
inputPaperInfoWindow.geometry('400x300')

lbl = Label(inputPaperInfoWindow, text="Paper Title: ")
lbl.grid(column=0, row=0)

txt = Entry(inputPaperInfoWindow, width=10)
txt.grid(column=1, row=0)

lbl1 = Label(inputPaperInfoWindow, text="Publication Name: ")
lbl1.grid(column=0, row=1)

txt1 = Entry(inputPaperInfoWindow, width=10)
txt1.grid(column=1, row=1)

lbl2 = Label(inputPaperInfoWindow, text="Publication Type: ")
lbl2.grid(column=0, row=2)

txt2 = Entry(inputPaperInfoWindow, width=10)
txt2.grid(column=1, row=2)

lbl3 = Label(inputPaperInfoWindow, text="Publication Number: ")
lbl3.grid(column=0, row=3)

txt3 = Entry(inputPaperInfoWindow, width=10)
txt3.grid(column=1, row=3)

lbl4 = Label(inputPaperInfoWindow, text="Publication Year: ")
lbl4.grid(column=0, row=4)

txt4 = Entry(inputPaperInfoWindow, width=10)
txt4.grid(column=1, row=4)

lbl5 = Label(inputPaperInfoWindow, text="Publication Location: ")
lbl5.grid(column=0, row=5)

txt5 = Entry(inputPaperInfoWindow, width=10)
txt5.grid(column=1, row=5)

lbl6 = Label(inputPaperInfoWindow, text="Publication Month: ")
lbl6.grid(column=0, row=6)

txt6 = Entry(inputPaperInfoWindow, width=10)
txt6.grid(column=1, row=6)

lbl7 = Label(inputPaperInfoWindow, text="Publication Volumn: ")
lbl7.grid(column=0, row=7)

txt7 = Entry(inputPaperInfoWindow, width=10)
txt7.grid(column=1, row=7)

lbl8 = Label(inputPaperInfoWindow, text="Publication Page Number: ")
lbl8.grid(column=0, row=8)

txt8 = Entry(inputPaperInfoWindow, width=10)
txt8.grid(column=1, row=8)

def clickedEnter():
    info = txt.get()
    info1 = txt1.get()
    info2 = txt2.get()
    info3 = txt3.get()
    info4 = txt4.get()
    info5 = txt5.get()
    info6 = txt6.get()
    info7 = txt7.get()
    info8 = txt8.get()
    print(info)
    print(info1)
    print(info2)
    print(info3)
    print(info4)
    print(info5)
    print(info6)
    print(info7)
    print(info8)

    txt.delete(0, END)
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)
    txt4.delete(0, END)
    txt5.delete(0, END)
    txt6.delete(0, END)
    txt7.delete(0, END)
    txt8.delete(0, END)

    print("Paper info entered.")

btn = Button(inputPaperInfoWindow, text="Enter", command=clickedEnter)
btn.grid(column=99, row=99)

inputAuthorInfoWindow = Tk()
inputAuthorInfoWindow.withdraw()
inputAuthorInfoWindow.title("Enter AuthorInfo")
inputAuthorInfoWindow.geometry('400x300')

def clickedAuthor():
    print("clicked author input")
    inputAuthorInfoWindow.deiconify()

paperButton = Button(mainMenuWindow, text="Enter Author Info", command=clickedAuthor)
paperButton.grid(column=99, row=2)

Albl = Label(inputAuthorInfoWindow, text="Author First Name: ")
Albl.grid(column=0, row=0)

Atxt = Entry(inputAuthorInfoWindow, width=10)
Atxt.grid(column=1, row=0)

Albl1 = Label(inputAuthorInfoWindow, text="Author Last Name: ")
Albl1.grid(column=0, row=1)

Atxt1 = Entry(inputAuthorInfoWindow, width=10)
Atxt1.grid(column=1, row=1)

Albl2 = Label(inputAuthorInfoWindow, text="Organization Name: ")
Albl2.grid(column=0, row=2)

Atxt2 = Entry(inputAuthorInfoWindow, width=10)
Atxt2.grid(column=1, row=2)

Albl3 = Label(inputAuthorInfoWindow, text="Employment Start Year: ")
Albl3.grid(column=0, row=3)

Atxt3 = Entry(inputAuthorInfoWindow, width=10)
Atxt3.grid(column=1, row=3)

Albl4 = Label(inputAuthorInfoWindow, text="Employment End Year: ")
Albl4.grid(column=0, row=4)

Atxt4 = Entry(inputAuthorInfoWindow, width=10)
Atxt4.grid(column=1, row=4)

def clickedAEnter():
    Ainfo = Atxt.get()
    Ainfo1 = Atxt1.get()
    Ainfo2 = Atxt2.get()
    Ainfo3 = Atxt3.get()
    Ainfo4 = Atxt4.get()

    print(Ainfo)
    print(Ainfo1)
    print(Ainfo2)
    print(Ainfo3)
    print(Ainfo4)


    Atxt.delete(0, END)
    Atxt1.delete(0, END)
    Atxt2.delete(0, END)
    Atxt3.delete(0, END)
    Atxt4.delete(0, END)
    print("Author info entered.")

Abtn = Button(inputAuthorInfoWindow, text="Enter", command=clickedAEnter)
Abtn.grid(column=99, row=99)

"""
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=2, row=1)
"""
if __name__ == "__main__":
    mainMenuWindow.mainloop()