import pyqrcode
import png

text='mitva'

try:
    url=pyqrcode.create(text)
    url.png('mitva.png')
    print('your png is generated')

except Exception as e:
    print(e)