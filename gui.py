from tkinter import *
from tkinter.ttk import *

mainMenuWindow = Tk()
mainMenuWindow.title("Main Menu")

mainMenuWindow.geometry('300x300')

def clickedQ1():
    print("clicked paper input")
    q1.deiconify()

def clickedQ2():
    print("clicked paper input")
    q2.deiconify()

def clickedQ3():
    print("clicked paper input")
    q3.deiconify()

q1 = Tk()
q1.withdraw()
q1.title("Search by paper name")
q1.geometry('400x300')

q1lbl = Label(q1, text="Name of the Paper: ")
q1lbl.grid(column=0, row=0)
q1txt = Entry(q1, width=10)
q1txt.grid(column=1, row=0)
def clickedQ1Enter():
    print("clicked Q1 Enter")
    q1txt.delete(0,END)
btn = Button(q1, text="Enter", command=clickedQ1Enter)
btn.grid(column=99, row=99)


q2 = Tk()
q2.withdraw()
q2.title("Search by author name")
q2.geometry('400x300')

q2lbl = Label(q2, text="Name of the author: ")
q2lbl.grid(column=0, row=0)
q2txt = Entry(q2, width=10)
q2txt.grid(column=1, row=0)
def clickedQ2Enter():
    print("clicked Q2 Enter")
    q2txt.delete(0,END)
btn = Button(q2, text="Enter", command=clickedQ2Enter)
btn.grid(column=99, row=99)

q3 = Tk()
q3.withdraw()
q3.title("Search by publication and year range")
q3.geometry('400x300')

q3lbl = Label(q3, text="Name of the author: ")
q3lbl.grid(column=0, row=0)
q3txt = Entry(q3, width=10)
q3txt.grid(column=1, row=0)
q3lbl1 = Label(q3, text="start year: ")
q3lbl1.grid(column=0, row=1)
q3txt1 = Entry(q3, width=10)
q3txt1.grid(column=1, row=1)
q3lbl2 = Label(q3, text="end year: ")
q3lbl2.grid(column=0, row=2)
q3txt2 = Entry(q3, width=10)
q3txt2.grid(column=1, row=2)
def clickedQ3Enter():
    print("clicked Q3 Enter")
    q3txt.delete(0,END)
    q3txt1.delete(0, END)
    q3txt2.delete(0, END)
btn = Button(q3, text="Enter", command=clickedQ3Enter)
btn.grid(column=99, row=99)

query1Button = Button(mainMenuWindow, text="Search by paper name", command=clickedQ1)
query1Button.grid(column=99, row=3)
query2Button = Button(mainMenuWindow, text="Search by author name", command=clickedQ2)
query2Button.grid(column=99, row=4)
query3Button = Button(mainMenuWindow, text="Search by publication and year range", command=clickedQ3)
query3Button.grid(column=99, row=5)




def clickedPaper():
    print("clicked paper input")
    inputInfoWindow.deiconify()


paperButton = Button(mainMenuWindow, text="Enter Paper Info", command=clickedPaper)
paperButton.grid(column=99, row=1)

inputInfoWindow = Tk()
inputInfoWindow.withdraw()
inputInfoWindow.title("Enter Paper Info")
width = 500
height = 500

inputInfoWindow.geometry('%sx%s'%(width,height))

lbl = Label(inputInfoWindow, text="Paper Title: ")
lbl.grid(column=0, row=0)

txt = Entry(inputInfoWindow, width=10)
txt.grid(column=1, row=0)

lbl1 = Label(inputInfoWindow, text="Publication Name: ")
lbl1.grid(column=0, row=1)

txt1 = Entry(inputInfoWindow, width=10)
txt1.grid(column=1, row=1)

lbl2 = Label(inputInfoWindow, text="Publication Type: ")
lbl2.grid(column=0, row=2)

txt2 = Entry(inputInfoWindow, width=10)
txt2.grid(column=1, row=2)

lbl3 = Label(inputInfoWindow, text="Publication Number: ")
lbl3.grid(column=0, row=3)

txt3 = Entry(inputInfoWindow, width=10)
txt3.grid(column=1, row=3)

lbl4 = Label(inputInfoWindow, text="Publication Year: ")
lbl4.grid(column=0, row=4)

txt4 = Entry(inputInfoWindow, width=10)
txt4.grid(column=1, row=4)

lbl5 = Label(inputInfoWindow, text="Publication Location: ")
lbl5.grid(column=0, row=5)

txt5 = Entry(inputInfoWindow, width=10)
txt5.grid(column=1, row=5)

lbl6 = Label(inputInfoWindow, text="Publication Month: ")
lbl6.grid(column=0, row=6)

txt6 = Entry(inputInfoWindow, width=10)
txt6.grid(column=1, row=6)

lbl7 = Label(inputInfoWindow, text="Publication Volumn: ")
lbl7.grid(column=0, row=7)

txt7 = Entry(inputInfoWindow, width=10)
txt7.grid(column=1, row=7)

lbl8 = Label(inputInfoWindow, text="Publication Page Number: ")
lbl8.grid(column=0, row=8)

txt8 = Entry(inputInfoWindow, width=10)
txt8.grid(column=1, row=8)


authorEntryList = []

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

    transformedAuthorList=[]
    for author in authorEntryList:
        transformedAuthor = {}
        for label in author["label"].keys():
            transformedAuthor[label]=author["entry"][label].get()
        transformedAuthorList.append(transformedAuthor)

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

count = 0


def addAuthor():
    global count
    entry = {}
    label = {}
    author = {}

    
    name = Label(inputInfoWindow, text="Author First Name: ")
    name.grid(column=0, row=9 + 6*count)


    Atxt = Entry(inputInfoWindow, width=10)
    Atxt.grid(column=1, row=9 + 6*count)

    label["fname"] = name
    entry["fname"] = Atxt

    Albl1 = Label(inputInfoWindow, text="Author Last Name: ")
    Albl1.grid(column=0, row=10 + 6*count)

    Atxt1 = Entry(inputInfoWindow, width=10)
    Atxt1.grid(column=1, row=10 + 6*count)

    label["lname"] = name
    entry["lname"] = Atxt1

    Albl2 = Label(inputInfoWindow, text="Organization Name: ")
    Albl2.grid(column=0, row=11 + 6*count)

    Atxt2 = Entry(inputInfoWindow, width=10)
    Atxt2.grid(column=1, row=11 + 6*count)

    label["organization"] = Albl2
    entry["organization"] = Atxt2

    Albl3 = Label(inputInfoWindow, text="Employment Start Year: ")
    Albl3.grid(column=0, row=12 + 6*count)

    Atxt3 = Entry(inputInfoWindow, width=10)
    Atxt3.grid(column=1, row=12 + 6*count)

    label["startYear"] = Albl3
    entry["startYear"] = Atxt3

    Albl4 = Label(inputInfoWindow, text="Employment End Year: ")
    Albl4.grid(column=0, row=13 + 6*count)

    Atxt4 = Entry(inputInfoWindow, width=10)
    Atxt4.grid(column=1, row=13 + 6*count)

    label["endYear"] = Albl3
    entry["endYear"] = Atxt3

    author["entry"] = entry
    author["label"] = label

    authorEntryList.append(author)
    count+=1
    

addAuthor()




btn = Button(inputInfoWindow, text="Add Author", command=addAuthor)
btn.grid(column=0, row=998)

btn1 = Button(inputInfoWindow, text="Enter", command=clickedEnter)
btn1.grid(column=999, row=999)



'''
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
'''

"""
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=2, row=1)
"""
if __name__ == "__main__":
    mainMenuWindow.mainloop()