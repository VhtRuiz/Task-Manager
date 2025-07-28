import Gerenciador_de_Tarefas
while True: 
    opcao = input('\nDigite o que você deseja realizar:\n'
                 '1. CRIAR TAREFA\n'
                 '2. LISTAR TAREFAS PENDENTES\n'
                 '3. MARCAR TAREFA COMO CONCLUÍDA\n'
                 '4. REMOVER TAREFA\n'
                 '5. SAIR\n'
                 '\nOpção: ')
    
    if opcao == '1':
        Gerenciador_de_Tarefas.criar_tarefa()
    elif opcao == '2':
        Gerenciador_de_Tarefas.listar_tarefa()
    elif opcao == '3':
        Gerenciador_de_Tarefas.marcar_como_concluida()
    elif opcao == '4':
        Gerenciador_de_Tarefas.remove_tarefa()
    elif opcao == '5':
        if Gerenciador_de_Tarefas.sair():
          break
        