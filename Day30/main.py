### In this day we'll see how to handle errors in python and catch the exceptions and also see about the json

try:
    file = open("./Day30/a_file.txt")
    a_dictionary = {"key" : "value"}
    # print(a_dictionary["nagu"])

except FileNotFoundError:
    file = open("./Day30/a_file.txt" , "w")
    file.write("something")

except KeyError as error_message:
    print(error_message)

else: ### this else statement only executed when try block has been executed successfully otherwise not.
    print("try block has executed successfully")

finally: ## this code will be executed anyhow 
    print("I will run any how!")
    raise ValueError("this value error is created by dodiya harsh.")


### Now we are learning about the json data formate for the python language

# to write in the json file we use json.dump()
# to read from the json file we use json.load()
# to update in the json file we use json.update()
