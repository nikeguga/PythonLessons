# Опция раз

# import random
# import pandas as pd

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


# categories = data['whoAmI'].unique()
# one_hot = pd.DataFrame(0, columns=categories, index=range(len(data)))

# for i, category in enumerate(categories):
#     one_hot[category] = (data['whoAmI'] == category).astype(int)


# one_hot.head()

# Опция два

import numpy as np
import pandas as pd

#  для создания DF
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# клеим значения 'whoAmI' к числовым индексам
unique_values = data['whoAmI'].unique()
value_to_index = {value: index for index, value in enumerate(unique_values)}

#  one-hot 
one_hot_encoded = np.zeros((len(data), len(unique_values)), dtype=int)
for i, value in enumerate(data['whoAmI']):
    one_hot_encoded[i, value_to_index[value]] = 1

# df под one-hot
one_hot_df = pd.DataFrame(one_hot_encoded, columns=unique_values)

# Вывод результата
one_hot_df.head()
