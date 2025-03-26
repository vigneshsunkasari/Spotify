import pandas as pd 
df=pd.read_csv("dataset.csv")
df.to_json("spotify.json",orient="records",indent=4)