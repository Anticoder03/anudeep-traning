import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Marks": [85, 90, 95, 80]
}
df = pd.DataFrame(data)
print(df)
print(df["Age"]) #? works because its a single column and converted to series

#! print(df["Age","Marks"]) # does not work because it is not a single column, it is a tuple of columns. To select multiple columns, you need to pass a list of column names instead of a tuple. The correct way to select multiple columns would be:\

city = ["New York", "Los Angeles", "Chicago", "Houston"]
df["City"] = city
print(df)

sales_data = pd.read_csv("salesdata.csv")
print(sales_data.head())  #* Display the first few rows of the DataFrame
print(sales_data)  