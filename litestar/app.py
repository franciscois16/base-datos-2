from litestar import Litestar , get
from dataclasses import dataclass
from litestar.exceptions import HTTPException

@dataclass
class TodoItem:
    id:int
    title:str
    done:bool

TODO_LIST:list[TodoItem]= [
    TodoItem(1,"comer empada",True),
    TodoItem(2,"tomar terremoto",True),
    TodoItem(3,"bailar cueca",False),
    TodoItem(4,"comer choripan",False),
    TodoItem(5,"terminar la tarea",False)
]

@get("/")
async def list_todos(done:bool | None = None) -> list[TodoItem]:
     if done is None:
          return TODO_LIST
     return[x for x in TODO_LIST if x.done == done] 
    
    # if done=="1":
    #     return[x for x in TODO_LIST if x.done]
    # elif done=="0":
    #     return[x for x in TODO_LIST if not x.done]
    # raise HTTPException(f"el parametro no es valido: {done!r}",status_code=400)

@get("/{todo_id:int}/")
async def get_todo(todo_id: int) -> TodoItem:
    for todo in TODO_LIST:
        if todo_id==todo_id:
            return todo
    raise HTTPException(f"TODO no encontrado",status_code=404) 

app = Litestar([list_todos,get_todo])