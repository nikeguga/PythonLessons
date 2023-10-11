import random
import pandas as pd
import numpy as np

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# Создание one-hot кодировки с использованием numpy
categories = data['whoAmI'].unique()
one_hot = pd.DataFrame(0, columns=categories, index=range(len(data)))

for i, category in enumerate(categories):
    one_hot[category] = (data['whoAmI'] == category).astype(int)

# Вывод результата
one_hot.head()