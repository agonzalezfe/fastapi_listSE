from model.linked_list import LinkedList,Child


class ChildController:
    def __init__(self):
        self.list = LinkedList()

    def add_child_at_start(self,child_data):
        child = Child(id=child_data['id'],name=child_data['name'],age=child_data['age'],
                      gender=child_data['gender'])
        self.list.insertBeggining(child)

    def add_child_at_position(self,child_data,position):
        child = Child(id=child_data['id'], name=child_data['name'], age=child_data['age'],
                      gender=child_data['gender'])
        self.list.insertPosition(child)

    def reverse_list(self):
        self.list.invertList()

    def delete_child_by_position(self,position):
        self.list.deletePosition(position)

    def swapEnds(self):
        self.list.swapEnds()

    def alternate_by_gender(self):
        self.list.alternateByGender()



    def print_list(self):
        self.list.printList()








