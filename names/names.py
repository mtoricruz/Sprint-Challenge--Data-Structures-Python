import time
# import BST because we have to traverse through entire name files,
# not just search for names
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# initialize BST
name_nodes = BSTNode(names_1[0])

# Replace the nested for loops below with your improvements
# traverse through 1st name file 
for name_1 in names_1:
    # and add names to BST which is assigned name_nodes
    name_nodes.insert(name_1)

# traverse through 2nd name file 
for name_2 in names_2:
    # if name_nodes contains name_2 as well
    if name_nodes.contains(name_2):
        # add that name to the duplicates list [should be 64]
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
