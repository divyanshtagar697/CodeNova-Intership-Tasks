import pandas as pd
import numpy as np
import io
raw_data_string = """ID,Date,Price,Units,Category
101,2026-05-10,500,5,Electronics
102,2026-05-11,,10,Furniture
103,12-05-2026,300,8,electronics
101,2026-05-10,500,5,Electronics
104,2026-05-13,450,,Home
105,,200,15,Home

df = pd.read_csv(io.StringIO(raw_data_string))
print("--- Original Raw Data ---")
print(df)



df.drop_duplicates(inplace=True)



df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Units'] = df['Units'].fillna(0)
df.dropna(subset=['Date'], inplace=True)


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Category'] = df['Category'].str.capitalize()

df.to_csv('cleaned_internship_data.csv', index=False)

print("\n--- Cleaned & Processed Data ---")
print(df)
print("\nSuccess: 'cleaned_internship_data.csv' is ready for analysis.")
