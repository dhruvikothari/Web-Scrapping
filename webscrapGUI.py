import requests
import html5lib
import bs4
import sys
from tkinter import *

win = Tk()

def scrappin():
    url = requests.get(URL.get())
    res = bs4.BeautifulSoup(url.txt, "html.parser")
    saveFile1 = open("WEB_TEXT.txt", "a")
    for i in res.select('p'):
        saveFile1.write(i.getText())
    saveFile1.close()
    saveFile2 = open("WEB_CODE.txt", "a")
    for i in res.select('p'):
        saveFile2.write(res.prettify())
    saveFile2.close()


# ********************************************************************************************************
var = StringVar()
var.set("Website scrapper tool")
LABEL_OF_WEB = Label(win, textvariable=var, bd=8, bg="#FAAFBA", font=("Helvetica, 35")).grid(row=0, column=0)
URL = StringVar()
E1 = Entry(win, bd=5, font=7, textvariable=URL).grid(row=1, column=0, ipadx=100)
button = Button(win, text="Scrap it!", bd=5, command=scrappin).grid(row=2, column=0, padx=8, pady=4)
# ********************************************************************************************************

win.mainloop()
