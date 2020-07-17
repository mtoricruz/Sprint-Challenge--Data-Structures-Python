# from queue import Queue
# from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if newnode < node.value
        if value < self.value:
        #    if left doesn't exist
            if self.left is None:
        #        create left
                self.left = BSTNode(value)
        #       else
            else:
        #           leftnode.insert(value)
                self.left.insert(value)
        #   if >=
        else:
        #       if right doesn't exist
            if self.right is None:
        #           create right
                self.right = BSTNode(value)
        #       else
            else:
        #           rightnode.insert(value)
                self.right.insert(value)

    def contains(self, target):
        # if node.value == findvalue
        if self.value == target:
        #   return true
            return True
        # else
        #   if find < node.value:
        if target < self.value:
            if self.left is None:
                return False
            else:
        #      contains on node.left
                return self.left.contains(target)
        #   else
        else:
            if self.right is None:
                return False
            else:
        #      contains on node.right:
                return self.right.contains(target)

    # Return the maximum value found in the tree
#     def get_max(self):
#         if self.right:
#             return self.right.get_max()
#         else:
#             return self.value

#     # Call the function `fn` on the value of each node
#     def for_each(self, fn):
#         fn(self.value)
#         if self.left:
#             self.left.for_each(fn)
#         if self.right:
#             self.right.for_each(fn)

#     # Part 2 -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self, node):
#         # P - Traverse BST on left side
#         # as long as a left side exist
#         # print root value
#         if self.left is not None:
#             self.left.in_order_print(node)
#         print(self.value)
#         if self.right is not None:
#             self.right.in_order_print(node)
         

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     def bft_print(self, node):
#         if node is None:
#             return
#         # P - Create queue
#         queue = Queue()
#         # add root to queue
#         queue.enqueue(node)
#         # while queue is not empty
#         while len(queue) > 0:
#             # node = pop head of queue
#             node = queue.dequeue()
#             # DO THE THING YOU NEED (in this case it is to print)
#             print(node.value)
#             # add children of node to queue
#             if node.left:
#                 queue.enqueue(node.left)
#             if node.right:
#                 queue.enqueue(node.right)

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self, node):
#         if node is None:
#             return
#         # P - Create stack
#         stack = Stack()
#         # add root to stack
#         stack.push(node)
#         # while stack is not empty
#         while len(stack) > 0:
#             # node = pop top off the stack
#             node = stack.pop()
#             # DO THE THING YOU NEED (in this case it is to print)
#             print(node.value)
#             # add children of node to stack
#             if node.left:
#                 stack.push(node.left)
#             if node.right:
#                 stack.push(node.right)
        

#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self, node):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self, node):
#         pass

# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# bst.bft_print(bst)
# bst.dft_print(bst)
# # print("elegant methods")
# # print("pre order")
# # bst.pre_order_dft(bst)
# # print("in order")
# # bst.in_order_dft(bst)
# # print("post order")
# # bst.post_order_dft(bst)
