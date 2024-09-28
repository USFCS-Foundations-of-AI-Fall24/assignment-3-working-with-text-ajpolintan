import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bc_data = pd.read_csv('breast-cancer.data')
bc_data.head()


classifications  = bc_data['class']
no = classifications.filter(like='no', axis=0)
yes = classifications.filter(like='recurrence-events', axis=0)
print(no)

#look 
counts = classifications.mode()
common = {}
print("MOST COMMON: " + counts)



#displays the most common data type
summary = bc_data.describe(include=[np.object_, pd.Categorical])
print(summary)

recurr = bc_data[bc_data['class'] == 'recurrence-events']
ages = recurr.groupby('age').size()

ages.plot(kind='bar', xlabel="ages", ylabel="recurrences", title="age vs recurrences")
plt.show()
print(recurr)
print(ages)
#print(classifications)
#compare the counts
