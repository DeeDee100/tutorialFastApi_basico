from fastapi import FastAPI

app = FastAPI()

TAREFAS = [
		{
		"id": "1",
		"titulo": "Familia Addams(2019)",
		"descrição": "Animação",
		"estado": "Finalizado",
	},
	{
		"id": "2",
		"titulo": "V de Vingança (2005)",
		"descrição": "Na luta pela liberdade, um vigilante, conhecido apenas como V, utiliza-se de táticas terroristas para enfrentar os opressores da sociedade.",
		"estado": "Finalizado",
	},
	{
		"id": "3",
		"titulo": "US (2019)",
		"descrição": "clone assassino",
		"estado": "não finalizado",
	},
]

@app.get("/tarefas")
def listar():
	return TAREFAS