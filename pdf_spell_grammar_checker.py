import PyPDF2
import enchant
import language_check
tool = language_check.LanguageTool('en-US')
d =     enchant.Dict("en_US")
pdfFileObj = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
print(text)
for i in text.split():
    # print(i)
    d.check(i)
    if(d.check(i)== False):
        print('Please look for the suspected word ie %s and below suggestions'% i)
        print(d.suggest(i))
matches = tool.check(text)
# print((matches))
print('Starting with grammar check...')
print('The suggested sentence is:-')
print(language_check.correct(text, matches))

