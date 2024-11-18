# write a Python function that returns a dict with names as keys and corresponding average of evaluations for each student

students = ["John", "Mark", "Alice"]
grades = [[27, 27, 30], [25, 18, "alfa"], [19, 20, 30, 28], [27, 21, 18]]


def set_average(students, grades):
    result = {}
    for s, g in zip(students, grades):
        avg_value = sum(g) / len(g)
        result[s] = avg_value

    return result


def set_average_lc(students, grades):
    return {s: sum(g) / len(g) for s, g in zip(students, grades)}


# main code
# print(set_average(students, grades))
print(set_average_lc(students, grades))

# write a solution that handles the following issues:
# non-integer values must be excluded from average
# consider only grades in the range 18-30
