import pandas as pd 
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
import statsmodels.api as sm

vancouver = pd.read_csv('project.csv')

#scatterplot

#ratings vs. amenities
plt.figure(figsize=(10, 5))
x = vancouver['review_scores_rating']
y = vancouver['count_amenities'] 
reg = stats.linregress(x,y)
plt.scatter(x, y)
plt.plot(x, reg.intercept + reg.slope*x, 'r-', linewidth=3)
plt.xlabel('review rating')
plt.ylabel('amenities count')
plt.title('review rating vs. amenities count')
print(reg.slope, reg.intercept)
print(reg.pvalue)
print(reg.rvalue)
print(reg.rvalue**2)


#price vs. amenities
vancouver = vancouver[vancouver['price'] <= 1000]
plt.figure(figsize=(10, 5))
x = vancouver['price']
y = vancouver['count_amenities'] 
reg = stats.linregress(x,y)
plt.scatter(x, y)
plt.plot(x, reg.intercept + reg.slope*x, 'r-', linewidth=3)
plt.xlabel('price')
plt.ylabel('amenities count')
plt.title('price vs. amenities count')
print(reg.slope, reg.intercept)
print(reg.pvalue)
print(reg.rvalue)
print(reg.rvalue**2)

#x: price
#y: # of amenities
z = vancouver['accommodates']
data = pd.DataFrame({'y':y, 'x': x, 'z': z})
results = sm.OLS(data['y'], data[['x', 'z']]).fit()
print(results.summary()) 

