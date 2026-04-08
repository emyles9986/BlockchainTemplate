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

        amtStr = str(amt)
        txn = fromAdd+"."+toAdd+"."+amtStr
        
        self.mempool.append(txn)

    def purgeMempool(self, block):
        '''
        You may not need this, but once a block has been mined, you should remove all transactions
        in the block from the mempool.
        '''
        self.mempool=[]

    def recieveBlock(self, block: Block):
        '''
        The goal here is to verify that the block that this node recieved adheres to 
        the rules of the blockchain (i.e correctly calcukated nonce, right reward, etc.)
        '''
        
        #declare previousBlock and set it to the last block in the chain
        previousBlock = self.chain[-1]
        
        #check the hash has the correct number of leading zeros
        for i in range(difficulty):
            if block.hash[i] != 0:
                return -1
            
        #check that the nonse gets the hash, previousBlock is the last block in the chain, 
        #block.index is the next index, and block.timestamp comes after previousblock.timestamp
        if (block.hash != block.calculateHash()) or (previousBlock.hash != block.previousHash) \
            or (previousBlock.index != (block.index - 1)) or (previousBlock.timestamp >= block.timestamp):
            return -1
        

        #add the block to the chain
        self.chain.append(block)
        self.purgeMempool
        return 0


    def mine(self):
        if len(self.mempool) >= 10:
            print(f"Starting mining process on {self.name}")

            #declare previousBlock and set it to the last block in the chain
            previousBlock = self.chain[-1]

            newBlock = Block(previousBlock.index + 1, self.mempool, previousBlock.hash) #create a new block
            validHash = False #declare a validHash flag and set it to false
            
            #try out nonces until it gives a hash with (difficulty) leading zeros
            while validHash == False:           
                validHash = True               
                for i in range(difficulty):    
                    if newBlock.hash[i] != 0:
                        validHash = False
                        newBlock.nonce = random.randint(0,9223372036854775807)
                        newBlock.hash = newBlock.calculateHash() 
                        break
                
            #have each peer validate and add the block to their chain
            for i in self.peers:
                i.recieveBlock(newBlock)
            #validate and add the block to the chain
            self.recieveBlock(newBlock)