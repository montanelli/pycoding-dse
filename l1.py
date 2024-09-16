"""This is the intro to Python programming"""

import sys

# return the result of an exam according to the result of different modules
# consider that modules can be weighted
# consider to manage courses with a non-predefined number of modules

# setup for three fixed modules
m1_grade = 18
m2_grade = 20
m3_grade = 30

m1_weight = 0.25
m2_weight = 0.25
m3_weight = 0.5

# setup for a variable number of modules as a list
grades = [18, 20, 30, 25]
weights = [0.25, 0.25, 0.5, 1]

# grade with three modules
# grade = (m1_grade + m2_grade + m3_grade) / 3

# grade with three weighted modules
# grade = (m1_grade*m1_weight + m2_grade*m2_weight + m3_grade*m3_weight) / (m1_weight + m2_weight + m3_weight)

# grade with lists
# iterate/loop over the grades/weights lists
sum_modules = 0
for i, num in enumerate(grades):
    sum_modules += num * weights[i]

grade = sum_modules / sum(weights)

if grade >= 18:
    print("exam passed")
else:
    print("exam failed")

sys.exit()
