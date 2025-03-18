import pandas as pd

df = pd.read_csv('Meteorite_Landings.csv')
df2 = pd.read_csv('Meteorite_Landings.csv')
df3 = pd.read_csv('Meteorite_Landings.csv')

# ↑ Reading in as three seperate dataframes to seperate out the meteor types according to the Meteorlogical bulletin.

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


meteorites = {}

schema_df = pd.read_csv('Meteorite_Landings.csv')
# print(schema_df)

sampling = df.sample(5)

df.drop(['reclat', 'reclong', 'GeoLocation'], axis=1, inplace=True)
df2.drop(['reclat', 'reclong', 'GeoLocation'], axis=1, inplace=True)
df3.drop(['reclat', 'reclong', 'GeoLocation'], axis=1, inplace=True)



df1 = df[df.isna().any(axis=1)]


df.dropna()

pattern = r'^H[0-9]'
pattern2 = r'^L[0-9]'
pattern3 = r'^LL[0-9]'


# row dropping thing

df = df[df['class'].str.contains(pattern2)]


# ↑ Looking for L types

df2 = df2[df2['class'].str.contains(pattern)]


# ↑ Looking for H types

df3 = df3[df3['class'].str.contains(pattern3)]

# ↑ Looking for LL types


# Saving to CSV

frames = [df, df2, df3]

combination = pd.concat(frames)


combinationNaN = combination[combination.isna().any(axis=1)]
combination = combination.dropna()

combination['name'] = combination['name'].apply(lambda x: ''.join(char for char in x if ord(char) < 128))

print(combination.info())
combination.set_index('id',inplace=True)
print(combination.info())
combination.to_csv('Meteorites Cleaned.csv', encoding = 'utf-8', index=False)
a = combination.T.to_dict()
print(a)
# Clean!

print("\nRaw data has been processed and has been exported as 'Meteorites Cleaned.csv' in folder 'CSCollection'.")