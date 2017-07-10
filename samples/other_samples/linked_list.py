# encoding:utf-8


class NodeException(Exception): 
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class LinkedListError(Exception): 
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return  str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.__last_index = 0
        self.__cnt = 0

    def __len__(self):
        if self.head == None:
            rtn = 0
        else:
            rtn = self.__last_index + 1
        return rtn

    def __repr__(self):
        elements = []
        for n in range(len(self)):
            elements.append(str(self[n].data))
        return  '[' + ', '.join(elements) + ']'

    def __str__(self):
        return self.__repr__()

    def is_empty(self):
        return self.head == None

    def add(self, node):
        if not isinstance(node, Node):
            raise NodeException('must add a Node')
        if self.is_empty():
            self.head = node
        else:
            last_node = self[self.__last_index]
            last_node.next = node
            self.__last_index += 1

    def __getitem__(self, index):
        if index < 0 or index > len(self):
            raise LinkedListError('index out of range')
        if self.is_empty():
            print 'list is empty'
        elif index == 0:
            return self.head
        else:
            for n in range(1, index+1):
                if n == 1:
                    node = self.head.next
                else:
                    node = node.next
            return node

    def __iter__(self):
        return self

    def next(self):
        
        if self.__cnt >= len(self):
            raise StopIteration()
        rtn = self[self.__cnt]
        self.__cnt += 1
        return rtn


    def remove(self, index):
        if index < 0 or index > len(self):
            raise LinkedListError('index out of range')
        if index == 0:
            next = self.head.next
            self.head = next
        else:
            self[index-1].next = self[index+1] 

        self.__last_index -= 1

    def insert(self, node, index):
        if index == 0:
            node.next = self.head
            self.head = node
        elif index == self.__last_index + 1:
            self[self.__last_index].next = node
        else:
            node.next = self[index]
            self[index-1].next = node
            
        self.__last_index += 1


def __test():
    a = LinkedList()
    print 'length after init: {}'.format(len(a))
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    a.add(n1)
    print 'length after add: {}'.format(len(a))
    a.add(n2)
    print 'length after add: {}'.format(len(a))
    a.add(n3)
    print a
    print 'length after add: {}'.format(len(a))
    a.remove(2)
    print 'length after remove: {}'.format(len(a))
    print a
    n4 = Node('insert0')
    a.insert(n4,0)
    n5 = Node('insert_to_end')
    a.insert(n5, len(a))
    print a, len(a)
    n6 = Node('insert_middle')
    a.insert(n6, 2)
    print a, len(a)
    n7 = Node('add again')
    a.add(n7)
    print a, len(a)
    
    for n in a:
        print 'test iterator ----- {}'.format(n)

if __name__ == '__main__':
    __test()


