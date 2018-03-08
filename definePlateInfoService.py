#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


class InfoService:
    def __init__(self, root):
        self.root = root
        self.i = 0  # row

        # subproduct components
        self.subproductRBVar = IntVar()
        self.subproductEntryVar = StringVar()
        self.subproductEntry = Entry(self.root, bd=1, width=25, textvariable=self.subproductEntryVar)
        self.subproductDic = {}

        # sheet components
        # variable contains number of sheets to produce (rows in the table)
        self.selectedSheetAmountVar = IntVar()
        self.checkButtonVarList = []
        self.colorEntryVarList = []
        # list beneath contains numbers of specific sheets that need to be printed again
        # they need to be an individual user input because otherwise it would start counting at 1
        self.sheetNumberVarList = []

    def createSubproductComponent(self, options, i):
        ''' creates Radiobuttons to choose the subproduct. Options given by list 'option' '''
        self.i = i
        Label(self.root, text="Teilprodukt:", font=("Helvetica 15 bold"), fg="darkgray").grid(row=self.i, column=0,
                                                                                              pady=10, padx=20,
                                                                                              sticky=W)
        for opt, val in options:
            Radiobutton(self.root, text=opt, variable=self.subproductRBVar, value=val).grid(row=self.i, column=1,
                                                                                            pady=10, padx=0, sticky=W)
            self.subproductDic[val] = opt

            self.i += 1

        Label(self.root, text="oder:", font=("Helvetica 15")).grid(row=self.i, column=1, pady=10, padx=0, sticky=W)
        self.subproductEntry.grid(row=self.i, column=1, pady=10, padx=40, sticky=W)
        self.i += 1

    def createSheetAmountOptionButton(self, sheetRange, i, createPDFButton):
        ''' creates dropdown menu to select the amount of labels needed '''
        self.i = i
        Label(self.root, text="Anzahl Bögen:", font=("Helvetica 15 bold"), fg="darkgray").grid(row=self.i, column=0,
                                                                                               pady=10,
                                                                                               padx=20, sticky=W)
        # default is at least one label to print
        self.selectedSheetAmountVar.set(1)

        # sheetRange = max amount of sheets to choose
        choices = list(range(1, sheetRange))
        option = OptionMenu(self.root, self.selectedSheetAmountVar, *choices)
        option.grid(row=self.i, column=1, pady=10, padx=0, sticky=W)

        # choose selected amount of sheets
        sheetButton = Button(self.root, text="ok",
                             command=lambda: self.addSheetTable(self.selectedSheetAmountVar.get(), self.i + 1,
                                                                createPDFButton, sheetButton))
        sheetButton.grid(row=self.i, column=1, pady=10, padx=80, sticky=NW)
        self.i += 1

    def addSheetTable(self, amount, i, createPDFButton, sheetButton):
        ''' creates sheet table '''

        self.i = i

        for row in range(amount + 1):
            for col in range(4):

                if col == 0:
                    if row == 0:
                        Label(self.root, text="B - Anz. Farben", font=("Helvetica 15")).grid(row=self.i, column=1,
                                                                                             pady=5,
                                                                                             padx=20,
                                                                                             sticky=NW)
                        Label(self.root, text="S - Anz. Farben", font=("Helvetica 15")).grid(row=self.i, column=2,
                                                                                             pady=5,
                                                                                             padx=20,
                                                                                             sticky=NW)
                        Label(self.root, text="W - Anz. Farben", font=("Helvetica 15")).grid(row=self.i, column=3,
                                                                                             pady=5,
                                                                                             padx=20,
                                                                                             sticky=NW)
                        Label(self.root, text="Bogenzahl (nur relevant \n bei Nachdruck)", font=("Helvetica 15")).grid(
                            row=self.i, column=4,
                            pady=5,
                            padx=20,
                            sticky=NW)
                    else:
                        Label(self.root, text=row, font=("Helvetica 15")).grid(row=self.i, column=col, pady=5, padx=20,
                                                                               sticky=NW)
                else:
                    if row != 0:
                        checkButtonVar = IntVar()
                        colorEntryVar = StringVar()

                        self.checkButtonVarList.append(checkButtonVar)
                        self.colorEntryVarList.append(colorEntryVar)

                        Checkbutton(self.root, variable=checkButtonVar).grid(row=self.i, column=col, pady=5, padx=20,
                                                                             sticky=NW)
                        Entry(self.root, bd=1, width=9, textvariable=colorEntryVar).grid(row=self.i, column=col, pady=5,
                                                                                         padx=40, sticky=NW)

            if row != 0:
                sheetNumberVar = StringVar()
                self.sheetNumberVarList.append(sheetNumberVar)
                Entry(self.root, bd=1, width=4, textvariable=sheetNumberVar).grid(row=self.i, column=4, pady=5,

                                                                                  padx=20, sticky=NW)

            self.i += 1
        # after creating the table you are able to generate a pdf
        createPDFButton.config(state=NORMAL)
        # disable sheet button to not print another sheet table
        sheetButton.config(state=DISABLED)
