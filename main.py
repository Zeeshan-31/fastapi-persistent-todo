import json
import os 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
  name:str
  price: float
  is_offer:bool =None

@app.get("/")
def read_root():
  return {"message":"hello, world!"}

@app.get("items/{item_id}")
def read_item(item_id: int, q: str=None):
  return{"item_id":item_id,"query_param":q}

@app.post("/products/")
def create_product(product: Product):
  return {"message":f"product {product.name} created!","total_price":product.price}

@app.get("/sum")
def sum(num1 :int,num2:int =0):
  return{"sum":num1+num2}


#loading logic
if os.path.exists("task.json"):
  try:
    with open("task.json","r") as file:
      my_tasks = json.load(file)
  except json.JSONDecodeError:
    my_tasks= []
else:
  my_tasks = []

#saving //Helper function
def save_data():
  with open("task.json","w") as file:
    json.dump(my_tasks, file)

@app.post("/add-task")
def add_task(task:str):
  new_id = max([item["id"] for item in my_tasks],default=0) +1
  new_task = {"id":new_id, "name":task}
  my_tasks.append(new_task)
  save_data()
  return{"message":"task added","task": new_task}

@app.get("/task/{task_id}")
def get_task(task_id:int):
    for item in my_tasks:
      if item["id"] == task_id:
        return item
    return {"error":"Task Not Found"}  
        
@app.delete("/task/{task_id}")
def del_task(task_id:int):
  global my_tasks
  task_exists = any(item["id"] == task_id for item in my_tasks)

  if not task_exists:
    return {"error":"Task Not Found"}
  
  my_tasks = [item for item in my_tasks if item["id"] !=task_id]
  save_data()
  return {"message" : f"{task_id} deleted successfully"}

@app.put("/task/{task_id}")
def update_task(task_id:int,new_name:str):
  for item in my_tasks:
    if isinstance(item ,dict) and item.get("id") == task_id:
      item["name"] = new_name
      save_data()
      return {"message" : "updated successfully!","task":item}
  return {"error":"Task Not Found"}

@app.get("/tasks")
def get_all_tasks():
    # This simply returns the current state of your list
    return {"total_tasks": len(my_tasks), "tasks": my_tasks}