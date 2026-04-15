import pandas as pd
df = pd.read_csv('C:/Users/deepa/Downloads/experience.csv')

print("Full DataFrame:")
print(df)
rows, columns = df.shape
print("\nNumber of rows:", rows)
print("Number of columns:", columns)
print("\nLength of DataFrame:", len(df))
print("\nFirst 2 rows:")
print(df.head(2))
