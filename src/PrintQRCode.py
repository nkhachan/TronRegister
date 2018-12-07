from Adafruit_Thermal import *
import serial

printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)

printer.doubleHeightOn()
printer.println("Double Height ON")
from logo import *

printer.printBitmap(width, height, data)