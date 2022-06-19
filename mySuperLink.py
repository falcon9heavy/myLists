"""
@author Chris Adams

Creating a linkedList that I've customized for full use in other programs when required.
Some key things needed are:

done:
    append(value) - add a new value to the end of the list
    count() - returns the total number of nodes in the list
    getVal(index) - returns the value at the index provided
    show_list() - get a read out of all node values
    insert(index,value) - add a value to specific index
    delete(value) - find that value/values and delete them ALL from index

to do:
    crypto() - cryptographically store/conceal the data stored in the node
    search(value) - determine if and how many times that value appears in the list

"""


class node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class linkedList:
    def __init__(self):
        self.head = node()

    # append a node to the linkedlist, pass the value to store in node

    def append(self, value):
        new_node = node(value)
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node

    # return the number of nodes in the linked list

# i think count is right for the wrong reason - fix it
    def count(self):
        num = 0
        current_node = self.head
        while current_node.next_node is not None:
            num += 1
            current_node = current_node.next_node
        return num

    # Show all LinkedList data elements in list format.

# i don't think this ever presents the last node - fix it
    def show_list(self):
        nodelist = []
        current_node = self.head
        while current_node.next_node is not None:
            nodelist.append(current_node.value)
            current_node = current_node.next_node
        print(nodelist)

    # the get() function returns the value of the node at a location (index)
    # which is the numeric link placement within LinkedList.
    # i.e. index=5 returns the value of the 5th node.

    def getVal(self, index) -> str:
        # ensure the index given is within range of our LL
        if index > self.count():
            return f'Your selection of {index} is out of range of this list'

        # start at the first index, the work our way down the line
        current_index = 0
        current_node = self.head
        while current_index < index:
            current_index += 1
            current_node = current_node.next_node
        return current_node.value

    # insert(index, value) places the value provided at the indexed location in the linkedList
    # location greater than 0

    def insert(self, index, value):
        if index > self.count():
            return f'Your selection of {index} is out of range of this list'

        # go to the indexed node, that is where we'll add the new node
        # and bump everything else down right by 1

        current_index = 0
        previous_node = self.head
        current_node = self.head

        while True:
            current_node = current_node.next_node
            if current_index == index:
                # do stuff to nodes, else
                new_node = node(value)
                new_node.next_node = current_node
                previous_node.next_node = new_node
                return
            previous_node = current_node
            current_index += 1

# test out  your linkedList

    # delete will remove all instances of the value passed yet leave
    # the linkedlist in 1 piece!

    # You need to see if this deals with first node deletion correctly

    # Deletes the node at index 'index'.
    def delete(self, index):
        if index >= self.length() or index < 0:  # added 'index<0' post-video
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

"""
    def delete(self,value):
        # start at the beginning of the list, then work your way right to the end
        current_node = self.head
        previous_node = self.head
        iterator = 0

        while True:
            if(current_node.value == value):
                #this condition should support if first value is equal to data set
                if current_node is self.head : # then we are dealing with first node
                    self.head = current_node.next_node
                    current_node = current_node.next_node
                    previous_node = self.head
                    continue
                previous_node.next_node = current_node.next_node


"""


ll = linkedList()
for var in range(5):
    print(var, end=',')
    ll.append(f'data_element_{var}')
ll.show_list()
print(ll.count())
#print(f'There are a total of {ll.count()} nodes')
#ll.insert(10,'tenth item')
#ll.show_list()


