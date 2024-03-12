from time import time
from printable import Printable


class Block(Printable):
    def __init__(self, index, previou_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previou_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof

    def __repr__(self):
        return 'Index: {}, Previous Hash: {}, Proof: {}'.format(
            self.index, self.previous_hash, self.proof)
