from fastapi import FastAPI
from http import HTTPStatus

from fastapi_zero.schemas import Message
app = FastAPI(title='Minha API BALA! cae')


@app.get(
    '/', 
    status_code=HTTPStatus.OK,
    response_model=Message
    )
def read_root():
    return {'message': 'Olá mundo!'}
