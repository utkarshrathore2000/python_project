import qrcode
qr=qrcode.QRCode(version=1,box_size=10,border=5)
data='https://github.com/utkarshrathore2000/python_project/upload/master'
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('github.png')
