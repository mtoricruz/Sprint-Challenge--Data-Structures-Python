class RingBuffer:
    # check test file for max cap
    def __init__(self, capacity=5):
        # initialize limit, start size, and storage 
        self.capacity = capacity
        self.size = 0
        self.order = [] 

    # U - append method adds given element to buffer
    def append(self, item):
        # check to see if length of list is at max capacity
        if len(self.order) == self.capacity:
            # if at max and wants to append, remove the first item in list
            # which is the oldest [using pop]
            self.order.pop(self.size)
            # insert the next item || insert item at given position of 0 
            self.order.insert(self.size, item)
            # 5 % 5 = 0 and that element is overwritten with newly stored data
            self.size = (self.size + 1) % self.capacity
        else:
            self.order.append(item)

    # U - get method returns all of the element in the buffer
    # in a list in their given order
    def get(self):
        # return the list
        return self.order

