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
    q1txt.delete(0, END)


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
    q2txt.delete(0, END)


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
    q3txt.delete(0, END)
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
width = 700
height = 500

trigger = 0

inputInfoWindow.geometry('%sx%s' % (width, height))
Clbl = Label(inputInfoWindow, text="Conference Name: ")
Clbl.grid(column=0, row=1)

Ctxt = Entry(inputInfoWindow, width=10)
Ctxt.grid(column=1, row=1)

Clbl1 = Label(inputInfoWindow, text="Conference number of times: ")
Clbl1.grid(column=0, row=2)

Ctxt1 = Entry(inputInfoWindow, width=10)
Ctxt1.grid(column=1, row=2)

Clbl2 = Label(inputInfoWindow, text="Conference year: ")
Clbl2.grid(column=0, row=3)

Ctxt2 = Entry(inputInfoWindow, width=10)
Ctxt2.grid(column=1, row=3)

Clbl3 = Label(inputInfoWindow, text="Conference location: ")
Clbl3.grid(column=0, row=4)

Ctxt3 = Entry(inputInfoWindow, width=10)
Ctxt3.grid(column=1, row=4)

Jlbl = Label(inputInfoWindow, text="Journal Name: ")
Jlbl.grid(column=5, row=1)

Jtxt = Entry(inputInfoWindow, width=10)
Jtxt.grid(column=6, row=1)

Jlbl1 = Label(inputInfoWindow, text="Journal year: ")
Jlbl1.grid(column=5, row=2)

Jtxt1 = Entry(inputInfoWindow, width=10)
Jtxt1.grid(column=6, row=2)

Jlbl2 = Label(inputInfoWindow, text="Journal month: ")
Jlbl2.grid(column=5, row=3)

Jtxt2 = Entry(inputInfoWindow, width=10)
Jtxt2.grid(column=6, row=3)

Jlbl2 = Label(inputInfoWindow, text="Journal volumn number: ")
Jlbl2.grid(column=5, row=4)

Jtxt2 = Entry(inputInfoWindow, width=10)
Jtxt2.grid(column=6, row=4)

URLlbl = Label(inputInfoWindow, text="URL: ")
URLlbl.grid(column=0, row=5)

URLlbl = Entry(inputInfoWindow, width=10)
URLlbl.grid(column=1, row=5)

PageNLbl = Label(inputInfoWindow, text="Page Number: ")
PageNLbl.grid(column=0, row=6)

PageNtxt = Entry(inputInfoWindow, width=10)
PageNtxt.grid(column=1, row=6)

authorEntryList = []

def clickedCEnter():
    global trigger
    trigger = 1
    Cinfo = Ctxt.get()
    Cinfo1 = Ctxt1.get()
    Cinfo2 = Ctxt2.get()
    Cinfo3 = Ctxt3.get()
    print(Cinfo)
    print(Cinfo1)
    print(Cinfo2)
    print(Cinfo3)

    Ctxt.delete(0, END)
    Ctxt1.delete(0, END)
    Ctxt2.delete(0, END)
    Ctxt3.delete(0, END)
    transformedAuthorList = []
    for author in authorEntryList:
        transformedAuthor = {}
        for label in author["label"].keys():
            transformedAuthor[label] = author["entry"][label].get()
        transformedAuthorList.append(transformedAuthor)
    print("Conference info entered.")
    print(transformedAuthorList)

def clickedJEnter():
    global trigger
    trigger = 2
    Jinfo = Jtxt.get()
    Jinfo1 = Jtxt1.get()
    Jinfo2 = Jtxt2.get()
    print(Jinfo)
    print(Jinfo1)
    print(Jinfo2)

    Jtxt.delete(0, END)
    Jtxt1.delete(0, END)
    Jtxt2.delete(0, END)
    transformedAuthorList = []
    for author in authorEntryList:
        transformedAuthor = {}
        for label in author["label"].keys():
            transformedAuthor[label] = author["entry"][label].get()
        transformedAuthorList.append(transformedAuthor)
    print("Journal info entered.")
    print(transformedAuthorList)
count = 0


def addAuthor():
    global count
    entry = {}
    label = {}
    author = {}

    name = Label(inputInfoWindow, text="Author First Name: ")
    name.grid(column=0, row=9 + 6 * count)

    Atxt = Entry(inputInfoWindow, width=10)
    Atxt.grid(column=1, row=9 + 6 * count)

    label["fname"] = name
    entry["fname"] = Atxt

    Albl1 = Label(inputInfoWindow, text="Author Last Name: ")
    Albl1.grid(column=0, row=10 + 6 * count)

    Atxt1 = Entry(inputInfoWindow, width=10)
    Atxt1.grid(column=1, row=10 + 6 * count)

    label["lname"] = name
    entry["lname"] = Atxt1

    Albl2 = Label(inputInfoWindow, text="Organization Name: ")
    Albl2.grid(column=0, row=11 + 6 * count)

    Atxt2 = Entry(inputInfoWindow, width=10)
    Atxt2.grid(column=1, row=11 + 6 * count)

    label["organization"] = Albl2
    entry["organization"] = Atxt2

    Albl3 = Label(inputInfoWindow, text="Employment Start Year: ")
    Albl3.grid(column=0, row=12 + 6 * count)

    Atxt3 = Entry(inputInfoWindow, width=10)
    Atxt3.grid(column=1, row=12 + 6 * count)

    label["startYear"] = Albl3
    entry["startYear"] = Atxt3

    Albl4 = Label(inputInfoWindow, text="Employment End Year: ")
    Albl4.grid(column=0, row=13 + 6 * count)

    Atxt4 = Entry(inputInfoWindow, width=10)
    Atxt4.grid(column=1, row=13 + 6 * count)

    label["endYear"] = Albl3
    entry["endYear"] = Atxt3

    author["entry"] = entry
    author["label"] = label

    authorEntryList.append(author)
    count += 1


addAuthor()

btn = Button(inputInfoWindow, text="Add Author", command=addAuthor)
btn.grid(column=0, row=998)

btn1 = Button(inputInfoWindow, text="EnterConference", command=clickedCEnter)
btn1.grid(column=998, row=999)

btn2 = Button(inputInfoWindow, text="EnterJournal", command=clickedJEnter)
btn2.grid(column=999, row=999)

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