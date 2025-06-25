import components.read_gsheet as read_gsheet


# Example usage:# sheet_url = "https://docs.google.com/spreadsheets/d/your_sheet_id_here/export?format=csv"

sheet_url = "https://docs.google.com/spreadsheets/d/106TMskJ4wV9u9TZYWnaCUWD_XerEEVH3PwYHvFwaF8U"

df  = read_gsheet(sheet_url)

print(df.head())  # Display the first few rows of the DataFrame
