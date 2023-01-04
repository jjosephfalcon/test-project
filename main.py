
# fishes = ["shark", "whale", "dolphin", "zebra fish", "sea horse"]


# num = fishes.index("nemo")
# print(num)

# Check to see if "shark" exists in fishes. Print "FOUND SHARK" if found.
# # 
# if "shark" in fishes:
#   print("Found Shark")
#   # Find the index of "shark" inside of fishes list using index()
#   idx = fishes.index("shark")
#   fishes.pop(idx)
 


# print(fishes)

# # Create a function that takes a list of items, and an item to remove.
# # The function will remove the item from the list and then return the list. 




# dbz = ["goku", "vegeta", "naruto"]
# wrong_char = "naruto"

# def removeItem(someList, wrongItem):
  

# def greeting(name):
#   g = "Hello " + name + "!"
#   return g
# # Creating the function step
# def hello():
#   print("I am the hello function!")
# # Executing the function
# hello()

# # Create a function that prints "I am working!" , then execute the function (use it!)
# def kemlamb():
#   print("I am working")


# kemlamb()

# # Create a function that take one argument and prints the argument.

# def fooysal(argument):
  
#   print(argument)

# fooysal("This is the argument")



# def add2(a,b):
#   return a + b
# print(add2(91,10))
''''''''''''''''
Create two sets. In each set, add 5 different random numbers between 1 and 10. Then, print out these two sets, the union of these two sets, and the intersection of these two sets.
For your second random set, either print out "The number 1 is inside the second set" or "The number 1 is not inside the second set"
Ask the user for a word. Then, use a set to print out all of the unique letters in the word and the number of unique letters in the word.
Ask the user for another word. Print out the letters these two words have in common.
Write a function that takes in a set of numbers and returns a set with only the even numbers from that set.
Write a function that takes in a set of words and returns a set with only the words that have 3 letters in them.
'''''''''''''''
 
import random

list1 = []

for i in range(5):
  randomfishyonmi = random.randint(0,10)
  list1.append(randomfishyonmi)


list2 = []

for i in range(5):
  randomfishyonmi = random.randint(0,10)
  list2.append(randomfishyonmi)

print("list1", list1)
print("list2", list2)

# For each list that we created, create a set using set() function:


setlist1 = set(list1)
setlist2 = set(list2)

print("setlist1", setlist1)
print("setlist2", setlist2)

setUnion = setlist1.union(setlist2)
print("setUnion",setUnion)



# Homework:
# Create a set from each of the lists below:
listOne = ["apple", "orange", "grapes", "pomegrante", "banana", "apple", "grapes"]
listTwo = ["pineapple", "strawberries", "apple", "orange", "pineapple", "apple"]

# Using the two sets you made, create a union set by using the union() function like we did above.


# Create a function that takes a number as a string. Ex: "100"
# The function should print "Your lucky number is 100"! 
# Depending on the number used for the argument, it should print different lucky numbers. 

# Ex: luckyNum("1000") --> "Your lucky number is 1000"
# Ex: luckyNum("25") --> "Your lucky number is 25"


# arr = ['a', 'b', 'c', 'a', 'a', 'b']
# # To create aset,use the set() function
# setArr = set(arr)
# print(arr)
# print(setArr)
