import pandas as pd
import numpy as np

bc_data = pd.read_csv('breast-cancer.data')
bc_data.head()


classifications  = bc_data['class']
no = classifications.filter(like='no', axis=1)
yes = classifications.filter(like='recurrence-events', axis=0)
print(no)

#look 
counts = classifications.max()
common = {}
print("MOST COMMON: " + counts)



#displays the most common data type
summary = bc_data.describe(include=[np.object_, pd.Categorical])
print(summary)

#print(classifications)
#compare the counts
