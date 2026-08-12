import pandas as pd
# data = {
#     "Name": ["Alice", "Bob", "Charlie", "David"],
#     "Age": [25, 30, 35, 40],
#     "Marks": [85, 90, 95, 80]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df["Age"]) #? works because its a single column and converted to series

#! print(df["Age","Marks"]) # does not work because it is not a single column, it is a tuple of columns. To select multiple columns, you need to pass a list of column names instead of a tuple. The correct way to select multiple columns would be:\

# city = ["New York", "Los Angeles", "Chicago", "Houston"]
# df["City"] = city
# print(df)

sales_data = pd.read_csv("salesdata.csv")
# print(sales_data)  
# print("Head: ", sales_data.head())  #* Display the first few rows of the DataFrame
# print("Tail: ", sales_data.tail())  #* Get summary statistics of the DataFrame

# print("Describe: ", sales_data.describe())  #* Get summary statistics of the DataFrame

# print("Info: ", sales_data.info())  #* Get information about the DataFrame

# print("Columns: ", sales_data.columns)  #* Get the column names of the DataFrame

# print("Shape: ", sales_data.shape)  #* Get the shape of the DataFrame

# print("Inverse of the describe: ", sales_data.describe().T)  #* Get the inverse of the describe DataFrame

# print("lowest amount in unit price: ", sales_data["UnitPrice"].min())  #* Get the minimum value of the "UnitPrice" column


print("Uniques manager names: ",sales_data["Manager"].unique())  #* Get the unique values of the "Manager" column

print("Count of unique manager names: ",sales_data["Manager"].nunique())  #* Get the count of unique values in the "Manager" column

print("Count of each unique manager name: ",sales_data["Manager"].value_counts())  #* Get the count of each unique value in the "Manager" column

