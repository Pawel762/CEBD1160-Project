import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import pandas as pd
import os

wine_df = pd.read_csv('wine.data',
                      sep=',',
                      header=0)
wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue',
                   'od280 od315_of_diluted_wines',
                   'proline']

X = wine_df.drop('class', axis=1)
# Nrmlzd = preprocessing.normalize(X)

os.makedirs('chart', exist_ok=True)

# Heatmap
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(X.corr(), vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(220, 20, n=7), square=True)
ax.set_xticklabels(X.columns, rotation=45, horizontalalignment='right')
ax.set_yticklabels(X.columns, rotation=0)
fig.tight_layout()
plt.savefig('chart/heatmap-all.png')
plt.close()

# Based on the heatmap, we can select the properties that impact the most the Hue.
# od280 od315_of_diluted_wines, color_intensity, flavanoids, total_phenols,alcalinity_of_ash and malic_acid.