"""
@author Chris Adams

Creating a linkedList that I've customized for full use in other programs when required.
Some key things needed are:

    append(value) - add a new value to the end of the list
    count() - returns the total number of nodes in the list
    get(index) - returns the value at the index provided
    show_list() - get a read out of all node values

    to do:
    insert(index,value) - add a value to specific index
    crypto() - cryptographically store/conceal the data stored in the node
    delete(value) = find that value/values and delete from index
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

    def count(self):
        num = 0
        current_node = self.head
        while current_node.next_node is not None:
            num += 1
            current_node = current_node.next_node
        return num

    # Show all LinkedList data elements in list format.

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

    def get(self, index) -> str:
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

# test out  your linkedList


ll = linkedList()
for var in range(51):
    ll.append(f'data_element_{var}')
ll.show_list()
print(f'There are a total of {ll.count()} nodes')
print(f'{ll.get(51)} is the value at index provided.')
# add code for deletion next...