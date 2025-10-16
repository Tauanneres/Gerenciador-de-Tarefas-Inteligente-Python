# Ficheiro: gerenciador_gui.py

import tkinter as tk
from tkinter import messagebox
# Importamos o nosso módulo de lógica de tarefas.
# Podemos agora chamar funções como logica.carregar_tarefas()
import logica_tarefas as logica

# --- Variáveis Globais (para serem acedidas e modificadas pelas funções da GUI) ---
# A lista de tarefas será carregada aqui.
tarefas = []


# --- Funções "Cola" (que ligam a interface à lógica e atualizam a GUI) ---

def atualizar_listbox():
    """
    Limpa completamente o Listbox na interface e o preenche novamente
    com a lista atual de tarefas, refletindo o seu estado (concluída/pendente).
    """
    listbox_tarefas.delete(0, tk.END)  # Limpa todos os itens do Listbox

    for i, tarefa in enumerate(tarefas):  # Percorre a lista de tarefas
        status = "[Concluída]" if tarefa["concluida"] else "[Pendente]"
        # Insere a tarefa formatada no Listbox
        listbox_tarefas.insert(tk.END, f'{status} {tarefa["descricao"]}')

        # Se a tarefa estiver concluída, altera a cor de fundo e da fonte
        if tarefa["concluida"]:
            # Obtém o índice do item que acabou de ser inserido
            listbox_tarefas.itemconfig(i, {'bg': 'lightgrey', 'fg': 'grey'})


def on_adicionar():
    """
    Função chamada quando o botão 'Adicionar Tarefa' é clicado.
    Obtém a descrição da tarefa do campo de entrada, adiciona-a e salva.
    """
    descricao = entry_nova_tarefa.get()  # Obtém o texto do campo de entrada

    # Validação simples para não adicionar tarefas vazias
    if not descricao:
        messagebox.showwarning("Aviso", "A descrição da tarefa não pode estar vazia.")
        return

    logica.adicionar_tarefa(tarefas, descricao)  # Chama a função de lógica para adicionar
    logica.salvar_tarefas(tarefas)  # Salva a lista atualizada
    atualizar_listbox()  # Atualiza a interface
    entry_nova_tarefa.delete(0, tk.END)  # Limpa o campo de entrada


def on_remover():
    """
    Função chamada quando o botão 'Remover Selecionada' é clicado.
    Remove a tarefa selecionada da lista e atualiza a interface.
    """
    try:
        # Obtém o índice da tarefa selecionada no Listbox (curselection retorna uma tupla)
        indice_selecionado = listbox_tarefas.curselection()[0]
        logica.remover_tarefa(tarefas, indice_selecionado)  # Chama a lógica para remover
        logica.salvar_tarefas(tarefas)  # Salva a lista atualizada
        atualizar_listbox()  # Atualiza a interface
    except IndexError:
        # Se nenhuma tarefa estiver selecionada, curselection() estará vazia,
        # gerando um IndexError.
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")


def on_concluir():
    """
    Função chamada quando o botão 'Marcar como Concluída' é clicado.
    Marca a tarefa selecionada como concluída e atualiza a interface.
    """
    try:
        indice_selecionado = listbox_tarefas.curselection()[0]
        logica.marcar_como_concluida(tarefas, indice_selecionado)  # Chama a lógica para marcar
        logica.salvar_tarefas(tarefas)  # Salva a lista atualizada
        atualizar_listbox()  # Atualiza a interface
    except IndexError:
        messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para concluir.")


# --- Configuração da Janela Principal (Root Window) ---
janela = tk.Tk()  # Cria a janela principal
janela.title("Gerenciador de Tarefas")  # Define o título da janela
janela.geometry("500x400")  # Define o tamanho inicial da janela (largura x altura)

# --- Criação dos Widgets da Interface ---

# Frame para agrupar o Listbox e o Scrollbar (melhor organização visual)
frame_lista = tk.Frame(janela)
# Pack é um gerenciador de layout: pady/padx para margens, fill para expandir, expand para ocupar espaço
frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Listbox para exibir as tarefas
listbox_tarefas = tk.Listbox(frame_lista, height=10, selectbackground="lightblue", font=('Arial', 10))
listbox_tarefas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar (barra de rolagem) para o Listbox
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # A barra de rolagem preenche verticalmente

# Conecta o Scrollbar ao Listbox
listbox_tarefas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tarefas.yview)

# Frame para o campo de entrada de nova tarefa e o botão 'Adicionar'
frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=5, padx=10, fill=tk.X)

# Campo de entrada de texto
entry_nova_tarefa = tk.Entry(frame_entrada, width=40, font=('Arial', 10))
entry_nova_tarefa.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Botão para adicionar tarefa
botao_adicionar = tk.Button(frame_entrada, text="Adicionar Tarefa", command=on_adicionar, font=('Arial', 10, 'bold'),
                            bg='#4CAF50', fg='white')
botao_adicionar.pack(side=tk.RIGHT, padx=5)

# Frame para os botões de ação (Concluir e Remover)
frame_acoes = tk.Frame(janela)
frame_acoes.pack(pady=10, padx=10, fill=tk.X)

# Botão para marcar tarefa como concluída
botao_concluir = tk.Button(frame_acoes, text="Marcar como Concluída", command=on_concluir, font=('Arial', 10, 'bold'),
                           bg='#2196F3', fg='white')
botao_concluir.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

# Botão para remover tarefa
botao_remover = tk.Button(frame_acoes, text="Remover Selecionada", command=on_remover, font=('Arial', 10, 'bold'),
                          bg='#f44336', fg='white')
botao_remover.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=5)

# --- Inicialização da Aplicação ---

# 1. Carrega as tarefas existentes (se houver) ao iniciar o programa
tarefas = logica.carregar_tarefas()
# 2. Preenche o Listbox com as tarefas carregadas
atualizar_listbox()
# 3. Inicia o loop principal do Tkinter, que mantém a janela aberta
#    e responsiva a eventos (cliques de botão, etc.).
janela.mainloop()