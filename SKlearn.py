import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('abc_manufacturing_data.csv')

print(df.head())
print(df.info())
print(df.describe())

plt.figure(figsize=(12, 8))
sns.pairplot(df)
plt.show()

corr_matrix = df.corr()
print(corr_matrix)


X = df[['feature1', 'feature2', 'feature3']]
y = df['target_variable']

