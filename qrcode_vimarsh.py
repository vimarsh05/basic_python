import pyqrcode
import png


text='vimarsh'
try:
    url=pyqrcode.create(text)
    url.png('C:/Users/Admin/Pictures/Saved Pictures/vimarsh.png')
    print('your png is created')

except Exception as e:
    print(e)


