

"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html#pandas.to_numeric 
https://stackoverflow.com/questions/15891038/change-data-type-of-columns-in-pandas/47303880
# convert all columns of DataFrame
df = df.apply(pd.to_numeric) # convert all columns of DataFrame

# convert just columns "a" and "b"
df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)

"""