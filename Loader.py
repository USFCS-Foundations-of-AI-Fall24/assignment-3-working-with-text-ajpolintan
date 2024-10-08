## Code for loading training sets and creating documents.
import string

from Document import *
from Cluster import *
from make_dataset import create_docs


# you should be able to call this like:
# positive_docs = create_easy_documents(pos_reviews, 'pos',
#                                  filters=[not_stopword],
#                                  transforms=[convert_to_lowercase, remove_trailing_punct])
def create_easy_documents(list_of_docs, true_class, filters=None, transforms=None) :
    document_list = []
    for item in list_of_docs :
        d = Document(true_class=true_class)
        words = item
        ## deal with filters here
        for f in filters:
            words = [word for word in words if f(word)]

        ## deal with transforms here

        d.add_tokens(words)
        document_list.append(d)
    return document_list

## filters - return true if the token meets the criterion

# you do this.
def not_stopword(token) :
    stop_words = ['a', 'an', 'the']
    return token is not stop_words

def not_cat(token) :
    return token is not 'cat'


# transforms - convert a token into a new format

# you do this.
def remove_trailing_punct(token) :
    return token.strip()

# and this
def convert_to_lowercase(token) :
    return token.tolower()



## homogeneity: for each cluster, what fraction of the cluster is comprised of the largest class?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
#ONLY ONE CLUSTER
# compute_homogeneity(result, ['pos','neg'])
def compute_homogeneity(list_of_clusters, list_of_classes) :
    # hlist will be the homogeneity for each cluster.
    hlist = []
    ##loop through the list of clusters
    for cluster in list_of_clusters :
        #find the dominant class
        findDominate = []
        #loop through the list of classes
        for c in list_of_classes :
            #for class the highest amount of members
            max = -1
            dom = 0
            class_list = [item for item in cluster.members if item.true_class == c]
            class_length = len(class_list)
            #pos is 500, neg is 400. I want to get the total for the cluster. cluster.length
            if class_length > max :
                max = class_length 
                dom = class_length
            
        
        #divide the number in the dominant class with teh length of the cluster
        hlist.append(dom / len(cluster.members))

    #hlist = []
    #for c in list_of_clusters :
    return hlist
    pass
    #return hlist

## completeness: for the dominant class in each cluster, what fraction
# of that class' members are in that cluster?
# call this like so:
# result = k_means(2, ['pos','neg'], positive_docs + negative_docs)
# compute_completeness(result, ['pos','neg'])

#find the dominate class. Completness looks at original dataset. 

#GET THE TOTAL NUMBER OF POSITIVE AND NEGATIVES
#FIND THE DOMINANT CLASS. GET THE TOTAL NUMBER OF THE DOMINANT CLASS
#DIVIDE BASED OFF THE TOTAL NUMBER OF POSITIVES AND NEGATIVES ACROSS THE CLUSTERS
#DO NOT DIVIDE BY NUMBER OF POSITIVE AND NEGATIVES WITHIN A CLUSTER
#find number of the donimation class
#divide by the number of class members

def compute_completeness(list_of_clusters, list_of_classes) :
    # clist will be the homogeneity for each cluster.
    
    #  clist = []
    pass 
    # return clist

if __name__=="__main__" :

    pos_reviews, neg_reviews = create_docs(10,10)

    positive_docs = create_easy_documents(pos_reviews, 'pos',
                                 filters=[],
                                 transforms=[])
    #print(positive_docs)
    negative_docs = create_easy_documents(neg_reviews, 'neg',
                                    filters=[],
                                 transforms=[])
    

    result = k_means(2, ['pos','neg'], positive_docs + negative_docs)

    #print(negative_docs)





