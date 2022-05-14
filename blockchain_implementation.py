# importing the required libraries  
import hashlib  
import json  
from time import time  
  
# creating the Block_chain class  
class Blockchain(object):  
    def __init__(self):  
        self.chain = []  
        self.pendingTransactions = []  
  
        self.newBlock(previousHash = "Cryptography is typically bypassed, not penetrated.", the_proof = 100)  
  
# Creating a new block listing key/value pairs of  
# block information in a JSON object.  
# Reset the list of pending transactions &  
# append the newest block to the chain.  
    def newBlock(self, the_proof, previousHash = None):  
        block = {  
            'index': len(self.chain) + 1,  
            'timestamp': time(),  
            'transactions': self.pendingTransactions,  
            'proof': the_proof,  
            'previous_hash': previousHash or self.hash(self.chain[-1]),  
        }  
        self.pendingTransactions = []  
        self.chain.append(block)  
  
        return block  
  
#Searching the blockchain for the most recent block.  
    @property  
    def lastBlock(self):  
   
        return self.chain[-1]  
  
# Adding a transaction with relevant info to the 'blockpool' - list of pending tx's.   
    def newTransaction(self, the_sender, the_recipient, the_amount):  
        transaction = {  
            'sender': the_sender,  
            'recipient': the_recipient,  
            'amount': the_amount  
        }  
        self.pendingTransactions.append(transaction)  
        return self.lastBlock['index'] + 1  
  
# receiving one block. Turning it into a string, turning that into  
# Unicode (for hashing). Hashing with SHA256 encryption,  
# then translating the Unicode into a hexidecimal string.  
    def hash(self, block):  
        stringObject = json.dumps(block, sort_keys = True)  
        blockString = stringObject.encode()  
  
        rawHash = hashlib.sha256(blockString)  
        hexHash = rawHash.hexdigest()  
  
        return hexHash  
  
block_chain = Blockchain()  
trans1 = block_chain.newTransaction("Chirag", "Dhrumil", '15 BTC')  
trans2 = block_chain.newTransaction("Dhrumil", "Chirag", '2 BTC')  
trans3 = block_chain.newTransaction("Chirag", "Mohan", '15 BTC')  
block_chain.newBlock(10123)  
  
trans4 = block_chain.newTransaction("Dhrumil", "Fenil", '2 BTC')  
trans5 = block_chain.newTransaction("Fenil", "Meet", '5 BTC')  
trans6 = block_chain.newTransaction("Meet", "Dhrumil", '1 BTC')  
block_chain.newBlock(10384)  
  
print("Genesis block: ", block_chain.chain)  
