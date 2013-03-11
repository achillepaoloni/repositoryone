# File: DBWithEventRECOK.py

import persistent

from Tkinter import *

from ZODB.FileStorage import FileStorage

from ZODB.DB import DB

import transaction

storage = FileStorage('PaoloniAchilleZODB.fs')

db = DB(storage)

connection = db.open()

connessionemy = connection.root()

class AchillePaoloni(persistent.Persistent):

    ##def setRecordBorse(self, Denominazione, DataNascita, Comune, Telefono):

    def __init__(self):

        self.Denominazione = "PAOLONI ACHILLE"

connessionemy['PaoloniAchille'] = AchillePaoloni()

connessionemy['09111963'] = AchillePaoloni()

connessionemy['ROMA'] = AchillePaoloni()

connessionemy['00169'] = AchillePaoloni()

class App(Frame):

    def __init__(self, master=None):

        frame = Frame(master)

        frame.pack()

        self.contents = StringVar()

        ##self.contents.set(connessionemy.keys()[:2] )

        self.contents.set(connessionemy.keys())

        self.button = Button(frame, text="USCITA", fg="red", command=frame.quit)

        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Nominativo", command=self.say_hi1)

        self.hi_there.pack(side=LEFT)

        self.entry = Entry(frame, fg="green")

        self.contents.set(connessionemy.keys()[:4] )

        self.entry["textvariable"] = self.contents

        self.entry.pack(side=LEFT)

        self.hi_there2 = Button(frame, text="Data nascita", command=self.say_hi2)

        self.hi_there2.pack(side=LEFT)

        self.entry2 = Entry(frame, fg="blue")

        self.contents.set(connessionemy.keys()[:3] )

        self.entry2["textvariable"] = self.content

        self.entry2.pack(side=LEFT)

        self.hi_there3 = Button(frame, text="Luogo nascita", command=self.say_hi3)

        self.hi_there3.pack(side=LEFT)

        self.entry3 = Entry(frame,  fg="pink")

        self.contents.set(connessionemy.keys()[:2] )

        self.entry3["textvariable"] = self.contents

        self.entry3.pack(side=LEFT)

        self.hi_there4 = Button(frame, text="CAP", command=self.say_hi4)

        self.hi_there4.pack(side=LEFT)

        ##root['ACHILLE']=AchillePaoloni()

        self.entry4 = Entry(frame,fg="red")

        self.contents.set(connessionemy.keys()[:2] )

        self.entry4.pack()

        self.entry4["textvariable"] = self.contents

        self.entry4.pack(side=LEFT)

       

       

    def say_hi1(self):

        connessionemy['PaoloniAchilleRec1'] = AchillePaoloni()

        self.contents.set(connessionemy.keys()[1] )

        self.entry["textvariable"] = self.contents

        self.entry.pack(side=LEFT)

        ##print "hi there, everyone1!"

    def say_hi2(self):

        connessionemy['PaoloniAchilleRec2'] = AchillePaoloni()

        self.contents.set(connessionemy.keys()[2] )

        self.entry2["textvariable"] = self.contents

        self.entry2.pack(side=LEFT)

        ##print "hi there, everyone2!"

    def say_hi3(self):

        connessionemy['PaoloniAchilleRec3'] = AchillePaoloni()

        self.contents.set(connessionemy.keys()[3] )

        self.entry["textvariable"] = self.contents

        self.entry.pack(side=LEFT)

        ##print "hi there, everyone3!"

    def say_hi4(self):

        connessionemy['PaoloniAchilleRec4'] = AchillePaoloni()

        self.contents.set(connessionemy.keys()[4] )

        self.entry2["textvariable"] = self.contents

        self.entry2.pack(side=LEFT)

root = Tk()

app = App(root)

root.mainloop()
