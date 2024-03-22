## In this program we'll know about the list comprehension

# the list comprehension is used to make shorter the array 

# for example in regular mathod we use this
# In this mathod we use for loop to increment the list to the 1 for each element
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add = n + 1
# new_list.append(add)

## Instead of doing this long mathod we use list comprehension and the syntax for the loop comprehension is :
# new_list = [new_item for item in list]
# if we compare this to above mathod we can see that list is equal to numbers and item is equal to n and new_item is equal to n + 1
# so now 

## This is the excercise for the list comprehension
# numbers = [1, 2, 3, 4, 5]
# new_list = [n + 5 for n in numbers]
# print(new_list)

# name = "Harsh Sanjaybhai Dodiya"
# new_name = [ch for ch in name]
# print(new_name)

# numbers = [n * 2 for n in range(1, 10)]
# print(numbers)



### Now there is another type its called conditional list comprehension
# syntax : new_list = [new_item for item in list if test]

# names = ["Harsh", "Mithil", "Man", "Anopsinh", "Punit", "Meet", "Dhairya", "Bhavlo"]
# short_names = [new_names for new_names in names if len(new_names) <= 6]
# print(short_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n ** 2 for n in numbers if n % 2 == 0]
# print(squared_numbers)


# with open("Day26/file1.txt") as file1:
#     file1_data = file1.readline()

# with open("Day26/file2.txt") as file2:
#     file2_data = file2.readline()


# result = [int(num) for num in file1_data if num in file2_data]
# print(result)


### Now we are learning to use the comprehension of the dictionary
## for that the syntax is : 
# result = {new_key: new_value for item in list}


# sentence = "The Mahabharat is the most powerful book on the entire earth."

# dict = {word: len(word) for word in sentence.split()}
# print(dict)


student_dict = {
    "student": ["Harsh", "Dev", "Dhairya"],
    "score" : [88, 89, 90]
}

# for (key, value) in student_dict.items():
#     print(value)


import pandas
student_data = pandas.DataFrame(student_dict)
# print(student_data)


## this is mathod for loop through dataframe
# for (key, value) in student_data.items():
#     print(value)



## now we are itereting the by the rows and columns

for (index, rows) in student_data.iterrows():
    print(rows.score)