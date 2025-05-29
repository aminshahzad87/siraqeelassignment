#  Ameen shazad 
#  237019
 # Q1: casting and type() Function in Python

x = "5"
y = int(x) + 10
print(y)

x = 42
print(type(x))

y = .43
print(type(y))

z = "word"
print(type(z))

mylist = [1, 2, 3]
print(type(mylist))


# Q2: Using List in Python

fruits = ["apple", "banana", "cherry"]

print(fruits[1], fruits[0])

# Loops
for fruit in fruits:
    print(fruit, end = " ")

# Add Items
print()
fruits.append("mango")
fruits.insert(1, "apple")
print("Fruits after adding mango and apple",fruits)

# Remove
fruits.remove("apple")
print("fruits after removing one apple",fruits)

# Sorting
numbers = [5, 2, 9, 1]
numbers.sort()
print("sorted list",numbers)  

numbers.sort(reverse=True)
print("sorted list in desc",numbers) 

# Copying list
copiedList = fruits.copy()
print(copiedList)

# List Comprehension
evens = [x for x in numbers if x % 2 == 0]
print("list of evens", evens)


# Q3: Tuples in python

colors = ("red", "green", "blue")

print(colors[0])
print(colors[-1])

# Looping
for color in colors:
    print(color, end = "  ")

# Joining two tuples
print()
tuple1 = (1, 2)
tuple2 = (3, 4)

joined = tuple1 + tuple2
print("Joined tuple1 and tuple2",joined)

# Update items in a tuple
colors_list = list(colors)
colors_list[1] = "yellow"
colors = tuple(colors_list)
print("tuple after updating item 1 to yellow",colors)

# Upacking
person = ("Alice", 25, "Engineer")

name, age, job = person
print(name)
print(age)  
print(job)

#some method of tuple

numbers = (1, 2, 2, 3, 4)
print(f"Count 2 in tuple numbers: {numbers.count(2)}")
print(f"index of item 3 in tuple: {numbers.index(3)}")


# Q4 Different set methods

fruits = {"apple", "banana"}
fruits.add("cherry")
print("After adding cherry to fruits set: ",fruits) 

a = {1, 2, 3}
b = {3, 4, 5}
result = a.union(b)
print("Union of two sets",result)

a = {1, 2, 3}
b = {2, 3, 4}
print("Difference of two sets", a.difference(b))

original = {1, 2, 3}
copy_set = original.copy()
print("Copied set ",copy_set) 


# Q5 Array in python---used to store items of same type

import array

numbers = array.array('i', [1, 2, 3, 4])
print(numbers)


numbers.append(40)
print("After adding 40",numbers)

""" Q6: A list named shopping_list like shopping_list = ["milk", "bread", 
"eggs", "butter", "juice", "sugar", "salt", "biscuits", "tea", "coffee"] 
is given with some initial items. 
Write a Python program to do the following: 
1. Display all items using a loop 
2. Ask the user if they want to add a new item 
 If yes, add the item to the list 
3. Ask the user if they want to remove any item 
 If the item exists, remove it 
 Otherwise, print "Item not found" 
4. Finally, display the updated list """


shopping_list = ["milk", "bread", 
"eggs", "butter", "juice", "sugar", "salt", "biscuits", "tea", "coffee"]
print("Current shopping list:")
for item in shopping_list:
    print("-", item)

add_item = input("\nDo you want to add a new item? (yes/no): ").strip().lower()
if add_item == "yes":
    new_item = input("Enter the item to add: ").strip()
    shopping_list.append(new_item)

remove_item = input("\nDo you want to remove an item? (yes/no): ").strip().lower()
if remove_item == "yes":
    item_to_remove = input("Enter the item to remove: ").strip()
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
    else:
        print("Item not found.")

print("\nUpdated shopping list:")
for item in shopping_list:
    print("-", item)

# Q7: even_odd_checker function

def check_even_odd(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

check_even_odd(1)
check_even_odd(2)

# Q8 Module in python
import math

num = 16
print("Square root:", math.sqrt(num))
# we can also use custom created module in out python file

"""Q9: You have a tuple containing students’ marks: 
I. Print the first and last elements of the tuple. 
II. Unpack the tuple elements into separate variables (e.g., m1, 
m2, m3, m4, m5). 
III. Create a new tuple by adding 5 marks to each element of the 
original tuple. (Remember, tuples are immutable, so create a 
new tuple.) 
IV. Print both the original and the new tuples. """

marks = (65, 70, 75, 80, 85)
print("First mark:", marks[0])
print("Last mark:", marks[-1])
m1, m2, m3, m4, m5 = marks
print("Unpacked marks:", m1, m2, m3, m4, m5)
new_marks = tuple(mark + 5 for mark in marks)
print("Original marks:", marks)
print("New marks (+5 each):", new_marks)


"""Q10: Takes a list of numbers: 
numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11] 
• Loops through each number and: 
• If the number is divisible by 3, print "X is divisible by 3" 
• Else if the number is even, print "X is even but not divisible by 
3" 
• Else print "X is odd and not divisible by 3" 
• At the end, print how many numbers were divisible by 3, how 
many were even (but not divisible by 3), and how many were 
odd (and not divisible by 3). """

numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]

count_div3 = 0
count_even_not_div3 = 0
count_odd_not_div3 = 0

for x in numbers:
    if x % 3 == 0:
        print(f"{x} is divisible by 3")
        count_div3 += 1
    elif x % 2 == 0:
        print(f"{x} is even but not divisible by 3")
        count_even_not_div3 += 1
    else:
        print(f"{x} is odd and not divisible by 3")
        count_odd_not_div3 += 1

print("\nSummary:")
print(f"Numbers divisible by 3: {count_div3}")
print(f"Numbers even but not divisible by 3: {count_even_not_div3}")
print(f"Numbers odd and not divisible by 3: {count_odd_not_div3}")

"""Q11: Write a function named classify_numbers that: 
1. Takes a list of numbers as input. 
2. Loops through each number in the list and: 
 Prints "X is positive" if the number is greater than zero 
 Prints "X is zero" if the number is zero 
 Prints "X is negative" if the number is less than zero 
3. Returns a dictionary with counts of positive, zero, and negative 
numbers."""

def classify_numbers(numbers):
    counts = {"positive": 0, "zero": 0, "negative": 0}

    for num in numbers:
        if num > 0:
            print(f"{num} is positive")
            counts["positive"] += 1
        elif num == 0:
            print(f"{num} is zero")
            counts["zero"] += 1
        else:
            print(f"{num} is negative")
            counts["negative"] += 1

    return counts

nums = [10, -5, 0, 3, -1, 0, 7]
result = classify_numbers(nums)
print("\nCounts:", result)