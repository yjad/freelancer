import pdftotext
#from six.moves.urllib.request import urlopen
import io


filename = r"C:\Users\yahia\Downloads\41832448_AI-bot-for-Trading.pdf"

url = 'https://www.sec.gov/litigation/admin/2015/34-76574.pdf'
remote_file = urlopen(url).read()
memory_file = io.BytesIO(remote_file)

pdf = pdftotext.PDF(memory_file)

# Iterate over all the pages
for page in pdf:
    print(page)