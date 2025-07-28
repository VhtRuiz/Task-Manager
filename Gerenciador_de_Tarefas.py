from rich import print
from rich.console import Console
from rich.table import Table

console = Console()
print('[italic black] Olá Usuário [/]')
tasks = []
completed_tasks = []


def mostrar_tabela(title, task_list, style="light_steel_blue"):
      table = Table(title=title)
      table.add_column("Nº", style="grey100")
      table.add_column("Tarefa", style = style)
      for i, task in enumerate(task_list, 1):
          table.add_row(str(i), task)

      console.print(table)

def criar_tarefa():
      x = input('Digite a tarefa que você deseja adicionar:\n')
      tasks.append(x)
      print(f'[italic dark_slate_gray1]Tarefa "{x}" adicionada com sucesso![/]')

def listar_tarefa(): 
      if tasks:
          mostrar_tabela('Tarefas Pendentes', tasks, style = 'dark_olive_green2')
      else:
          print('[italic yellow1]Não há tarefas pendentes![/]')

def marcar_como_concluida():
      if not tasks:
          print('[italic yellow1]Não há tarefas para marcar como concluída![/]')
          return
      
      mostrar_tabela('Selecione a Tarefa concluída', tasks, style = 'dark_olive_green2')
      try:
          num = int(input('\nDigite o número da tarefa para marcar como concluída: \n'))
          if 1 <= num <= len(tasks):
              completed = tasks.pop(num-1)
              completed_tasks.append(completed) 
              print(f'[italic green]Tarefa "{completed}" marcada como concluída![/]')
          else:
              print('[italic yellow1]Número inválido![/]')
      except ValueError:
          print('[italic yellow1]Digite um número válido![/]')

def remove_tarefa():
      if not tasks:
          print('[italic yellow1]Não há tarefas para remover[/]')
          return
      
      mostrar_tabela('Selecione a tarefa para remover', tasks, style = 'red1')
      try:
          num = int(input('Digite o índice da tarefa que você deseja remover: '))
          if 1 <= num <= len(tasks): 
              removed = tasks.pop(num - 1)
              print(f'[italic red1] Tarefa "{removed}" removida com sucesso! [/]')
          else:
              print('[italic yellow1]Número inválido![/]')
      except ValueError:
          print('[italic yellow1]Digite um número válido![/]')

def sair():
      print('[italic gray3]Obrigado por usar nosso programa![/]')
      print('[italic red1]Você escolheu sair[/]')
      if tasks:
          mostrar_tabela('Tarefas Pendentes', tasks, style="purple3")
      if completed_tasks:
          mostrar_tabela('Tarefas Concluídas', completed_tasks, style="deep_sky_blue1")
      return True