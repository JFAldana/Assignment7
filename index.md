##### *Dev* **JoeAldana** *Data* **3mar22**
# Pickling and Error Handling
## Pickle Module
### Pickling data means converting it from a text format into its binary machine format. You can then save or read to files in the binary form. This has the possible advantage of saving space but does not encrypt the data.
#### Here is the resource I found most helpful: https://docs.python.org/3/library/pickle.html
#### Here is example of some code using the pickle module:
```
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
```
## Error Handling
### Error handling is done by the the built-in class BaseException. From there all other exception classes are child classes. The coder is also able to create custom child exception classes to try for errores not already built into Python.
#### Again the most helpful link was from Python: https://docs.python.org/3/library/exceptions.html?highlight=exception#BaseException
#### Here is my code using a simple error handling case:
```
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
```
