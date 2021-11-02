from fastapi.testclient import TestClient
from fastapi import status
from starlette.status import HTTP_201_CREATED
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

def test_aceitar_post():
	client = TestClient(app)
	response = client.post("/tarefas")
	assert response.status_code != status.HTTP_405_METHOD_NOT_ALLOWED
	TAREFAS.clear()

def test_tarefa_deve_ter_titulo():
	client = TestClient(app)
	response = client.post("/tarefas", json={})
	assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
	TAREFAS.clear()

def test_tarefa_deve_ter_descricao():
	client = TestClient(app)
	response = client.post("/tarefas", json={"titulo": "Addams"})
	assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
	TAREFAS.clear()

def test_tarefa_deve_ter_descricao_min_5_caracteres():
	client = TestClient(app)
	response = client.post("/tarefas", json={"titulo": "Addams", "descricao":"A"})
	assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
	TAREFAS.clear()

# def test_tarefa_deve_ter_estado():
# 	client = TestClient(app)
# 	response = client.post("/tarefas", json={"titulo": "Addams", "descricao":"A121223"})
# 	assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_criar_tarefa_retorna_tarefa():
	client = TestClient(app)
	tarefa = {"titulo": "Nancy Drew", "descricao":"A121223"}
	response = client.post("/tarefas", json=tarefa)
	nova_response = dict(response.json())
	nova_response.pop("id")
	nova_response.pop("estado")
	assert nova_response == tarefa
	TAREFAS.clear()

def test_quando_criar_uma_tarefa_seu_id_deve_ser_unico():
	cliente = TestClient(app)
	tarefa1 = {"titulo": "titulo1", "descricao": "descricao1"}
	tarefa2 = {"titulo": "titulo2", "descricao": "descricao1"}
	resposta1 = cliente.post("/tarefas", json=tarefa1)
	resposta2 = cliente.post("/tarefas", json=tarefa2)
	assert resposta1.json()["id"] != resposta2.json()["id"]
	TAREFAS.clear()

def test_tarefa_criada_estado_padrao_naoFinalizado():
	client = TestClient(app)
	tarefa = {"titulo": "Nancy Drew", "descricao":"A121223"}
	response = client.post("/tarefas", json=tarefa)
	assert response.json()["estado"] == "Nao Finalizado"
	TAREFAS.clear()

def test_POST_codigo_retorno_201():
	client = TestClient(app)
	tarefa = {"titulo": "Nancy Drew", "descricao":"descricao"}
	response = client.post("/tarefas", json=tarefa)
	assert response.status_code == HTTP_201_CREATED
	TAREFAS.clear()

def test_salvar_ao_criar():
	client = TestClient(app)
	tarefa = {"titulo": "Nancy Drew", "descricao":"descricao"}
	response = client.post("/tarefas", json=tarefa)
	assert response.status_code == 201
	assert len(TAREFAS) == 1
	TAREFAS.clear()

