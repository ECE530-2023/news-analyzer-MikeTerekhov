import PyPDF2
import io
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#implement this using google API
def secure_login(username, password):
    username_ = "Mike"
    password_ = 123
    if username == username_:
        if password == password_:
            return True
    return False
    # Errors 001, 002, 006

def uploader():
    # prompt user to select a PDF file
    Tk().withdraw()
    filename = askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    # read the PDF file
    with open(filename, "rb") as f:
        pdf = PyPDF2.PdfReader(f)
        # iterate over all pages of the PDF file
        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            # extract text from the page
            text = page.extractText()
            # split the text into words
            words = text.split()
            # print the words
            for word in words:
                print(word)
    

#currently this function is not needed because uploader() doesnt allow selection
#of anything that is not PDF format
def checker(file_name):
    if file_name.endswith('.txt'):
        print('valid')
        return True
    if file_name.endswith('.test'):
        print('valid')
        return True
    else:
        print( "Error related to uploader")
        return False
    # Error 001

uploader()
