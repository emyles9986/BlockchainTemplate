from lib.block import Block
import random

#PARAMS
difficulty = 3
reward = 10

class BlockChainClient:
    def __init__(self, n: str):
        self.name = n #eventually we'll add public and private keys but for now we work in plaintext
        self.peers = []
        self.mempool = [] #kinda lika a staging area for transactions before they are consolidated into a block
        self.chain = [Block(0, ["Genesis"], "0")]
    
    def transmitTxn(self, fromAdd, toAdd, amt):
        '''
        this function should create a transaction (you can do this in plaintext for now)
        and append it to your mempool and also 'transmit' it to everyone elses mempool.
        '''

        pass

    def purgeMempool(self, block):
        '''
        You may not need this, but once a block has been mined, you should remove all transactions
        in the block from the mempool.
        '''

        pass

    def recieveBlock(self, block: Block):
        '''
        The goal here is to verify that the block that this node recieved adheres to 
        the rules of the blockchain (i.e correctly calcukated nonce, right reward, etc.)
        '''

        pass

    def mine(self):
        if len(self.mempool) >= 10:
            print(f"Starting mining process on {self.name}")

            #create a new block, look at the first (difficulty) characters, 
            # if they aren't all zeros generate a new nonce and check again
            # transmit it.

            newBlock = Block() #create a new block
            validHash = False #declare a validHash flag and set it to false
            while validHash == False: #loop until we get a valid hash
                validHash = True #set validHash to true for now
                for i in range(difficulty): #look at the first (difficulty) characters in the hash
                    if newBlock.hash[i] != 0: #if any of them aren't 0
                        validHash = False #since hash is invalid, set validHash to False
                        newBlock.nonce = random.randint(0,9223372036854775807) #generate a new nonse from 0 to int limit
                        newBlock.calculateHash() #recalculate hash
                        break #break since hash has changed
                

            for i in self.peers:
                i.recieveBlock(newBlock)