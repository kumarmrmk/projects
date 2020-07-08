import pyqrcode
import png
from pyqrcode import QRCode
s = input("enter website name: ")
url = pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png("myqrcode.png",scale=6)
print(url)
