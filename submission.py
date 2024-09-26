from Document import *
from Cluster import *
if __name__ == '__main__' :
    d = Document(true_class='pos')
    d.add_tokens(['cat','cat','dog', 'fish','jungkook', "woooooooof"])
    d2 = Document(true_class='pos')
    d2.add_tokens(['cat', 'fish'])
    d3 = Document(true_class='pos')
    d3.add_tokens(['cat', 'dog', 'fish', "swish"])

    c = []
    c.append(d)
    c.append(d2)
    c.append(d3)

    cluster = Cluster(members=c)
    cluster.calculate_centroid()
    print(cluster)

    distance = euclidean_distance(d, d2)
    dii = cosine_similarity(d2, d)
    print("HELLO" + str(dii))
