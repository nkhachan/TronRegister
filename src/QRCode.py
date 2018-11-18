import pyqrcode

def createQR():
    qr = pyqrcode.create('Unladden swallow')
    print(qr.text())