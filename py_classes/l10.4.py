# Further exercises

# determine the output of the following codes
# A #
s = "never change your mind"
s1 = s.split()
s2 = " ".join(s1[1::2])

print(s2)

# B #
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = [n for r in m for n in r]
print(l)

# C #
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]

print([x for x in l1 if x in l2])

# D #
print([x for x in range(10, 100) if str(x) == str(x)[::-1]])


# E #
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d = {}
for (k1, v1), (k2, v2) in zip(d1.items(), d2.items()):
    d[k1] = v1
    d[k2] = v2
print(d)


# F #
# write a Python function that returns the Least Frequent Character in a String
# return all the elements with the minimum frequency
def least_frequent_char(the_string):
    frequencies = {}
    for i in the_string:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    the_min = min(frequencies.values())
    the_leasts = []
    for f in frequencies:
        if frequencies[f] == the_min:
            the_leasts.append(f)
    return the_leasts


s = "things never change if you do not try"
print(least_frequent_char(s))


# G ¶
# write a Python function to split a list into a given number of segments.
# example with 2 segments. x is half-index; y is len(list)
# list[0:x], list[x:y]. it is equivalent to
# list[0:x], list[x:2x].
# example with 3 segments. x is 1/3-index
# list[0:x], list[x:2x], list[2x:3x]
def split_list(alist, segments):
    length = len(alist)
    return [
        alist[i * length // segments : (i + 1) * length // segments]
        for i in range(segments)
    ]


segments = [2, 3, 4]
animals = ["dog", "cat", "elephant", "tiger", "bear", "lion"]

for i in segments:
    animal_segments = split_list(animals, i)
    print(animal_segments)
