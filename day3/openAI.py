# define a function to compute the priority of a character
def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

# read the input from a file named "input.txt"
with open("input.txt") as f:
    input = f.read().strip().split("\n")

# initialize the sum of priorities to 0
sum_of_priorities = 0

# loop through the list of rucksacks
for rucksack in input:
    # split the rucksack into two compartments
    comp1 = rucksack[:len(rucksack) // 2]
    comp2 = rucksack[len(rucksack) // 2:]

    # create sets for each compartment
    set1 = set(comp1)
    set2 = set(comp2)

    # find the intersection of the two sets
    intersection = set1 & set2

    # loop through the intersection and add the priorities to the sum
    for c in intersection:
        sum_of_priorities += priority(c)

# print the sum of priorities
print(sum_of_priorities)
