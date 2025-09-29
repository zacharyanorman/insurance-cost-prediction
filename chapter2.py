import pandas as pd

x = [32, 45, 32, 47, 89]
year = list(range(2015, 2020))
df = pd.DataFrame({"Year": year, "Observation": x})
df.set_index("Year", inplace=True)

print(df)