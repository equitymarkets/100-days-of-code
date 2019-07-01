#Day 73

import hashlib

block  = []
blockchain = []
counter = 0



# ~ def add_value(transaction_amount, last_transaction=[1]):
    # ~ blockchain.append([last_transaction,transaction_amount])

def trade_input():                              
    trade = input("What are you trading? ")
    tradehash = hashlib.sha256(trade.encode('ascii')).hexdigest()
    block.append(tradehash)

def num_trade_input():
    amount = input('How many? ')
    amthash = hashlib.sha256(amount.encode('ascii')).hexdigest()
    block.append(amthash)

def recd_input():
    recd = input("What are you receiving? ")    
    recdhash = hashlib.sha256(recd.encode('ascii')).hexdigest()
    block.append(recdhash) 

def num_recd_input():
    amount = input("How many? ")
    amthash = hashlib.sha256(amount.encode('ascii')).hexdigest()
    block.append(amthash)

# ~ def current_blockchain_value():
    # ~ blockchain.append(block)


    
trade_input()
num_trade_input()
recd_input()
num_recd_input()
print(block)
    
 


# ~ item = user_input()
# ~ amount = user_input()
# ~ add_value()

# ~ tx_amount = user_input()
# ~ add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

# ~ tx_amount = user_input()
# ~ add_value(tx_amount, get_last_blockchain_value())
   
# ~ add_value(2)
# ~ add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9)
# ~ add_value(10.89, get_last_blockchain_value())

# ~ print(blockchain)
