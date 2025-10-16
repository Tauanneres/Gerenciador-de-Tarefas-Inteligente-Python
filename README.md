# Gerenciador-de-Tarefas-Inteligente-Python

Um gerenciador de tarefas desenvolvido em Python com interface gráfica usando tkinter. Este projeto permite adicionar, remover e marcar tarefas como concluídas, incluindo a definição de prioridade. As tarefas são salvas em um arquivo JSON, garantindo persistência de dados.

## Tecnologias Utilizadas

- Python 3
- Tkinter para interface gráfica
- JSON para salvar e carregar tarefas
- Estrutura modular: separação entre lógica e interface gráfica

## Funcionalidades

- Adicionar tarefas com descrição e prioridade (Baixa, Média ou Alta).
- Marcar tarefas como concluídas, destacando visualmente na lista.
- Remover tarefas individuais ou limpar toda a lista.
- Persistência de dados: todas as tarefas são salvas e carregadas automaticamente do arquivo tarefas.json.
- Interface gráfica intuitiva e fácil de usar.

## Estrutura do Código

### `logica_tarefas.py`
Contém a lógica principal do aplicativo: carregar, salvar, adicionar, remover e marcar tarefas como concluídas. Manipula dados em formato JSON. É independente da interface gráfica.

### `gerenciador_gui.py`
Cria a interface gráfica usando Tkinter (janela, frames, botões, campos de texto e listbox). Conecta a interação do usuário com a lógica do aplicativo por meio de funções de callback. Atualiza a interface dinamicamente quando tarefas são adicionadas, removidas ou concluídas.
