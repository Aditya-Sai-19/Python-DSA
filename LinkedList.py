class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class LinkedList:
    #creating empty linkedlist
    def __init__(self):
        self.head = None
        # to track the number of nodes we use n currently set to zero
        self.n = 0

    #To track the length of the LL
    def __len__(self):
        return self.n

    #To create new nodes and insert at head
    def insert_head(self,value):

        #create new node
        new_node = Node(value)

        #create connection
        new_node.next = self.head

        #reassign head
        self.head = new_node

        #increament n (since new node is added)
        self.n +=1

    def __str__(self):

        current = self.head

        result = ''

        while current != None:
            result = result + str(current.data) + '->'
            current = current.next
        
        return result[:-2]

    def insert_tail(self,value):

        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n += 1

        else:
            current = self.head


            #traverse until you find the tail node
            while current.next != None:
                current = current.next

            # add the new node to the tail
            current.next = new_node
            self.n += 1



l = LinkedList()

# l.insert_head(12)
l.insert_head([1,3])
print(l)
print(len(l))


