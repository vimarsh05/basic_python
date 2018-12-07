import pyqrcode
import png

text='smeet'

try:
    url=pyqrcode.create(text)
    url.png('smeet.png')
    print('your png is generated')

except Exception as e:
    print(e)