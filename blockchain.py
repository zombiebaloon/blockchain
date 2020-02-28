class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_transaction(self, sender, recipient, amount):
        pass


    def new_block(self, proof, previous_block = None):
        pass

    @property  #we don"t have to use () this in function calling cause we are not passing parameters while calling function
    def last_block(self):
        return self.chain[-1]


    @staticmethod  #inbuild maths calculation function used to calcuclate hash here
    def hash(block):
        pass

    @staticmethod
    def varify_block(blobk):
        pass