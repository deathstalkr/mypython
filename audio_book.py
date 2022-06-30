import pyttsx3
import PyPDF2
book = open('Click_Millionaires_-_Scott_Fox.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(book)
pages = pdf.numPages
print(pages)
speak = pyttsx3.init()
for num in range(8, pages):
    page = pdf.getPage(num)
    text = page.extractText()
    speak.say(text)
    speak.runAndWait()
