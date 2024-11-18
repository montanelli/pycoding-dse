# write a Python function to drop the first x elements and the last y elements from a list
def list_slice(alist, x, y):
    # check if the x, y params are valid input:
    # accept only positive integers
    # accept only x, y that are real list positions
    # accept only x<y
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Only integers are valid params")
        return None

    if x < 0 or y < 0:
        raise ValueError("Negative values are not allowed")

    if x >= y:
        raise ValueError("x must be lower than y")

    if y >= len(alist):
        raise ValueError("y must be a valid list position")

    return alist[x:-y]


# main
animals = ["tiger", "lion", "elephant", "dog", "cat"]
try:
    print(list_slice(animals, 1.1, 5))
except ValueError as e:
    print(e)
