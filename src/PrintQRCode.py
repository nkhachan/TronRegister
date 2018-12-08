from Adafruit_Thermal import *
import sys
import serial


printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)



from qr import *
printer.printBitmap(width, height, data)