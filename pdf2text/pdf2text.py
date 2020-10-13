import PyPDF2

filename = r"C:\Yahia\HDB\DTS\2- Projects\VASCO\3- Execution - VASCO\Fraud- RA\Analysis sessions\OneSpan CBE Regulation Internet Banking.pdf"

pdf = PyPDF2.PdfFileReader(open(filename, "rb"))
# for page in pdf.pages:
#     print (page, page.extractText())

# print (pdf.getDocumentInfo())
# print (pdf.getNamedDestinations())
# print ("# of pages:", pdf.getNumPages())
# print ("page Layout:", pdf.pageLayout(pdf.getPage(1)))

page = pdf.getPage(1)
print (page)
#print (page.extractText())

#txt = page.extractText()
#print (type(txt))
# for i, t in enumerate(txt):
#     print (i, ":", t)

#print (txt)

# page_1 = pdf.getPage(1)
# print (page_1)
# for x,y in page_1.items():
#     print (x, ":", type(x), y, ":", type(y))
#     if type(x) == dict:
#         for k,v in x.items():
#             print (k, ": ", v)

#print (page1.extractText())