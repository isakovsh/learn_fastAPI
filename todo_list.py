from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI(title="Todo List")

class Item(BaseModel):
    name : str 
    due_date : int 
    description : str or None = None
todo = []

@app.get('/')
def main_root():
    return "Project is health"


@app.get('/todo')
async def get_todo():
    return {'todo':todo}

@app.get('/todo/{id}')
async def get_todo(id:int):
    return {'todo':todo[id]}

@app.post('/add_todo')
async def add_todo(item:Item):
    todo.append(item)
    return "Added new todo"

@app.put('/update_todo/')
async def update(id: int,new_item:Item):
    try:
        todo[id] = new_item
        return "Updated todo"
    except:
        raise HTTPException(status_code=404,detail="Todo not find")
    
@app.delete('/delete_todo')
async def delete(id:int):
    try:
        todo.pop(id)
        return "deleted todo"
    except:
        raise HTTPException(status_code=404,detail="Todo not find")



