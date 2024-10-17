
class Node:
    def __init__(self,child):
        self.child = child
        self.next = None
class Child:
    def __init__(self, id:str, name:str, age:int,gender:str ):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head == None:
            return 'no elements'
        else:
            tmp = self.head
            while tmp != None:
                print(f'name:{tmp.child.name},id:{tmp.child.id},age:{tmp.child.age},gender:{tmp.child.gender}')
                tmp = tmp.next


    def insertBeginning(self, child):
        newNode = Node(child)
        newNode.next = self.head
        self.head = newNode
    def invertList(self):
        if self.head == None or self.head.next == None :
            return 'empty list or with one element in it'
        prev = None
        current = self.head

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def insertPosition(self,child,position):
        newNode = Node(child)
        if position == 1:
            self.insertBeginning(child)

        tmp = self.head
        count  = 1
        while tmp != None:

            if count == position-1:
                newNode.next = tmp.next
                tmp.next = newNode
            tmp = tmp.next
            count +=1
        if position > count:
            raise Exception('the entered value is greater than the number of elements in the list')
    def deleteID(self,ide):
        tmp = self.head
        if self.head.child.id == ide:
            self.head = tmp.next
        else:

            while tmp.next != None:
                if tmp.next.child.id == ide:
                    tmp.next = tmp.next.next
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

    def swapEnds(self):
        if self.head == None or self.head.next ==None:
            return 'empty list or with one node in it'

        first = self.head
        prev = None
        current = self.head

        while current.next != None:
            prev = current
            current = current.next


        prev.next = first
        current.next = first.next
        prev.next.next = None
        self.head = current
    def alternateByGender(self):
        #must add the length attribute and incorporate in each method
        '''if self.length <= 2:
            return 'son menos de dos no se pueden mezclar'''

        boys = LinkedList()
        girls = LinkedList()

        tmp = self.head
        while tmp:
            if tmp.child.gender.upper() == 'M':
                boys.insert(tmp.child)

            else:
                girls.insert(tmp.child)

            tmp = tmp.next

        self.head = None
        self.length = 0

        boyNode = boys.head
        girlNode = girls.head

        while boyNode or girlNode:
            if boyNode:
                self.insert(boyNode.child)
                boyNode = boyNode.next

            if girlNode:
                self.insert(girlNode.child)
                girlNode = girlNode.next

    def insert(self,child):
        newNode = Node(child)
        if self.head is None:
            self.head = newNode
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = newNode




if __name__ == '__main__':
    child1 = Child('1','juana',15,'F')
    child2 = Child('2','marlon',23,'M')
    child3 = Child('3','pedro',20,'M')
    listSE = LinkedList()
    print('list.insertBeginning')
    listSE.insertBeginning(child1)
    listSE.insertBeginning(child2)
    listSE.insertBeginning(child3)
    listSE.printList()
    child4 = Child('4','johana',20,'F')
    print('--------list.insertPosition-------')
    listSE.insertPosition(child4,3)
    listSE.printList()

    listSE.printList()
    print('------------list.invertList----------')
    listSE.invertList()
    listSE.printList()
    print('------------list.deleteID------------')
    listSE.deleteID('1')
    listSE.printList()
    print('------------list.deletePosition------')
    listSE.deletePosition(3)
    listSE.printList()
    print('------------list.swapEnds------------')
    listSE.swapEnds()
    listSE.printList()

    print('------------adding child to the list---')
    child5 = Child('5','carlos',13,'M')
    listSE.insertPosition(child5,3)
    listSE.printList()
    print('------------list.swapEnds------------')
    listSE.swapEnds()
    listSE.printList()
    print('-----------adding more children to the list------')
    child6 = Child('6','mariana',20,'M')
    child7 = Child('7','sara',12,'M')
    child8 = Child('8','maria',15,'F')
    child9 = Child('9','estefania',20,'F')
    listSE.insertPosition(child6,4)
    listSE.insertPosition(child7,5)
    listSE.insertPosition(child8, 6)
    listSE.insertPosition(child9, 7)
    listSE.printList()
    print('--------------listSE.insert---------')
    child10 = Child('10','karen',10,'F')
    listSE.insert(child10)
    listSE.printList()
    print('-----------listSE.altenateByGender----------')
    listSE.alternateByGender()
    listSE.printList()





















