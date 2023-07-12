from fastapi import FastAPI,Query,Path, Body
from enum import Enum
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

# @app.get("/",description="Thi is our fisrt route")
# async def root():
#     return {"Message":"Hello world"}


# @app.post("/")
# async def post():
#     return {"MEssage":"hello from the post route"}


# @app.put("/")
# async def put():
#     return {"Message":"hello from the put route"}


# @app.get("/users")
# async def list_items():
#     return {"Message":"list user route"}


# @app.get("/users/me")
# async def get_current_user():
#     return {"Message":"This is current user"}

# @app.get("/users/{user_id}")
# async def get_user(user_id:str):
#     return {"Message":user_id}

# class FoodEnum(str,Enum):
#     fruits='fruits'
#     vegetables='vegetables'
#     dairy='dairy'

# @app.get("/food/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {
#             "food_name":food_name,
#             "message":"you are healty"
#             }
    
#     if food_name.value == 'dairy':
#         return {
#             'food_name':food_name,
#             'message':'you are still healty but like sweet things'

#         }
#     return {'food_name':food_name,'message':'I like chocolate milk'}


# fake_item_db = [{'item_name':"Apple"},{'item_name':"Banana"},{'item_name':"Orange"},{'item_name':"Strawbery"},{'item_name':"Nutt"}]

# # @app.get("/items")
# # async def list_items(skip: int = 0, limit: int =10):
# #     return fake_item_db[skip:skip+limit]

# @app.get("/items/{item_id}")
# async def get_item(item_id:str, q: str or None = None,short: bool = False):
#     item = {"item_id":item_id}

#     if q:
#         item.update({"q":q})
    
#     if not short:
#         item.update(
#                 {
#                     "description":"Bu yerda description"
#                 }
#         )
#     return item

# @app.get("users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q: str or None = None, short: bool=False):
#     item = {"item_id":item_id,"owner_id":user_id}

#     if q:
#         item.update({"q":q})
    
#     if not short:
#         item.update(
#                 {
#                     "description":"Bu yerda description"
#                 }
#         )
#         return item
    
# class Item(BaseModel):
#     name : str 
#     description : str or None = None
#     price : float 
#     tax : float or None =None
    
# @app.post("/items")
# async def create_item(item:Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id:int,item:Item, q: str or None = None):
#     result = {"item_id":item_id,**item.dict()}
#     if q: 
#         result.update({"q":q})
#     return result 

 

# @app.get('/items')
# async def read_items(
#     q:list[str] or None = Query(None,max_length=10,title="Samle query",alias='item-query')
#     ):
#     results = {'items':[{'item_id':'Foo'},{'item_id':'Bar'}]}
#     if q:
#         results.update({'q':q})
#     return results

# @app.get('/items_hidden')
# async def hideen_query_route(hidden_query: str or None = Query(None,include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query":hidden_query}
#     return hidden_query

# @app.get('/items_validation/{item_id}')   
# async def read_items_validation(
#     *,
#     item_id : int = Path(...,title='The ID of the item to get',gt=12,le=100),
#     q: str or None = Query(None),
#     size : float =Query(...,gt=0,le=7.75)
     
# ):    
#     results = {'item_id':item_id,'size':size}
#     if q: 
#         results.update({'q':q})
#     return results
    
    


""""
Part 7 - > Body - Multiple paramerts
"""
class Item(BaseModel):
    name: str
    description : str or None = None
    price : float
    tax : float or None = None

@app.put('/items/{item_id}')
def update_item(
    *,
    item_id : int = Path(...,title="The  ID of the item to get",ge=0,le=150),
    q: str or None = None,
    item : Item = Body(...)
):
    results = {'item_id':item_id}
    if q:
        results.update({'q':q})
    if item:
        results.update({'item':item})
    return results
