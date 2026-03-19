from hhttp import HTTPStatus

from fastapi.testeclient import TestClient

from test_root_deve_retornar_ola_mundo():

#Arrange
    client = TestClient(app)
#Act    
    response = client.get('/')
#Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK