import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
#print(pd.get_dummies(data))

data_one_hot_view = data
code_column = data_one_hot_view.columns[0]
values = set(data_one_hot_view[code_column].to_list())
for i in values:
    data_one_hot_view[code_column + "_" + i] = data_one_hot_view[code_column] == i
data_one_hot_view = data_one_hot_view.drop([code_column], axis=1)

print(data_one_hot_view)