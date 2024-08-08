from fastapi import APIRouter,Depends,Header
from sqlalchemy.orm import Session
from database import get_db
from typing import Annotated
from service import user as UserService
from dto import user as UserDTO

router = APIRouter()

@router.post("/",tags=['user'])
async def create_user(data:UserDTO.User = None,db:Session=Depends(get_db),x_token:Annotated[list[str] | None,Header()]=None):
    if 'Salohiddin1' in x_token:
        return UserService.create_user(data,db)
    else:
        return {"api_key":"Not found api key"}


@router.get("/",tags=['user'])
async def get_all(db:Session=Depends(get_db)):
    return UserService.get_all_users(db)

@router.get("/{id}",tags=['user'])
async def get(id:str=None,db:Session=Depends(get_db)):
    return UserService.get_user(id,db)

@router.put('/{id}',tags=['user'])
async def update(id:int = None,data:UserDTO.User=None,db:Session=Depends(get_db),x_token:Annotated[list[str] | None,Header()]=None):
    if 'Salohiddin1' in x_token:
        return UserService.update(data,db,id)
    else:
        return {"api_key":"Not found api key"}
    
@router.delete('/{id}',tags=['user'])
async def delete(id:int=None,db:Session=Depends(get_db),x_token:Annotated[list[str] | None,Header()]=None):
    if 'Salohiddin1' in x_token:
        return UserService.remove(db,id)
    else:
        return {"api_key":"Not found api key"}