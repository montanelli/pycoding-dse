# error handling
# syntax errors
# exception, runtime errors: they depend on the context, so they become evident only when you run the script with certain variable values
# examples of differente kinds of exceptions:
# TypeError, NameError, ValueError, IndexError


# consider a function for reading the element of a list in a given position
def list_access(alist, aposition):
    result = None

    try:
        result = alist[aposition]
    except IndexError:
        print(f"The position {aposition} is not defined in the list.")
        # in error handling, it is common to write in a log file the status of the variables, so that it will be possible to analyse what happended during the script execution
        return None

    # the following return operation is not executed when an exception is raised
    return result


# main code
fruits = ["apple", "banana", "cherry", "strawberry"]
try:
    position = int(input("insert a position index: "))
except:
    print("an error occurred during the input processing")

print(list_access(fruits, position))

exit()
