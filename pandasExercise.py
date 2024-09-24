import pandas as pd
import numpy as np

bc_data = pd.read_csv('breast-cancer.data')
bc_data.head()

classifications  = bc_data['class']
print(classifications)