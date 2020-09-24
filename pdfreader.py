import os
import pyttsx3
import PyPDF2

book = open(input("enter file name with extension: "),'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("total pages: ",pages)
for num in range(5,pages):
    page = pdfReader.getPage(int(input("enter from which page you want to listen: ")))
    text = page.extractText()
    pyttsx3.speak(text)
