# from PIL import Image
#
# try:
#     file='robot.jpg'
#     im=Image.open(file)
#     new_file='robot1.pdf'
#     print('your pdf is generated')
#     im.save(new_file,resolution=10.0)
#
# except Exception as e:
#     print(e)

import img2pdf
file='robot.jpg'
with open('robot.pdf','wb') as f:
    f.write(img2pdf.convert(file))
    print('your pdf is generated')
