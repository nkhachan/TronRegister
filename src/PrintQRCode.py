from Bill import bill
from CoinMarketCap import *

from Adafruit_Thermal import *
import serial

def printOutFinalBill():
    printer = Adafruit_Thermal("/dev/ttyUSB0", 9600, timeout=3000)

    printer.doubleHeightOn()
    printer.println("Double Height ON")