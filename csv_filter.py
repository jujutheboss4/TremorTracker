import pandas as pd

# read csv
df = pd.read_csv("/path/to/file")

# filter to only include points after a certain number of rows
df = df[df["Time"] > 13000]

# make new csv file
df.to_csv("normal_walk_arm_13k.csv", index=False)
