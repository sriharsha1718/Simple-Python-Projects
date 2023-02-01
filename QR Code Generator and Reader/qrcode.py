import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Hello Everyone!")
qr.png("MyQRCode.png", scale=8)

d = decode(Image.open("MyQRCode.png"))
print(d[0].data.decode("ascii"))