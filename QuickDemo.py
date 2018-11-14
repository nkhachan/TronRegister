'''

    Quick Demo for Class

        This allows you to get updates to your wallet and check your balance

'''


from TronAPI import *

def quickDemo():
    address = input("Please enter your public address  \n")

    transactions = []

    balance = str(getbalance(address))
    print("Your current balance is : ", str(formatBalance(balance)), "TRX", "\n")

    print ("Your most recent transactions are the following \n ")

    for transaction in gettransactionobjects(address):
        transactions.append(transaction)
        print(transaction)

    while(1):
        if (len(gettransactionobjects(address)) == len(transactions)):
            pass
        else :
            lastTransaction = getlasttransactionobject(address)
            print(lastTransaction)
            transactions.append(lastTransaction)



