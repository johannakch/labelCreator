#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from cip3FileService import FileService
from definePlateInfoService import InfoService
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
import os


class InfoLabel:
    def __init__(self, root, options, sheetRange, row=0):
        # root widget
        self.root = root
        # current row
        self.i = row
        # options for subproduct (Teilprodukt)
        self.options = options
        # max. number of sheets/labels
        self.sheetRange = sheetRange

        # components to search for cip3 file
        self.searchCIP3FileLabel = Label(self.root, text="Datei auswählen:")
        self.searchCIP3FileButton = Button(self.root, text="suchen")
        # button to create PDF file
        self.createPDFButton = Button(self.root, text="PDF", state=DISABLED)
        # button to clear the whole root widget and start again with the search dialog
        self.clearButton = Button(self.root, text="clear")

    def generateInfoLabel(self):
        ''' creates step by step the components:
             - read values from the CIP3 file
             - create Radiobuttons to choose the subproduct
             - create dropdown to select the amount of labels '''

        # File Service object
        fs = FileService(self.root)
        # gets the chosen file from the search dialog
        filename = fs.getFileName()
        fs.readAttrValues(filename, self.i)

        # deletes the label and the button that opens the search dialog
        self.searchCIP3FileButton.destroy()
        self.searchCIP3FileLabel.destroy()

        self.i = fs.i

        self.clearButton.config(command=self.clearWindow)
        self.clearButton.grid(row=0, column=0, pady=10, padx=20, sticky=NW)
        self.createPDFButton.grid(row=2, column=2, pady=10, padx=0, sticky=NW)

        # Info Service object
        inf = InfoService(self.root)
        # creates radiobuttons for subproduct
        inf.createSubproductComponent(self.options, self.i)
        self.i = inf.i
        # creates dropdown menu to choose amount of labels
        inf.createSheetAmountOptionButton(self.sheetRange, self.i, self.createPDFButton)
        # add function to the newly enabled button
        self.createPDFButton.config(command=lambda: self.createPDF(fs, inf))


    def createPDF(self, fs, inf):
        ''' generates one pdf file containing every label needed '''

        sheetAmount = inf.selectedSheetAmountVar.get()

        # possible sheet options with sheet number
        sheetOptions = {0: ["Bogen", 0], 1: ["Schön", 0], 2: ["Wider", 0]}

        # determines the type of the subproduct (either a value of the radiobuttons or the value of the entry)
        if inf.subproductRBVar.get() == 0:
            if inf.subproductEntryVar.get() == "":
                subproduct = "-"
            else:
                subproduct = inf.subproductEntryVar.get()
        else:
            if inf.subproductEntryVar.get() == "":
                subproduct = inf.subproductDic[inf.subproductRBVar.get()]
            else:
                subproduct = inf.subproductEntryVar.get()

        # setting the name of the pdf file
        pdfFileName = fs.cip3AdmJobCodeLabel['text'] + ".pdf"
        # print(pdfFileName)
        # generating the pdf file
        c = canvas.Canvas(pdfFileName, bottomup=0, pagesize=A5)

        index = 0
        color = "-"
        for e in range(0, sheetAmount):
            sheetNumber = inf.sheetNumberVarList[e].get()

            for sheetOption in range(0, len(sheetOptions)):
                if inf.checkButtonVarList[index].get() == 1:
                    opt = index % len(sheetOptions)
                    if inf.colorEntryVarList[index].get() != "":
                        color = inf.colorEntryVarList[index].get()

                    c.setFont("Helvetica", 11)
                    c.drawString(15, 340, fs.companyNameLabel['text'])
                    c.setFont("Helvetica", 18)
                    c.drawString(15, 365, fs.cip3AdmCustomerLabel['text'])
                    c.setFont("Helvetica", 11)
                    c.drawString(15, 410, "Auftrags-Nr.: ")
                    c.drawString(110, 410, fs.cip3AdmJobCodeLabel['text'])
                    c.drawString(15, 430, "Auftrags-Name: ")
                    c.drawString(110, 430, fs.cip3AdmJobNameLabel['text'])

                    c.drawString(15, 450, "Teilprodukt: ")
                    c.drawString(110, 450, subproduct)
                    c.drawString(15, 470, "Bogen: ")
                    if opt in range(0, 3):
                        if sheetNumber == "":
                            sheetOptions[opt][1] += 1
                            c.drawString(110, 470, sheetOptions[opt][0] + " " + str(sheetOptions[opt][1]))
                        else:
                            c.drawString(110, 470, sheetOptions[opt][0] + " " + sheetNumber)

                    else:
                        c.drawString(110, 470, "-")
                    c.drawString(15, 490, "Farben: ")
                    c.drawString(110, 490, color)
                    # to start a new page within a pdf file
                    c.showPage()

                index += 1

        c.save()

        # view created PDF document
        os.system('open ' + pdfFileName)
        self.createPDFButton.config(state=DISABLED)
        self.root.destroy()

    def clearWindow(self):
        ''' deletes all children from root and creates the search components to start all over again'''

        for widget in self.root.winfo_children():
            widget.destroy()

        infLabel = InfoLabel(self.root, self.options, self.sheetRange, 1)
        infLabel.searchCIP3FileLabel = Label(self.root, text="Datei auswählen:")
        infLabel.searchCIP3FileButton = Button(self.root, text="suchen")
        infLabel.searchCIP3FileLabel.grid(row=0, column=0, pady=10, padx=20, sticky=W)
        infLabel.searchCIP3FileButton.grid(row=0, column=0, pady=10, padx=140, sticky=W)
        infLabel.searchCIP3FileButton.config(command=lambda: infLabel.generateInfoLabel())
