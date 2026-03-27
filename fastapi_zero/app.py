from http import HTTPStatus

from fastapi_zero.routers import auth, users
from fastapi_zero.schemas import Message
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
