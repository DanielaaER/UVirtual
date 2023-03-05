from fastapi import APIRouter
user = APIRouter()

@user.get("/users")
def helloworld():
    return "Hello world"


@user.get("/users")
def helloworld():
    return "Hello world"

