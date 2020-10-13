import PyPDF2

filename = r"C:\Yahia\HDB\DTS\2- Projects\VASCO\3- Execution - VASCO\Fraud- RA\Analysis sessions\OneSpan CBE Regulation Internet Banking.pdf"

pdf = PyPDF2.PdfFileReader(open(filename, "rb"))
for page in pdf.pages:
    print (page.extractText())

# page1 = pdf.getPage(0)
# print (page1)
# for x in page1:
#      print (x)
#
# print (page1.extractText())