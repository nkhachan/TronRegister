from TronAPI import *
from Binance import *

def main():
    address = 'TMZtJCtmk7ykoCFn5WTSKbedgv8xFuucfz';
    print(gettransactions(address))

if __name__ == "__main__":
    main()