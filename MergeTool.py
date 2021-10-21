import pandas as pd
import glob
from IPython.display import display

path = r'C:\Users\ConnorSands\OneDrive - DIAS Geophysical\Documents\Projects\Test Project\Dumped GPS Files\Spreadsheets'
path2 = r'C:\Users\ConnorSands\OneDrive - DIAS Geophysical\Documents\Projects\Test Project\Dumped GPS Files'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

print('Final Sheet:')
display(li)

import os  
frame.to_csv(os.path.join(path2,r'Master Spreadsheet 4.csv'), index=False, mode='w+')