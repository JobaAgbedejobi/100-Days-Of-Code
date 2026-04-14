#HANDLING ERRORS & EXCEPTIONS

# #FileNotFound
# with open("a_file.txt") as file:
#    file.read()

#KeyError
# dict = {"key" : "value"}
# value = dict["a_non-existent_key"]

# #IndexError
# fruit_list = ["Banana", "Apple", "Pear"]
# fruit = fruit_list[3]
# print(fruit)

# #TypeError
# text = "abc"
# print(text + 5)

# #CATCHING EXCEPTIONS: THE TRY CATCH EXCEPT FINALLY PATTERN
# try: Something that might cause an exception/error
# except: Do this if there WAS an exception/error
# else: Don this if there were NO exceptions/errors
# finally: Do this no matter what happens

# # i.e:
# try:
#     with open("a_file.txt") as file:
#         file.read()
# except:
#     print("There was an error!")
#
# # i.e. 2:
# try:
#     with open("a_file.txt") as file:
#         file.read()
#     dictionary = {"key": "value"}
#     print(dictionary["nothing_key"])
# except:
#     file = open(file="a_file.txt", mode="w")
#     file.write("Something")

# i.e. 3:
# try:
#     file = open("a_file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["key"])
# except FileNotFoundError:
#     file = open(file="a_file.txt", mode="w")
#     file.write("Something")
# # except KeyError:
# #     print("That key doesn't exist!")
# #OR:
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed!")

# # RAISING YOUR OWN EXCEPTIONS
# # i.e.
# # finally:
#     # raise TypeError("This is an error that I made up")

height = float(input("What is your height in metres?\n"))
weight = int(input("What is your weight in kilograms\n"))

if height > 3:
    raise ValueError("You shouldn't be that tall!")

BMI = weight / height ** 2
print(f"BMI: {BMI}")

#JSON: composed of many lists and dictionaries in a {key}:{value} pair data structure