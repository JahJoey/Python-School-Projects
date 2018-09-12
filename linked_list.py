#
# Joseph Hein
# CS3060 T/TH 13:00
# Assignment: Linked List   | Due : MOVED 3/23
#


class node :
    def __init__(self, item, prev = None, next = None) : 
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self) :
        return str(self.item)

    def __repr__(self) :
        return repr(self.item)


## linked_list
# Implements a doubly-linked list ADT
# @invariant (len == 0 and head == None and tail == None)
#         or (len != 0 and head != None and tail != None and head.prev == None and tail.next == None)
# You do not have to call your data members head/tail, but should be descriptive names
class linked_list :

    class iterator:

        def __init__(self, linked_list) :
            self.linked_list = linked_list
            self.current = self.linked_list.head

        def __next__(self):
            if self.current == None :
                raise StopIteration

            item = self.current
            self.current = self.current.next
            return item

            
    ## constructor - iterable is an iterable object that initializes
    #  the linked_list in the order iterable is traversed
    def __init__(self, iterable = []) :
        self.head = None
        self.tail = None
        self.size = 0
        for i in iterable:
            self.push_back(i)

    ## constant time access to first/last node, respectively
    #  @returns the first/last node, respectively
    def front(self) : 
        return self.head

    def back(self) :
        return self.tail

    ## constant time insertion of a data item (any element)
    #  as the first/last (respectively) element 
    def push_front(self, item) :
        if self.head == None:
            new_node = node(item)
            self.head = new_node
            self.tail = new_node
            self.size = self.__len__()
        else: 
            new_node = node(item)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size = self.__len__()

    def push_back(self, item) : 
        if self.tail == None:
            new_node = node(item)
            self.tail = new_node
            self.head = new_node
            self.size = self.__len__()
        else:
            new_node = node(item)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size = self.__len__()


    ## constant time removal of the first/last (respectively) node/item
    #  @returns the item (not the node)
    def pop_front(self) :
        if self.head == None:
            return None
        else:
            self.current = self.head
            if self.head == self.tail:
                item = self.head.item
                self.head = None
                self.tail = None
                del self.current
            else:
                item = self.head.item
                self.head = self.head.next
                del self.current
                
            self.size = self.__len__()
            return item



    def pop_back(self) :
        if self.tail == None:
            return None
        else:
            self.current = self.tail
            if self.head == self.tail:
                item = self.tail.item
                self.tail = None
                self.head = None
                del self.current
            else:
                item = self.tail.item
                self.tail = self.tail.prev
                del self.current
                
            self.size = self.__len__()
            return item

    ## Turns list into a string representation.
    #  Strings prints identical to how 
    #  it would if it were a Python list
    #  @returns the string representation 
    def __str__(self) :
        current = self.head
        restr = '['
        while current != None:
            restr += str(current.item)
            current = current.next
            if current != None:
                restr += ", "
        restr += ']'
        return restr[:]

    ## Provides an iterator over an instance of the linked list
    #  iterator is a separate class (either external or inner)
    #  that iterates from first to last.
    # __next__ returns a node
    #  @returns an iterator
    def __iter__(self) :
        return linked_list.iterator(self)

    ## Generator function to iterate over the linked list from last to first.
    #  Generates nodes.
    def __reversed__(self) :
        current = self.tail
        self.size = self.__len__() # To make sure the correct size is reported
        for i in reversed(range(self.size)) :
            item = current
            current = current.prev
            yield item
            

    ## converts linked list to a bool
    #  @returns False if empty, True otherwise
    def __bool__(self) :
        assert isinstance(self, linked_list)

        if self.size == 0:
            return False
        elif self.size > 0:
            return True


    ## Computes length of linked list
    #  @returns the length of the linked list 
    def __len__(self) :
        current = self.head
        self.size = 0
        while current != None:
            self.size += 1
            current = current.next
        return self.size

    ## implements Python sequence-style equality and less-then 
    #  (on the items held and not the nodes), respectively
    #  Ensures other is another linked list, if noS assertion fail
    #  @returns True if equal/less-than, False otherwise
    def __eq__(self, other) : 
        assert isinstance(other, linked_list)
        current = self.head
        othercur = other.head
        if self.size != other.size:
            return False
        elif self.size == 0 and other.size == 0:
            return True
        elif current == None:
            return True

        while current != None:
            if current.item != othercur.item:
                return False
            current = current.next
            othercur = othercur.next

        return True


    def __lt__(self, other) :
        assert isinstance(other, linked_list)

        self.current = self.head
        other.current = other.head
        ls_one = []
        ls_two = []

        while self.current != None:
            ls_one.append(self.current.item)
            self.current = self.current.next
        while other.current != None:
            ls_two.append(other.current.item)
            other.current = other.current.next

        if len(ls_one) == 0 and len(ls_two) == 0:
            return False
        elif len(ls_one) == 0 and len(ls_two) > 0:
            return True
        elif ls_one < ls_two:
            return True
        else:
            return False

    ## implements in operator
    #  @returns True if item is in linked-list, False otherwise
    def __contains__(self, item) : 
        current = self.head
        ls = []
        while current != None:
            ls.append(current.item)
            current = current.next

        if item in ls:
            return True
        else:
            return False
            




    ## insert_after and remove are extra credit (5 points)
    #  All or nothing, linked-list must function perfectly to be elligible
    #  No partial credit

    ## constant time insertion of the data item (any element) after node
    #  @pre (precondition) node is in the linked list (self)
    def insert_after(self, after_insert, item) : # NOT PROPERLY PASSING ALL TESTS
        if self.__contains__(after_insert) == True:
            self.current = self.head
            while self.current.item != after_insert:
                self.current = self.current.next
            if self.current == self.tail:
                self.push_back(item)
            elif self.current == self.head:
                new_node = node(item)
                self.hold = self.current.next
                self.backtrack = self.current
                self.current.next = new_node
                self.current = self.current.next
                self.current.next = self.hold
                self.current.prev = self.backtrack
                self.hold.prev = self.current
                self.size = self.__len__()
            else:
                new_node = node(item)
                self.hold = self.current.next
                self.backtrack = self.current
                self.current.next = new_node
                self.current = self.current.next
                self.current.prev = self.backtrack
                self.current.next = self.hold
                self.hold.prev = self.current
                self.size = self.__len__()



    ## constant time removal of node from the linked list (self)
    #  @pre (precondition) node is in the linked list (self)
    def remove(self, node) :  # NOT PROPERLY PASSING ALL TESTS
        if self.__contains__(node) == True:
            self.current = self.head
            while self.current.item != node:
                self.current = self.current.next
            if self.current == self.tail:
                self.delete = self.tail
                self.current = self.current.prev
                self.current.next = None
                self.tail = self.current
                self.size = self.__len__()
                del self.hold
            elif self.current == self.head:
                self.delete = self.head
                self.current = self.current.next
                self.current.prev = None
                self.head = self.current
                self.size = self.__len__()
                del self.delete
            else:
                self.delete = self.current
                self.hold = self.current
                self.current = self.current.prev
                self.hold.prev = None
                self.hold = self.hold.next
                self.hold.prev = self.current
                self.current.next = self.hold
                self.size = self.__len__()
                del self.delete
