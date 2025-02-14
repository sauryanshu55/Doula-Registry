import pdfplumber
import pandas as pd

pdf_path = "scrapers/content/Massachussets Doulas.pdf"

table_data = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_table()
        if tables:
            for row in tables:
                table_data.append(row)

# Convert to a dataframe
df = pd.DataFrame(table_data)
df = df.iloc[1:].reset_index(drop=True) ## Remove the first row

print(df.head())

# Save to CSV if needed
df.to_csv("scrapers/data/ma.csv", index=False)
