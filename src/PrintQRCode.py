from Adafruit_Thermal import *
import serial

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("TMZtJCtmk7ykoCFn5WTSKbedgv8xFuucfz")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)

printer.doubleHeightOn()
printer.println("Double Height ON")
from qr import *
printer.printBitmap(width, height, data)