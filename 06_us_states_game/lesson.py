# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)
# This is a lot of code for just getting a column of data. We need the help of Pandas

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data)) It's a data frame
# Same operation as before, and better formatting
# print(data["temp"]) this is a Series, like a list
# data_dict = data.to_dict() to convert data frames into dictionaries
temp_list = data["temp"].to_list()
# Converting a Series into a list
# Mean of temperatures:
temp_mean = sum(temp_list)/len(temp_list)
temp_mean_method = data["temp"].mean()
# This last method requires a Series object, not a list
# data["condition"] == data.condition, because Pandas converts the names of the columns into attributes of the
# data frame
# Getting the row of data with the maximum temperature:
# print(data[data.temp == data.temp.max()])
# Getting a particular value in a row
# monday = data[data.day == "Monday"]
# print(monday.condition)
