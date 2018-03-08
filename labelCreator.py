#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from infoLabel import InfoLabel


def main():
    # create root-widget
    root = Tk()
    root.title("Label Creator")

    # set up of the program window
    root.geometry("1200x1000")

    # setting the parameters
    # options for subproduct (Teilprodukt)
    options = [
        ("Umschlag", 1),
        ("Inhalt", 2)
    ]
    # sheet range = max. number of sheets/labels
    sheetRange = 21
    # row number for tkinter's grid system (to know in which row to start the content)
    row = 1
    # creating an Info Label object
    infLabel = InfoLabel(root, options, sheetRange, row)

    # start by showing the search dialog
    infLabel.searchCIP3FileLabel.grid(row=0, column=0, pady=10, padx=20, sticky=W)
    infLabel.searchCIP3FileButton.config(command=infLabel.generateInfoLabel)
    infLabel.searchCIP3FileButton.grid(row=0, column=0, pady=10, padx=140, sticky=W)

    mainloop()


if __name__ == "__main__":
    main()
