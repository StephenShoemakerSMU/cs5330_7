
from tkinter import *
from tkinter.ttk import *

paperFields = ["title", {"authors":["fname", "lname","organization", "startYear", "endYear"], "type":"array"},{"publication": ["name", "month","year","type"], "type": "dict"}]
import db
def insertForm(root, fields, action):
    entryValue = {}

    for field in fields:
        
        if isinstance(field,dict):
            if(field["type"]=="dict"):
                entryValue[list(field.keys())[0]] = {}
                label = Label(root, text = list(field.keys())[0])
                label.pack(side=TOP)
                for innerField in field[list(field.keys())[0]]:
                    label = Label(root, text = innerField)
                    label.pack(side=TOP)

                    entry = Entry(root, width = 20)
                    entry.pack(side=TOP)
                    entryValue[list(field.keys())[0]][innerField] = entry
            else:
                authorFrame = Frame(root)
                authorFrame.pack(side=TOP)
                print(field)
                entryValue[list(field.keys())[0]] = []
                entryValue[list(field.keys())[0]].append({})
                label = Label(authorFrame, text = list(field.keys())[0])
                label.pack(side=TOP)
                for innerField in field[list(field.keys())[0]]:
                    label = Label(authorFrame, text = innerField)
                    label.pack(side=TOP)

                    entry = Entry(authorFrame, width = 20)
                    entry.pack(side=TOP)
                    entryValue[list(field.keys())[0]][0][innerField] = entry

                def addAuthorButton(newFields):
                    newAuthor = {}
                    for innerField in newFields:
                        label = Label(authorFrame, text = innerField)
                        label.pack(side=TOP)

                        entry = Entry(authorFrame, width = 20)
                        entry.pack(side=TOP)
                        newAuthor[innerField] = entry
                    entryValue["authors"].append(newAuthor)
                    

                addAuthor = Button(authorFrame, text = "addAuthor", command = lambda : addAuthorButton(fields[1]["authors"]))
                addAuthor.pack(side=BOTTOM)

        else:
            label = Label(root, text = field)
            label.pack(side=TOP)
            entry = Entry(root, width = 20)
            entry.pack(side=TOP)
            entryValue[field] = entry

    submit = Button(root, text = "Submit", command = lambda : action(entryValue))
    submit.pack(side=TOP)
    




def submit(entries):
    dbDict = {}
    for entry in entries:
        
        if(isinstance(entries[entry],dict)):
            dbDict[entry] = {}
            for innerEntry in entries[entry].keys():
                dbDict[entry][innerEntry] = entries[entry][innerEntry].get()
        elif(isinstance(entries[entry],list)):
            dbDict[entry] = []
            for author in entries[entry]:
                dbAuthor = {}
                for innerEntry in author.keys():
                    dbAuthor[innerEntry] = author[innerEntry].get()
                dbDict[entry].append(dbAuthor)
        else:
            dbDict[entry] = entries[entry].get()
    db.submitPaper(dbDict)
            
        
insertWindow = Tk()
insertWindow.title("Insert Menu")    


insertForm(insertWindow, paperFields, submit)



def query1Frame(window):
    queryLabel = Label(window,text = "Paper Name")
    queryEntry = Entry(window) 
    queryLabel.pack(side=TOP)
    queryEntry.pack(side=TOP)

    def query1(root,name):
        result = db.getPaper(name)
        print(result)
        for paper in result:
            print(paper, ": " , result[paper])


    processQuery = Button(window, text= "Process Query", command=lambda: query1(window,queryEntry.get()))
    processQuery.pack(side=TOP)

q1Window = Frame(insertWindow)
q1Window.pack(side=RIGHT)


query1Frame(q1Window)


insertWindow.mainloop()