import random
from Document import *
from Classifier import *

class Cluster :
    ## a cluster is a group of documents
    def __init__(self, centroid=None, members=None):
        if centroid :
            self.centroid = centroid
        else :
            self.centroid = Document(true_class='pos')
        if members :
            self.members = members
        else :
            self.members = []

    def __repr__(self):
        return f"{self.centroid} {len(self.members)}"

    ## You do this.
    def calculate_centroid(self):
        ##creates new document
        num_documents = len(self.members)
        print("HIIII")
        union = []
        

        #find all the unique keys
        for d in self.members :
            if len(union) == 0 :
                union = d.tokens.keys() 
            else : 
                union = union | d.tokens.keys()

        for item in union :
            #m is a document
            for m in self.members :
                #reset the counts
                self.centroid.tokens[item] = 0
    
       # print(union)
        for item in union :
            #m is a document
            for m in self.members :
                self.centroid.tokens[item] += m.tokens[item] 
            self.centroid.tokens[item] = self.centroid.tokens[item] / num_documents
        
        print(f"{self.centroid} {len(self.members)}")
        #add the tokens to the centroid
        return self.centroid


def similarity(clusters, item) :
    dist = -1
    best = None
    for c in clusters :
        d = cosine_similarity(c.centroid, item)
        if d > dist :
            dist = d
            best = c
    return best

# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]


    for c in cluster_list :
        while len(c.members) == 0 :
            d = random.choice(data)
            print("HEYYY")
            if d.cluster == None : 
               d.cluster = c
               c.members.append(d)

    for d in data :
        c = random.choice(cluster_list)
        if d.cluster == None : 
            d.cluster = c 
            c.members.append(d)
        
    
    ## compute initial cluster centroids
    for c in cluster_list:
        c.calculate_centroid()

    change = True
    i = 0
    while change and i < 10 :
        change = False
        i += 1
        ##check every document
        #this will return the tree class
        #For every document in the data
        for d in data :
            #Classify it. This means finding the closest cluster
            #similarity returns the cluster that the data point is closets to
            c = similarity(cluster_list, d)      
            if (d not in c.members) :
                print("DOES THIS EVER CHANGE")
                c.members.append(d)
                #if it does belong to a current cluster
                d.cluster.members.remove(d)
                d.cluster = c
                change = True

        for c in cluster_list :
            c.calculate_centroid()
                

    # while not done and i < limit
    #   i++

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    #   compute the centroids of each cluster
    return cluster_list

