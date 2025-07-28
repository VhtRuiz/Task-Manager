from rich import print # Importa a função 'print' da biblioteca 'rich' para exibir texto colorido no terminal.
from rich.console import Console # Importa a classe 'Console' da 'rich' para gerenciar a saída do console.
from rich.table import Table # Importa a classe 'Table' da 'rich' para criar tabelas formatadas.

console = Console() # Cria uma variável da classe Console para utilizar seus recursos.
print('[italic black] Olá Usuário [/]') # Exibe uma saudação inicial ao usuário em texto itálico e preto.
tasks = [] # Inicializa uma lista vazia para armazenar as tarefas pendentes.
completed_tasks = [] # Inicializa uma lista vazia para armazenar as tarefas concluídas.


def mostrar_tabela(title, task_list, style="light_steel_blue"): # Função para criar uma mini interface na forma de uma tabela.
    table = Table(title=title) # Cria um novo objeto Table com o título fornecido.
    table.add_column("Nº", style="grey100") # Adiciona uma coluna para os números das tarefas com estilo cinza.
    table.add_column("Tarefa", style=style) # Adiciona uma coluna para as tarefas com o estilo de cor especificado.
    for i, task in enumerate(task_list, 1):
        # Itera sobre a 'task_list', adicionando cada tarefa como uma linha na tabela.
        # 'enumerate(task_list, 1)' fornece tanto o índice (começando de 1) quanto a tarefa.
        table.add_row(str(i), task) # Adiciona uma linha com o número da tarefa e a descrição da tarefa.

    console.print(table) # Imprime a tabela formatada no console.


def criar_tarefa():
    # Esta função solicita ao usuário que digite uma nova tarefa e a adiciona à lista 'tasks'.
    x = input('Digite a tarefa que você deseja adicionar:\n') # Obtém a descrição da tarefa do usuário.
    tasks.append(x) # Adiciona a nova tarefa à lista 'tasks'.
    print(f'[italic dark_slate_gray1]Tarefa "{x}" adicionada com sucesso![/]') # Confirma a adição da tarefa.


def listar_tarefa():
    # Esta função exibe as tarefas pendentes ou uma mensagem caso não haja nenhuma.
    if tasks:
        # Se houver tarefas na lista 'tasks', as exibe em uma tabela.
        mostrar_tabela('Tarefas Pendentes', tasks, style='dark_olive_green2')
    else:
        # Se a lista 'tasks' estiver vazia, informa o usuário.
        print('[italic yellow1]Não há tarefas pendentes![/]')


def marcar_como_concluida():
    # Esta função permite ao usuário marcar uma tarefa pendente como concluída.
    if not tasks:
        # Se não houver tarefas, informa o usuário e encerra a função.
        print('[italic yellow1]Não há tarefas para marcar como concluída![/]')
        return

    mostrar_tabela('Selecione a Tarefa concluída', tasks, style='dark_olive_green2') # Exibe as tarefas pendentes.
    try:
        # Tenta obter o número da tarefa que o usuário deseja marcar como concluída.
        num = int(input('\nDigite o número da tarefa para marcar como concluída: \n'))
        if 1 <= num <= len(tasks):
            # Se o número digitado for válido (dentro do intervalo de índices das tarefas).
            completed = tasks.pop(num - 1) # Remove a tarefa da lista 'tasks' e a armazena.
            completed_tasks.append(completed) # Adiciona a tarefa concluída à lista 'completed_tasks'.
            print(f'[italic green]Tarefa "{completed}" marcada como concluída![/]') # Confirma a conclusão da tarefa.
        else:
            # Se o número digitado estiver fora do intervalo.
            print('[italic yellow1]Número inválido![/]')
    except ValueError:
        # Captura um erro se o usuário digitar uma entrada não numérica.
        print('[italic yellow1]Digite um número válido![/]')


def remove_tarefa():
    # Esta função permite ao usuário remover uma tarefa pendente.
    if not tasks:
        # Se não houver tarefas, informa o usuário e encerra a função.
        print('[italic yellow1]Não há tarefas para remover[/]')
        return

    mostrar_tabela('Selecione a tarefa para remover', tasks, style='red1') # Exibe as tarefas pendentes para remoção.
    try:
        # Tenta obter o índice da tarefa que o usuário deseja remover.
        num = int(input('Digite o índice da tarefa que você deseja remover: '))
        if 1 <= num <= len(tasks):
            # Se o número digitado for válido.
            removed = tasks.pop(num - 1) # Remove a tarefa da lista 'tasks' e a armazena.
            print(f'[italic red1] Tarefa "{removed}" removida com sucesso! [/]') # Confirma a remoção da tarefa.
        else:
            # Se o número digitado estiver fora do intervalo.
            print('[italic yellow1]Número inválido![/]')
    except ValueError:
        # Captura um erro se o usuário digitar uma entrada não numérica.
        print('[italic yellow1]Digite um número válido![/]')


def sair():
    # Esta função lida com a saída do programa, exibindo as tarefas pendentes e concluídas.
    print('[italic gray3]Obrigado por usar nosso programa![/]') # Agradece ao usuário.
    print('[italic red1]Você escolheu sair[/]') # Informa ao usuário que ele optou por sair.
    if tasks:
        # Se houver tarefas pendentes restantes, as exibe.
        mostrar_tabela('Tarefas Pendentes', tasks, style="purple3")
    if completed_tasks:
        # Se houver tarefas concluídas, as exibe.
        mostrar_tabela('Tarefas Concluídas', completed_tasks, style="deep_sky_blue1")
    return True # Retorna True para indicar que o programa deve ser encerrado.
