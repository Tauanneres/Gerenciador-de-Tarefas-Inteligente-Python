# Ficheiro: logica_tarefas.py

import json

# Define o nome do ficheiro onde as tarefas serão guardadas
FICHEIRO_TAREFAS = 'tarefas.json'

def carregar_tarefas():
    """
    Carrega as tarefas do ficheiro JSON.
    Se o ficheiro não existir, retorna uma lista vazia.
    """
    try:
        # Abre o ficheiro em modo de leitura ('r') com codificação UTF-8
        with open(FICHEIRO_TAREFAS, 'r', encoding='utf-8') as f:
            # Carrega (lê) o conteúdo JSON do ficheiro para uma lista Python
            return json.load(f)
    except FileNotFoundError:
        # Se o ficheiro não for encontrado (primeira vez a executar, por exemplo),
        # retorna uma lista vazia, pois ainda não há tarefas.
        return []

def salvar_tarefas(tarefas):
    """
    Salva a lista de tarefas (passada como argumento) no ficheiro JSON.
    """
    # Abre o ficheiro em modo de escrita ('w') com codificação UTF-8
    # Se o ficheiro não existir, ele é criado. Se existir, é sobrescrito.
    with open(FICHEIRO_TAREFAS, 'w', encoding='utf-8') as f:
        # Guarda (escreve) a lista de tarefas no ficheiro no formato JSON.
        # indent=4 torna o ficheiro JSON mais legível por humanos (com indentação).
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(tarefas, descricao_nova_tarefa):
    """
    Adiciona uma nova tarefa à lista de tarefas.
    Uma tarefa é um dicionário com 'descricao' e 'concluida'.
    """
    if descricao_nova_tarefa: # Verifica se a descrição não está vazia
        tarefa = {"descricao": descricao_nova_tarefa, "concluida": False}
        tarefas.append(tarefa) # Adiciona a nova tarefa à lista

def remover_tarefa(tarefas, indice):
    """
    Remove uma tarefa da lista pelo seu índice.
    """
    # Verifica se o índice é válido (está dentro dos limites da lista)
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice) # Remove a tarefa no índice especificado

def marcar_como_concluida(tarefas, indice):
    """
    Marca uma tarefa específica como concluída pelo seu índice.
    """
    # Verifica se o índice é válido
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True # Altera o estado 'concluida' para True