import os
import pandas as pd
import re
df= pd.DataFrame(columns=['name','url'])
path= "C:/Users/guill/Desktop/buscar locations"

newlist = os.listdir(path)
if len(newlist) != 0:
    for item in newlist:
        if "pagina" in item:
            print(item)
            with open(item) as f:
                with open(item, "r",encoding="utf-8") as f:
                    file = f.readlines()

                # Loop through each line in the file
                for line in file:
                    # Use regex to find the number of 5 digits
                    number = re.search(r"\b\d{5}\b", line)

                    # Use regex to find the text starting with "ACUNID - "
                    text = re.search(r"ACUNID - .*</a></td>$", line)

                    # If both the number and text are found
                    if number and text:
                        # Append the number and text to the dataframe
                        df = df.append({"url": number.group(), "name": text.group()}, ignore_index=True)

                # Print the dataframe

df['name'] = df['name'].str.replace('</a></td>', '')
print(df)
df.to_csv('table.csv',sep=";",encoding='utf-8')

