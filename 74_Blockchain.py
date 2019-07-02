#Day 74 - Understanding Blockchain - Credit goes to Siraj Raval for his youtube
#video "Simple Blockchain in 5 Minutes" at [https://www.youtube.com/watch?v=MViBvQXQ3mM]
#for the backbone of most of my uncommented code below, as well as a great explanation!
import datetime
import hashlib


# ~ block  = []
# ~ counter = 0
class Block:
    
    data = None
    next = None
    hash = None
    blockNum = 0
    nonce = 0
    prev_hash = 0x0
    time = datetime.datetime.now()
    
    def __init__(self, data):
        self.data = data
    
    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.prev_hash).encode('utf-8') +
        str(self.time).encode('utf-8') +
        str(self.blockNum).encode('utf-8')
        )
        return h.hexdigest()
        
    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nPrevious Hash: " + str(self.prev_hash) + "\nBlock No: " + str(self.blockNum) + "\nHashes: " + str(self.nonce) + "\n " #+ ""\nTime: " + str(self.time) 

class Blockchain:
    
    
    difficulty = 20
    maxi = 2**32
    target = 2 ** (256 - difficulty)
    
    block = Block("Genesis")
    
    head = block
    
    def add(self, block):
        block.prev_hash = self.block.hash()
        block.blockNum = self.block.blockNum + 1
        
        
        self.block.next = block
        self.block = self.block.next
    
    def mine(self, block):
        for n in range(self.maxi):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
                
blockchain = Blockchain()


for n in range(20):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
# ~ def add_value(transaction_amount, last_transaction=[1]):
    # ~ blockchain.append([last_transaction,transaction_amount])

# ~ def trade_input():                              
    # ~ trade = input("What are you trading? ")
    # ~ tradehash = hashlib.sha256(trade.encode('ascii')).hexdigest()
    # ~ block.append(tradehash)

# ~ def num_trade_input():
    # ~ amount = input('How many? ')
    # ~ amthash = hashlib.sha256(amount.encode('ascii')).hexdigest()
    # ~ block.append(amthash)

# ~ def recd_input():
    # ~ recd = input("What are you receiving? ")    
    # ~ recdhash = hashlib.sha256(recd.encode('ascii')).hexdigest()
    # ~ block.append(recdhash) 

# ~ def num_recd_input():
    # ~ amount = input("How many? ")
    # ~ amthash = hashlib.sha256(amount.encode('ascii')).hexdigest()
    # ~ block.append(amthash)

# ~ def current_blockchain_value():
    # ~ print(block[-1])
    # ~ return block[-1]
    
# ~ trade_input()
# ~ num_trade_input()
# ~ recd_input()
# ~ num_recd_input()
# ~ print(block)
    



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
