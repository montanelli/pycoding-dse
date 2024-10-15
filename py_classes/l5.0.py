# further data structures
# tuples are lists that are immodifiable
my_string = "stefano"
my_list = ["one", "two", "three"]
my_tuple = ("alfa", "beta", "gamma")

print(my_string[1])
print(my_list[1])
print(my_tuple[1])

# my_string[1] = "e"
# my_list[1] = "four"
# my_tuple[1] = "delta"

print(my_tuple.index("gamma"))

# a tuple consumes less memory than a list (because it has fewer methods and functionalities)
# it is a better solution than lists when a temp variable is needed (no need to edit the tuple content)

# sets
# A set is an unordered, unindexed, and unchangeable collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
fruits = {"apple", "banana", "cherry"}

# an item is added
fruits.add("strawberry")

# nothing is done
fruits.add("apple")

# an item is dropped
fruits.remove("banana")

# remoan error is raised when we remove an item that is not in the set
# test the presence of the item before using remove
if "peach" in fruits:
    fruits.remove("peach")

# other solution to remove an item from a set
# nothing is done and no error is raised
fruits.discard("peach")

print(fruits)

# how to drop duplicate items from lists
my_list = ["one", "two", "three", "one"]
my_list = list(set(my_list))
print(my_list)

# sets support basic set operations
odds = {1, 3, 5, 7}
even = {2, 4, 6, 8}
primes = {1, 2, 3, 5}

print(odds.union(even))
print(even.union(odds))
print(odds.intersection(primes))
# A (odds) - B (primes)
print(odds.difference(primes))
