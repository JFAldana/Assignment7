# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Error Handling
# ChangeLog (Who,When,What):
# JoeAldana,2.28.2022,Created started script
# ---------------------------------------------------------------------------- #

import pickle

try:
    animal = input("Enter an animal: ")
    color = input(f"Enter {animal}'s color: ")
    if animal.isnumeric() or color.isnumeric():
        raise Exception("Please do not use numbers!")
    animal_list = [animal, color]
except Exception as n:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(n, n.__doc__, type(n), sep='\n')

def save_pickled_data(file, list):
    """Storing pickled data"""
file = open("pickled.txt", "ab")
list = animal_list
pickle.dump(animal_list, file)
file.close()

def read_pickled_data(file):
    """Reading the pickled data"""
file = open("pickled.txt", "rb")
animal_list = pickle.load(file)
file.close()


print("Data is about to be pickled")
save_pickled_data(file, list)
print("Data has been pickled, please view 'pickled.txt'.")
input("Please push enter to continue. ")
print("Data is about to be loaded from file")
read_pickled_data(file)
print("This is the data" + "\n" + str(animal_list))
