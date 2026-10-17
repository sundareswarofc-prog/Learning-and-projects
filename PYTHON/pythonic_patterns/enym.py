fruits = ["apple", "banana", "cherry"]

########################################### enumerate #################################################
# Non-Pythonic
i = 0
for f in fruits:
    print(i, f)
    i += 1

### for normal loops in python we dont have a index value

#### it used to maipulate the array using index  #######
for i,data in enumerate(fruits):
    print(i,data)


# we can also control the start index value
for i,data in enumerate(fruits,start=1):
    print(i,data)

######################################### ZIP ###########################################

# using these we can loop throug sequesnce of aray by getting pyhon dictionaries

names = ["Asha", "Ravi", "Meena"]
scores = [90, 85, 92]

for name, score in zip(names, scores):
    print(name, score)

# Build a dictionary
dict(zip(names, scores))   # {'Asha': 90, 'Ravi': 85, 'Meena': 92}


##############################################################################################


x, y = (10, 20)            # x=10, y=20
a, b = b, a                # swap without a temp variable

first, *rest = [1, 2, 3, 4]    # first=1, rest=[2, 3, 4]
*head, last = [1, 2, 3, 4]     # head=[1, 2, 3], last=4
first, *middle, last = [1, 2, 3, 4, 5]   # middle=[2, 3, 4]


################################# any and All #####################################

nums = [3, 8, 12, 5]

any(n > 10 for n in nums)    # True  (12 qualifies)
all(n > 0 for n in nums)     # True  (all positive)
all(n > 5 for n in nums)     # False (3 and 5 fail)


############################## sorted ###################################

nums = [5, 2, 9, 1]
sorted(nums)                  # [1, 2, 5, 9]
sorted(nums, reverse=True)    # [9, 5, 2, 1]

words = ["banana", "kiwi", "apple"]
sorted(words, key=len)        # ['kiwi', 'apple', 'banana']

people = [("Asha", 30), ("Ravi", 25)]
sorted(people, key=lambda p: p[1])   # sort by age


############################ min and max ##################################
min([4, 1, 7])    # 1
max([4, 1, 7])    # 7

words = ["banana", "kiwi", "apple"]
max(words, key=len)     # 'banana'
min(words, key=len)     # 'kiwi'

max([], default=0)      # avoids an error on empty input