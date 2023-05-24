   Este projeto visa analisar os possíveis caminhos críticos (CPM) das disciplinas do curso Ciência da Computação UnB-2023. Para isto é construído um grafo direcionado acíclico (DAG) das disciplinas obrigatórias do curso. Para o DAG são considerados os pré-requisitos, e um peso P que será exatamente o número de créditos da matéria incidente. Um algoritmo de Ordenação Topológica então é aplicado gerando a representação do grafo, os 2 caminhos críticos selecionados, um possível caminho topológica e uma representação gráfica do grafo.

Requisitos:

	Python 3.10.6 ou superior.
	Bibliotecas networkx e matplotlib.
	Ex3: |- ~~(((p -> u) -> p) -> p)

Comandos para instalar as Bibliotecas (Linux):

	pip install networkx
	pip install matplotlib


	
