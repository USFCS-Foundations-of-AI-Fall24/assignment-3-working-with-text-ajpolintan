## A representation of a document as a set of tokens.

from collections import defaultdict
from math import sqrt

class Document :
    def __init__(self, true_class=None):
        self.true_class = true_class
        self.tokens = defaultdict(lambda:0)

    def add_tokens(self, token_list) :
        for item in token_list :
            self.tokens[item] = self.tokens[item] + 1

    def __repr__(self):
        return f"{self.true_class} {self.tokens}"


# return the distance between two documents
def euclidean_distance(d1, d2) :
    # take the union of the tokens in each document
    union = d1.tokens.keys() | d2.tokens.keys()
    print(union)
    dist = sum([(d1.tokens[item] - d2.tokens[item])**2 for item in union])
    return dist

## You implement this.
def cosine_similarity(d1,d2) :
    union = d1.tokens.keys() | d2.tokens.keys()
    num = sum([d1.tokens[item] * d2.tokens[item] for item in union])
    dm =  sqrt(sum([d1.tokens[item]**2 for item in d1.tokens.keys()])) * sqrt(sum([d2.tokens[item]**2 for item in d2.tokens.keys()]))
    
    #calculate cosine
    cos = num / dm

    print(num)
    print("COS:" + str(cos))
    return cos
  
   

