import pandas as pd
    
print("Loading DataFrame from Google Sheets...")
url = "https://docs.google.com/spreadsheets/d/106TMskJ4wV9u9TZYWnaCUWD_XerEEVH3PwYHvFwaF8U/export?format=csv"

df = pd.read_csv(url)   
print("DataFrame loaded successfully.")

print(df)

print(df.head())

    
    

