

import pandas as pd

df = pd.read_csv('customer_data.csv')

df['First_Name'] = df['First_Name'].fillna('')
df['Last_Name'] = df['Last_Name'].fillna('')
df['Phone'] = df['Phone'].fillna('')
df['Gender'] = df['Gender'].fillna('')
df['Age'] = df['Age'].fillna(0)
df['Loyalty_Program'] = df['Loyalty_Program'].fillna(False)

df['City'] = df['City'].replace('', 'Unknown')
df['Zip_Code'] = df['Zip_Code'].replace('', 'Unknown')

df['Age'] = df['Age'].astype(int)
df['Loyalty_Program'] = df['Loyalty_Program'].astype(bool)

print(df)