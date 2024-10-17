from fastapi import FastAPI, HTTPException
from model import linked_list
from model.linked_list import LinkedList, Child
from pydantic import BaseModel

class ChildSchema(BaseModel):
    id : str
    name: str
    age: int
    gender: str
app = FastAPI()
linked_list = LinkedList()

@app.post("/children/beginning")
def add_child_at_start(child: ChildSchema):
    linked_list.insertBeginning(Child(**child.dict()))
    return {'message': 'Child add the beginning '}

@app.post('/children/{position}')
def add_child_at_position(position: int, child: ChildSchema):
    try:
        linked_list.list.insertBeginning(Child(**child.dict),position)
        return {'message': f'child added at position {position}'}

@app.put('/children/reverse')
def reverse_list():
    linked_list.invert_list()
    return {'message':'list reversed'}
@app.delete('/children/id/{id}')
def delete_child_by_id(id:str):
    try:
        linked_list.deleteID(id)
        return {'message': f'child deleted with id: {id}'}


@app.delete('/children/position/{position}')
def delete_child_position(position: int):
    try:
        linked_list.deletePosition(position)
        return {'message': f'child deleted at position: {position}'}

@app.put('/children/swap-ends')
def swap_ends():
    linked_list.swapEnds()
    return {'message': 'ends swapped'}

@app.put('/children/alternate-gender')
def alternate_by_gender():
    linked_list.alternateByGender()
    return {'message': 'genders alternated'}

@app.get('/children')
def print_list():
    list = []
    current = linked_list.head
    while current != None:
        list.append({'name' : current.child.name,
                     'id' : current.child.id,
                     'age': current.child.age,
                     'gender': current.child.gender
                     }
        )
        current = current.next

    return {'children': list}



