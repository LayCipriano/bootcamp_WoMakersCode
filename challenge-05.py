# DESAFIO 5

# Crie um programa que permita ao usuário gerenciar suas tarefas diárias. O programa deve oferecer as seguintes funcionalidades:

# Adicionar uma nova tarefa;
# Visualizar todas as tarefas;
# Marcar uma tarefa como concluída;
# Remover uma tarefa;
# Sair do programa.
# (Você pode implementar essas funcionalidades usando listas para armazenar as tarefas e estruturas de controle como loops e condicionais para interagir com o usuário.)

def criarTask(name, status = False):
    if not status:
        statusCode = "Em Andamento"
    else:
        statusCode = "Concluído"
    
    print("------------------------------------")
    print("Item adicionado, lista atualizada!")
    print("------------------------------------")
    
    return {'nome': name, 'status': statusCode}


def verTask():    
    if len(task) < 1:
            print("Não há tarefas!")
    else:
        for index in task:
            print(index['nome'] + " - " + str(index['status']))
            print("------------------------------------")


def concluirTask():    
    print("Concluir uma task da lista")
    
    choice = input("Qual task deseja concluir? ")
                
    found = False        
                
    for index in task:
        if index['nome'] == choice:
            index['status'] = 'Concluído'
            found = True
        break  
    if found:
        print("Tarefa concluída com sucesso")
        print("------------------------------------")     
    else:
        print("Tarefa não encontrada!")   
     
    
def removerTask():
    print("Remover uma task da lista")
    
    delete = input("Qual task deseja remover? ")

    for index in task:
        if index['nome'] == delete:
            task.remove(index)
            print("Task removida, lista atualizada!")
            print("------------------------------------")
            break
    else: 
        print("Task não encontrada")
    
def sair():
    print("Saindo... obrigada por usar!")


# lista de tasks
task = []

def toDoList():
   
    # "menu" para o usuário escolher o que vai fazer
    print("""
        1. Adicionar nova tarefa
        2. Visualizar todas as tarefas
        3. Concluir uma tarefa
        4. Remover uma tarefa
        5. Sair do programa
          """)
    try:
        value = int(input("O que você quer fazer? "))
    except ValueError:
        print("Opção inválida. Por favor, insira um número!")
        return toDoList()
    
    if value == 1:
        print("ADICIONAR NOVA TAREFA")
        print(" ")
        newTask = input("TAREFA: ")
        task.append(criarTask(newTask))
        toDoList()
        
    elif value == 2:
        print("VER TODAS AS TAREFAS")
        print(" ")
        verTask()
        toDoList()
        
    elif value == 3:
        print("CONCLUIR TASK")
        print(" ")
        concluirTask()
        toDoList()
        
    elif value == 4:
        print("REMOVER UMA TASK")
        print(" ")
        
        removerTask()
        toDoList()
        
    elif value == 5:
        print("OBRIGADA POR USAR..............")
        
toDoList()