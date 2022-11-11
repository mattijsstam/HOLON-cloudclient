# make_a_set.py
import pandas as pd

for i in set(pd.read_clipboard().values[:, 0]):
    print(i)
