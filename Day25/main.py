# # with open("D:\Harsh\Python\Day25\weather-data.csv") as file:
# #     data = file.readlines()
# #     print(data)


# import csv
# # with open("D:\Harsh\Python\Day25\weather-data.csv") as file:
# #     data = csv.reader(file)
# #     temp = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temp.append(int(row[1]))
            
# #     print(temp)

# import pandas

# data = pandas.read_csv("D:\Harsh\Python\Day25\central-data.csv")
# gray_data = len(data[data["Primary Fur Color"] == "Gray"])
# red_data = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_data = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_data)
# print(red_data)
# print(black_data)

# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [gray_data, red_data, black_data]
# }

### DataFrame is used to create a new file with the csv data with the help of the pandas 
# df = pandas.DataFrame(data_dict)
# df.to_csv("Squiral_Count.csv")


