import Gerenciador_de_Tarefas #importando o outro módulo criado anteriormente
while True: #utilização de um loop para o programa continuar rodando até atingir a condição de parada
    opcao = input('\nDigite o que você deseja realizar:\n'
                 '1. CRIAR TAREFA\n'
                 '2. LISTAR TAREFAS PENDENTES\n'
                 '3. MARCAR TAREFA COMO CONCLUÍDA\n'
                 '4. REMOVER TAREFA\n'
                 '5. SAIR\n'
                 '\nOpção: ')
    
    if opcao == '1': 
        Gerenciador_de_Tarefas.criar_tarefa() #chama a função criar tarefa do módulo importado
    elif opcao == '2':
        Gerenciador_de_Tarefas.listar_tarefa() #chama a função listar tarefa do módulo importado
    elif opcao == '3':
        Gerenciador_de_Tarefas.marcar_como_concluida() #chama a função marcar como concluida do módulo importado
    elif opcao == '4':
        Gerenciador_de_Tarefas.remove_tarefa() #chama a função remove tarefa do módulo importado
    elif opcao == '5':
        if Gerenciador_de_Tarefas.sair():  #chama a função sair para finalizar o programa
          break #aqui se encerra o loop e consequentemente o programa
        
