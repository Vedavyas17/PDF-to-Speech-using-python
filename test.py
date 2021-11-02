import os
#
import PyPDF2
from gtts import gTTS

# OPENING SAMPLE.PDF FILE IN BINARY MODE
file = open("sample.pdf", "rb")
#
# CREATING AN OBJECT TO PDFFILEREADER CLASS AND PASS THE PDF FILE AND GET PDF
pdfReader = PyPDF2.PdfFileReader(file)
#
text1 = ""
# 
for pageNum in range(pdfReader.numPages):
     # GETPAGE() WILL TAKE PAGE NUM AS ARGUMENT
     page = pdfReader.getPage(pageNum)
     # print(text1)
     text1 += page.extractText() #EXTRACTING TEXT FROM PDF
#
 file.close() # FINALLY CLOSSING PDF FILE.
 print(text1)

# LISTENING USING GOOGLE API (GOOGLE TEXT TO SPEECH)

 op = gTTS(text = text1, lang='en')
 op.save("ex.mp3")

# READING .TXT FILE AND LISTENING FROM GTTS API

fh = open("test.txt","r")
myText = fh.read()
lan = 'en'

# GTTS WORKS OFFLINE AS WELL
output = gTTS(text=myText, lang=lan, slow=False)
output.save("audio.mp3")

#
fh.close()
os.system("start audio.mp3")
