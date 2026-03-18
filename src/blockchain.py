from lib.block import Block

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
        txn = fromAdd+toAdd+amt
        
        self.mempool.append(txn)

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

            #create a new block, figure out the nonce and transmit it.
            
            for i in self.peers:
                i.recieveBlock(newBlock)