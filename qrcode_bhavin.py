import pyqrcode
import png

text='bhavin'

try:
    url=pyqrcode.create(text)
    url.png('bhavin.png')
    print('your png is generated')

except Exception as e:
    print(e)