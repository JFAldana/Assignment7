### *Dev* **JoeAldana** *Data* **3mar22**
# Pickling and Error Handling
## Pickle Module
### Pickling data means converting it from a text format into its binary machine format. You can then save or read to files in the binary form. This has the possible advantage of saving space but does not encrypt the data.
#### Here is the resource I found most helpful: https://docs.python.org/3/library/pickle.html
#### Here is example of some code using the pickle module:
#### ``` 

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
file.close()    ```
