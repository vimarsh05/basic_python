import pyqrcode
import png

text='sapna'

try:
    url=pyqrcode.create(text)
    url.png('sapna.png')
    print('your png is generated')

except Exception as e:
    print(e)
