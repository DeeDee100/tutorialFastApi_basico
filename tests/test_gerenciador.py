from fastapi.testclient import TestClient
from fastapi import status
from gerenciador_tarefas.gerenciador import app, TAREFAS

def test_lista_tarefas_retorno_200():
	client = TestClient(app)
	response = client.get("/tarefas")
	assert response.status_code == status.HTTP_200_OK

def test_lista_tarefa_formato_json():
	client = TestClient(app)
	response = client.get("/tarefas")
	assert response.headers['Content-Type'] == "application/json"

def test_listar_tarefa_retorno_como_lista():
	client = TestClient(app)
	response = client.get("/tarefas")
	assert isinstance(response.json(), list)

def test_listar_tarefa_retornada_id():
	TAREFAS.append({"id": 1})
	client = TestClient(app)
	response = client.get("/tarefas")
	assert "id" in response.json().pop()
	TAREFAS.clear()

def test_listar_tarefa_retornada_titulo():
	TAREFAS.append({"titulo": "Familia Addams"})
	client = TestClient(app)
	response = client.get("/tarefas")
	assert "titulo" in response.json().pop()
	TAREFAS.clear()

def test_listar_tarefa_retornada_descricao():
	TAREFAS.append({"descricao": "descricao1"})
	client = TestClient(app)
	response = client.get("/tarefas")
	assert "descricao" in response.json().pop()
	TAREFAS.clear()

def test_listar_tarefa_retornada_estado():
	TAREFAS.append({"estado": "Finalizado"})
	client = TestClient(app)
	response = client.get("/tarefas")
	assert "estado" in response.json().pop()
	TAREFAS.clear()
