import pyqrcode
import svg


text='vimarsh'

try:
    url=pyqrcode.create(text)
    url.svg('vimarsh.svg')
    print('your svg is generated')

except Exception as e:
    print(e)
