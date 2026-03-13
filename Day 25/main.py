"""
This file demonstrates different methods for working with CSV data in Python, 
showing how we can move from manual file handling to powerful data analysis with Pandas.
"""

# --- METHOD 1: Basic File Handling ---
# This is the most manual way of reading a CSV file.
# It reads everything as a list of strings, including headers and newline characters.
# Manual parsing is required to do anything meaningful with the data.
# with open("weather_data.csv") as data_file:
#     raw_data = data_file.readlines()
#     print("Raw Data Strings:", raw_data)

# --- METHOD 2: Using the Built-in CSV Module ---
# Python's built-in 'csv' module provides a 'reader' object to iterate over rows.
# This approach splits lines into lists (rows), which is better than Method 1.
# However, you still need to manually loop through rows and convert data types.
# import csv
# with open("weather_data.csv") as data_file:
#     csv_reader = csv.reader(data_file)
#     temperatures = []
#     for row in csv_reader:
#         # We skip the "temp" header and convert subsequent values to integers.
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print("Row from CSV module:", row)
#     print("Temperature List:", temperatures)

# --- METHOD 3: Using the Pandas Library (Industry Standard) ---
# Pandas is optimized for data analysis and provides much cleaner syntax.
import pandas

# Read the CSV directly into a 'DataFrame' (a table-like object).
# data = pandas.read_csv("weather_data.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# 1. Accessing Data:
# Columns can be accessed as a 'Series' (a list-like object).
# print("Temperature Column Data:\n", data["temp"])
# print("Condition Column Data:\n", data.condition) # Accessing via attribute style

# 2. Basic Conversions and Calculations:
# You can convert columns to Python dictionaries or lists easily.
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# Instead of calculating averages manually, Pandas has built-in methods:
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()
# print(f"Average Temp: {average_temp}, Max Temp: {max_temp}")

# 3. Filtering Data (Rows):
# You can select specific rows based on conditions.
# print("Monday's Data:\n", data[data.day == "Monday"])
# print("Row with the highest temperature:\n", data[data.temp == data.temp.max()])

# 4. Extracting and Converting Specific Values:
# Finding Monday's temperature and converting it from Celsius to Fahrenheit.
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0] # [0] accesses the actual integer value in the Series
# monday_temp_F = (monday_temp * 9/5) + 32
# print(f"Monday's temperature in Fahrenheit: {monday_temp_F}")

# --- CREATING DATAFRAMES FROM SCRATCH ---
# You can create a new DataFrame from a Python dictionary and save it to a file.
# student_data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(student_data_dict)
# print("\nCreated DataFrame from scratch:\n", new_data)

# Export the new data to a new CSV file
# new_data.to_csv("new_data.csv")
# monday = data[data.day == "Monday"]
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(f"Cinnamon: {cinnamon_squirrels_count}")
print(f"Gray: {gray_squirrels_count}")
print(f"Black: {black_squirrels_count}")

squirrel_dict = {
    "Primary Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
print(squirrel_dict)
squirrel_data = pandas.DataFrame(squirrel_dict)
squirrel_data.to_csv("squirrel_count.csv")