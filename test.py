import pandas as pd

# read the two files
df1 = pd.read_csv("Data-part-one.csv")
df2 = pd.read_csv("Data-part-two.csv")

# take a look at the data
print(df1)
print(df2)

# we can look at the data and drop the undefined column of df1

df1 = df1.drop(["Unnamed: 2"], axis=1)

# merge
df = df1.merge(df2, left_on="id", right_on="id")

# take a look at the data
print(df)

# now that we dont need colun "id" anymore, we can delete it
df = df.drop(["id"], axis=1)

# take a look at the data
print(df)

# TODO change data types

# TODO: select row, select column, select row with condition (max) etc.

# feature enginieering. column junios, senior
# next line is placeholder
df = df.fillna(value=0)

# add two new columns
df['IsSenior'] = None

print(df)

# Junior if age < 45, Senior if age >= 45

df.loc[df['Age'] >= 45, 'IsSenior'] = True
df.loc[df['Age'] < 45, 'IsSenior'] = False
print()
print(df)
