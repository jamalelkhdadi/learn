import pandas


my_data = pandas.read_csv("csv.csv")

name = my_data["name"]
value = my_data["value"]

for i in name:
    print(i)

for i in value:
    print(i)
