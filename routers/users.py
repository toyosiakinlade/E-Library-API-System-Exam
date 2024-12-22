from fastapi import APIRouter, status
from services.users import user_crud, UserCrud
from schemas.users import UserCreate, UserUpdate

user_router = APIRouter()


@user_router.get("/")
def get_users():
    user = user_crud.get_users()
    return user

@user_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_users(id: int):
    user = user_crud.get_users(id)
    return user

@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(payload:UserCreate):
    new_user = user_crud.create_user(payload)
    return new_user

@user_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_user(id: int, payload:UserCreate):
    user = user_crud.get_user(id)
    update_user = user_crud.update_user(user=user, data=payload)
    return {"message": "success",'data': update_user}

@user_router.patch("/{id}", status_code=status.HTTP_200_OK)
def part_update_user(id:int, payload:UserUpdate):
    user =  user_crud.get_user(id)
    part_update_user = user_crud.part_update_user(user=user, data=payload)
    return part_update_user

@user_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int):
    user_crud.delete_user(id)