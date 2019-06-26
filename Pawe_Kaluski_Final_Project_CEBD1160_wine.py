import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
import pandas as pd
import os

wine_df = pd.read_csv('wine.data',
                      sep=',',
                      header=0)
wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids','nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280 od315_of_diluted_wines',
                   'proline']

X = wine_df.drop(['hue', 'class','alcohol', 'magnesium', 'ash'], axis=1)
y = wine_df['hue']

# Splitting features and target dataset into: train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.38)

# Training a Linear Regression model with fit()
lm = LinearRegression()
lm.fit(X_train, y_train)

# save the model to disk
joblib.dump(lm, 'Pawel_Kaluski_Wine_Model.sav')

# # Load the model
# lm_load = joblib.load('Pawel_Kaluski_Wine_Model.sav')


# Predicting the results for our test dataset
predicted_values = lm.predict(X_test)

# Printing the residuals: difference between real and predicted
for (real, predicted) in list(zip(y_test, predicted_values)):
    print(f"Value: {real:.2f}, pred: {predicted:.2f}, diff: {(real - predicted):.2f}")

# Plotting the residuals: difference between Actual and Predicted
sns.set(palette="plasma")
residuals = y_test - predicted_values
os.makedirs('chart', exist_ok=True)
os.makedirs('chart', exist_ok=True)
os.makedirs('chart', exist_ok=True)

sns.scatterplot(y_test, predicted_values)
plt.plot([0, 2], [0, 2], '--')
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
plt.savefig('chart/Actual_Predicted.png', dpi=300)
plt.show()
plt.close()

sns.scatterplot(y_test, residuals)
plt.plot([2, 0], [0, 0], '--')
plt.xlabel('Actual Value')
plt.ylabel('Residual (difference)')
plt.savefig('chart/Actual_ResidualDiff.png', dpi=300)
plt.show()
plt.close()

sns.distplot(residuals, bins=20, kde=False)
plt.plot([0, 0], [2, 0], '--')
plt.title('Residual (difference) Distribution')
plt.savefig('chart/ResidualDiff_Distribution.png', dpi=300)
plt.show()
plt.close()

# Understanding the error that we want to minimize
from sklearn import metrics
print(f"Printing MAE error(avg abs residual): {metrics.mean_absolute_error(y_test, predicted_values)}")
print(f"Printing MSE error: {metrics.mean_squared_error(y_test, predicted_values)}")
print(f"Printing RMSE error: {np.sqrt(metrics.mean_squared_error(y_test, predicted_values))}")
