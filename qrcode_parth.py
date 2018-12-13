import pyqrcode
import png

text='parth.png'

try:
    url=pyqrcode.create(text)
    url.png('parth.png')
    print('your png is generated')

except Exception as e:
    print(e)