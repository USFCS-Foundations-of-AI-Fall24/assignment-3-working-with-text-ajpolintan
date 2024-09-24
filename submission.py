from Document import *

if __name__ == '__main__' :
    d = Document(true_class='pos')
    d.add_tokens(['cat', 'dog', 'fish'])
    d2 = Document(true_class='pos')
    d2.add_tokens(['cat', 'dog', 'fish'])

    distance = euclidean_distance(d, d2)
    dii = cosine_similarity(d, d2)
    print("HELLO" + str(dii))
