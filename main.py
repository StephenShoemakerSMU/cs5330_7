from pymongo import MongoClient

from pprint import pprint

from tkinter import *
from tkinter import ttk

client= MongoClient("mongodb://root:example@localhost:27017")

db = client["paperDB"]

papers = db["papers"]
papers.create_index("title")
papers.create_index("authors")
papers.create_index("publication.name")
papers.create_index("publication.year")

authors = db["authors"]
papers.create_index("name")

def addAuthor(entries):
    try:
        for ent in entries:
            print(entries[ent].get())
    except ValueError:
        pass


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        
        row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
        lab.pack(side = LEFT)
        ent.pack(side = RIGHT, expand = YES, fill = X)
        entries[field] = ent

    row = Frame(root)
    row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
    Button(row, width=22, text="Submit Author",command=lambda e =entries: addAuthor(e)).pack(side="left")
    return entries

authorFields=("First Name", "Last Name", "Organization", "Start Year", "Last Year")

root = Tk()
makeform(root,authorFields)

root.mainloop()

