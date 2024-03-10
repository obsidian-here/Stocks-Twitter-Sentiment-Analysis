import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Data for plotting
t = np.arange (0.0, 3.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV) ',
title='Simple Sine graph')
ax. grid()
fig 

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import mpl_toolkits
# # %matplotlib inline

# data = pd.read_csv("kc_house_data.csv")

# fig=data['bedrooms'].value_counts().plot(kind='bar')
# plt.title('number of Bedroom')
# plt.xlabel('Bedrooms')
# plt.ylabel('Count')
# # sns.despine
# print(fig)