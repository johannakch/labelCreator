#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog

SEARCH_DIR = "/Schreibtisch/CIP3Files/"


class FileService:
    """ class to open a CIP3 file and read attribute values """

    def __init__(self, root):

        self.root = root
        self.i = 0

        self.companyNameLabel = Label(self.root, text="Koch. Prepress Print Media GmbH", font=("Helvetica", 15))

        # file components
        self.cip3AdmCustomerLabel = Label(self.root)
        self.cip3AdmJobCodeLabel = Label(self.root)
        self.cip3AdmJobNameLabel = Label(self.root)

        self.customerEntryVar = StringVar()
        self.cip3AdmCustomerEntry = Entry(self.root, bd=1, width=25, textvariable=self.customerEntryVar)
        self.saveButton = Button(self.root)
        self.editButton = Button(self.root)

    def getFileName(self):
        ''' returns the path of the chosen CIP3 file of the search dialog '''
        # TODO: Im Folgenden muss das Suchverzeichnis (SEARCH_DIR) auf die Umgebung des Zielrechners angepasst werden
        # creates attribute 'filename' with path to the selected file
        filename = filedialog.askopenfilename(initialdir=SEARCH_DIR, title="Datei auswählen")
        print("Filename:", filename)
        return filename

    def readAttrValues(self, filename, i):
        ''' opens CIP3 file and reads the important values from the file,
            also creates the specific labels '''
        self.i = i
        cip3AdmCustomer = ""
        cip3AdmJobCode = ""
        cip3AdmJobName = ""
        fileContent = open(filename, "rb").readlines()
        for e in fileContent:
            if "/CIP3AdmCustomer".encode('utf-8') in e:
                cip3AdmCustomer = e.decode('utf-8')
            elif "/CIP3AdmJobCode".encode('utf-8') in e:
                cip3AdmJobCode = e.decode('utf-8')
            elif "/CIP3AdmJobName".encode('utf-8') in e:
                cip3AdmJobName = e.decode('utf-8')

        print(self.splitAttrString(cip3AdmCustomer, "(", ")"))
        print(self.splitAttrString(cip3AdmJobName, "(", ")"))
        print(self.splitAttrString(cip3AdmJobCode, "(", ")"))

        self.companyNameLabel.grid(row=self.i, column=0, pady=10, padx=20, sticky=W)
        self.i += 1

        Label(self.root, text="Kunde:", font=("Helvetica 15 bold"), fg="darkgray").grid(row=self.i, column=0, pady=10,
                                                                                        padx=20,
                                                                                        sticky=W)
        # decides wether the customer name is given or not. If not an Entry will be created to get an user input
        # which will be saved as the customer name that can be edited as well
        if cip3AdmCustomer != "":
            self.cip3AdmCustomerLabel.config(text=self.splitAttrString(cip3AdmCustomer, "(", ")"),
                                             font=("Helvetica", 21))
            self.cip3AdmCustomerLabel.grid(row=self.i, column=1, pady=10, padx=0, sticky=W)
        else:
            currentRow = self.i
            self.cip3AdmCustomerEntry.grid(row=self.i, column=1, pady=10, padx=0, sticky=W)
            self.saveButton.config(text="speichern", command=lambda: self.saveCustomerEntry(currentRow))
            self.editButton.config(text="bearbeiten", state=DISABLED)
            self.i += 1
            self.saveButton.grid(row=self.i, column=1, pady=10, padx=0, sticky=NW)
            self.editButton.grid(row=self.i, column=1, pady=10, padx=95, sticky=NW)
        self.i += 1

        Label(self.root, text="Auftragsnr.:", font=("Helvetica 15 bold"), fg="darkgray").grid(row=self.i, column=0,
                                                                                              pady=10,
                                                                                              padx=20, sticky=W)
        self.cip3AdmJobCodeLabel.config(text=self.splitAttrString(cip3AdmJobCode, "(", ")"), font=("Helvetica", 15))
        self.cip3AdmJobCodeLabel.grid(row=self.i, column=1, pady=10, padx=0, sticky=W)
        self.i += 1

        Label(self.root, text="Auftrags-Name:", font=("Helvetica 15 bold"), fg="darkgray").grid(row=self.i, column=0,
                                                                                                pady=10,
                                                                                                padx=20, sticky=W)
        self.cip3AdmJobNameLabel.config(text=self.splitAttrString(cip3AdmJobName, "(", ")"), font=("Helvetica", 15))
        self.cip3AdmJobNameLabel.grid(row=self.i, column=1, pady=10, padx=0, sticky=W)
        self.i += 1

    @staticmethod
    def splitAttrString(s, delim1, delim2):
        ''' cuts out the value from a given string s between index of delim1 and index of delim2'''
        if s:
            return s[s.index(delim1) + len(delim1): s.index(delim2)]
        else:
            return s

    def saveCustomerEntry(self, i):
        ''' saves user input of the customer name entry and turns the entry with the value into a label'''
        print(self.customerEntryVar.get())
        self.cip3AdmCustomerEntry.destroy()
        self.saveButton.config(state=DISABLED)
        self.cip3AdmCustomerLabel.config(text=self.customerEntryVar.get(), font=("Helvetica", 21))
        self.cip3AdmCustomerLabel.grid(row=i, column=1, pady=10, padx=0, sticky=W)
        self.editButton.config(state=NORMAL, command=lambda: self.editCustomerEntry(i))

    def editCustomerEntry(self, row):
        ''' changes the customer name label to an entry again to edit the customer name '''
        self.cip3AdmCustomerEntry = Entry(self.root, bd=1, width=25, textvariable=self.customerEntryVar)
        self.cip3AdmCustomerEntry.grid(row=row, column=1, pady=10, padx=0, sticky=W)
        self.saveButton.config(state=NORMAL)
