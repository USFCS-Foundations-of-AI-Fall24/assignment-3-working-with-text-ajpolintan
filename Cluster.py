import random
from Document import *
from Classifier import classify

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
  
        #
        #find all the unique keys
        for d in self.members :
            if len(union) == 0 :
                union = d.tokens.keys() 
            else : 
                union = union | d.tokens.keys()

        print(union)
        for item in union :
            #m is a document
            for m in self.members :
                self.centroid.tokens[item] += m.tokens[item] 
            self.centroid.tokens[item] = self.centroid.tokens[item] / num_documents
        
        print(self.centroid)
        #add the tokens to the centroid
        return self.centroid


# Call like so: k_means(2, ['pos','neg'], positive_docs + negative_docs)

def k_means(n_clusters, true_classes, data) :
    cluster_list = [Cluster(centroid=Document(true_class=item)) for item in true_classes]

    ## initially assign data randomly.
    for c in cluster_list :
        c.members.append(random.choice(data))

    ## compute initial cluster centroids
    for c in cluster_list:
        c.calculate_centroid()

    i = 0
    while i < n_clusters :
        i += 1
        
        ##check every document
        #this will return the tree class
        #for every document in the data. classift it 
        for d in data :
            #classify returns the centroid which is a document
            d.true_class = classify(cluster_list, d)      
            for c in cluster_list :
                if d.true_class == c.true_class :
                    c.members.append(d)

            


        for c in cluster_list :
            c.calculate_centroid()
                

    # while not done and i < limit
    #   i++

    #   reassign each Document to the closest matching cluster using
    #   cosine similarity
    #   compute the centroids of each cluster
    return cluster_list

