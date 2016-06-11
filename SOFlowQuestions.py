"""
How do i find the highest value and swap it within the end value in an array in python

"""
import collections

array = [1, 3, 4, 12, 4, 7]

"""
def get_and_swap(give_array):
    maxindex = give_array.index(max(give_array))
    # minindex = give_array.index(min(give_array))
    give_array[-1], give_array[maxindex] = give_array[maxindex], give_array[-1]
    return array


print(get_and_swap(array))
print("Trying the logic with for loop")
√√Compound interest

def get_swap(array):
    indexmax = 0;
    for i in range(len(array)):
        if array[i] > array[indexmax]:
            indexmax = i
    array[-1], array[indexmax] = array[indexmax], array[-1]


print(array)
get_swap(array)

def get_maxnum(give_array):
    maxnum = max(give_array)
    return maxnum
print("max num is ",get_maxnum(array))
"""

"""
#looping through letters and words
sentence = input("Please enter a sentence \n")
no_space = ""

for letter in sentence:
    if letter != " ":
        no_space += letter
print("sentence without spaces")
print(no_space)

for i in sentence.split(" "):
    print(i)
"""

# looping through nested for loops
students = [("Alejandro", ["CompSci", "Physics"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Ed", ["CompSci", "Accounting", "Economics"]),
            ("Margot", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]
for (name, subjects) in students:
    print(name, " takes ", len(subjects), " courses")

# looping through the subjects
students.append(("George", ["Economics", "Law", "Stats", "Music", "CompSci"]))  # adding new data
students.append(("Michael", ["English", "Chemistry", "Math", "Music", "CompSci"]))
counter = 0
for (name, subjects) in students:
    for s in subjects:
        if s == "CompSci":
            counter += 1
            # print(name)  # names of the students
print("The number of students taking CompSci is ", counter)

numbers = [1, 2, 3, 4, 5]
com_num = [x ** 2 for x in numbers]  # square
print(com_num)

"""
Suppose an amount of 1,500 is deposited in a bank paying an annual interest rate of 4.3%, compounded quarterly.
Then the balance after 6 years is found by using the formula above, with P = 1500, i = 4.3% = 0.043, n = 4, and t = 6:

"""


def compound_interest(p, i, n, t):
    finance = p * (1 + (i / n)) ** (n * t)
    principal_sum = finance - p
    print("Principal sum is ", round(principal_sum, 2))


compound_interest(1500, 0.043, 4, 6)

"""
finding VOWELS in given words
[x for x in t if x not in s]
"""
VOWELS = "aeiou"


def find_vowels(words):
    print(sum([x in VOWELS for x in words], ))


find_vowels("Michael")
word_list = ['big', 'cats', 'like', 'really']


def count_vowel(word):
    vowels = "aeiou"
    for v in vowels:
        count = 0
        for x in word:
            if v in x:
                count += 1
        print(v, "occurs ", count, " times")


count_vowel(word_list)


def count_vowels2(word):
    print("The the second method->>>>>>>>>>>>>>here\n")
    vowels = "aeiou"
    letters = collections.Counter("".join(word))
    for letter in vowels:
        print(letter, " occurs", letters.get(letter, 0), " times")


count_vowels2(word_list)
