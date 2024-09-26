from linked_list import Child
from linked_list import LinkedList
from linked_list import Node

class NodeDLL(Node):
    def __init__(self,child):
        super().__init__(child)
        self.prev = None


    def __str__(self):
        return f'{self.prev} <- {self.child} -> {self.next}'


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None
        self.length = 0
    def append(self,child):
        newNode = NodeDLL(child)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
    def __str__(self):
        tmp = self.head
        result = ''
        while tmp:
            result += str(tmp.child.name)
            if tmp.next:
                result += ' <-> '
            tmp = tmp.next
        return result

    def prepend(self,child):
        newNode = NodeDLL(child)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length +=1
    def invert(self):
        current = self.head
        tmp = None
        while current:
            tmp = current.prev
            current.prev = current.next
            current.next = tmp
            current = current.prev

        if tmp:
            self.tail = self.head
            self.head = tmp.prev

    def deleteID(self,ide):
        tmp = self.head
        if self.head.child.id == ide:
            self.head = tmp.next
        if self.tail.child.id == ide:
            self.tail = self.tail.prev
            self.tail.next = None
        else:

            while tmp.next != None:
                if tmp.next.child.id == ide:
                    tmp.next = tmp.next.next
                    tmp.next.next.prev = tmp
                    self.length -=1
                    return f'the {ide} was deleted'
                tmp = tmp.next


    def deletePosition(self,position):
        if self.head == None:
            return 'empty list'
        if position == 1:
            self.head = self.head.next


        else:
            count = 1
            tmp = self.head
            while count < position - 1:
                tmp = tmp.next
                count +=1
            tmp.next = tmp.next.next
            tmp.next.next.prev = tmp
            self.length -=1



    def add_in_position(self, child, position):
        newNode = NodeDLL(child)
        if position == 1:
            self.insertBeginning(child)

        '''if position > self.length+1:
            raise Exception('the entered value is greater than the number of elements')'''
        tmp = self.head
        count = 1
        while tmp != None:

            if count == position - 1:
                newNode.next = tmp.next
                tmp.next = newNode
            tmp = tmp.next
            count += 1



        self.length += 1

    def mix_by_gender(self):
        if self.length > 2:
            pos_b = 1
            pos_g = 2
            list_cp = DoublyLinkedList()
            temp = self.head


            while temp is not None:

                if temp.child.gender.upper() == 'F':
                    list_cp.add_in_position(temp.child, pos_g)
                    pos_g += 2
                else:
                    list_cp.add_in_position(temp.child, pos_b)
                    pos_b += 2
                temp = temp.next


            self.head = list_cp.head





if __name__ == '__main__':
    child0 = Child('0','unnamed',0,'M')
    node1 = NodeDLL(child0)
    print(node1)
    dll = DoublyLinkedList()
    print('-------appendAtTheEnd--------')
    child1 = Child('1', 'juana', 15, 'F')
    child2 = Child('2', 'marlon', 23, 'M')
    dll.append(child1)
    dll.append(child2)
    print(dll)
    print('--------appendAtTheBeginning----')
    child3 = Child('3', 'pedro', 20, 'M')
    dll.prepend(child3)
    print(dll)
    print('---------reverseList------')
    dll.invert()
    print(dll)
    print('---------deleteID----------')
    child4 = Child('4','johana',20,'F')
    dll.append(child4)
    print(dll)
    dll.deleteID('2')
    print(dll)
    print('---------deletePosition-------')
    print(dll)
    dll.deletePosition(1)
    print(dll)
    print('---------mixByGenders--------')
    child6 = Child('6', 'mario', 20, 'M')
    child7 = Child('7', 'samuel', 12, 'M')
    child8 = Child('8', 'maria', 15, 'F')
    child9 = Child('9', 'estefania', 20, 'F')
    dll.append(child6)
    dll.append(child7)
    dll.append(child8)
    dll.append(child9)
    print(dll)
    dll.mix_by_gender()
    print(dll)
