import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

<<<<<<< HEAD
def pdfparser(filename):

    fp = open(filename, 'rb')
=======
def pdfparser(data):

    fp = open(data, 'rb')
>>>>>>> 6d491bc042e86688b60a965fcdaf4c69a46b249b
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    #device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    print(data)

if __name__ == '__main__':
    #pdfparser(r"C:\Users\yahia\Downloads\41832448_AI-bot-for-Trading.pdf")
<<<<<<< HEAD
    # pdfparser(r"C:\Yahia\HDB\DTS\2- Projects\VASCO\3- Execution - VASCO\Fraud- RA\Analysis sessions\OneSpan CBE Regulation Internet Banking.pdf")
    pdfparser(r"C:\Users\yahia\Downloads\Assgn3-LinkedListsArray (1).pdf")
=======
    pdfparser(r"C:\Yahia\HDB\DTS\2- Projects\VASCO\3- Execution - VASCO\Fraud- RA\Analysis sessions\OneSpan CBE Regulation Internet Banking.pdf")
>>>>>>> 6d491bc042e86688b60a965fcdaf4c69a46b249b
