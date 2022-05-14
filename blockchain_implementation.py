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
  
# Creating a new JSON object block listing key-value pairs. 
# Pending transactions list Rest and the new box to the blockchain append
    def newBlock(self, the_proof, previousHash = None):  
        new_box = {  
            'index': len(self.chain) + 1,  
            'proof': the_proof,  
            'timestamp': time(),  
            'previous_hash_func': previousHash or self.hash(self.chain[-1]),  
            'transactions': self.pendingTransactions,  
        }  
        self.pendingTransactions = []  
        self.chain.append(new_box)  
  
        return new_box  
  
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
  
# receiving one box. Turning it into a string Unicode (for hashing). Hashing with SHA256 encryption,  
# then translating the Unicode into a string(hexadecimal).  
    def hash(self, block):  
        stringObject = json.dumps(block, sort_keys = True)  
        blockString = stringObject.encode()  
  
        raw_Hashing = hashlib.sha256(blockString)  
        hex_Hashing = raw_Hashing.hexdigest()  
  
        return hex_Hashing
  
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
