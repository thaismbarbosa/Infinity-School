# Desenvolva um aplicativo de gerenciamento de tarefas
# em python. Crie duas classes, Tarefa e Projeto, com uma
# associação unidirecional. Permita que as tarefas sejam
# associadas a projetos e que você possa listar as tarefas

# de um projeto em particular.

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao 
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True
        print(f'Tarefa {self.descricao} concluida com sucesso!')

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        print(f'Tarefas do projeto {self.nome}:')
        for i, tarefa in enumerate(self.tarefas, 1):
            status = "✅ Concluida" if tarefa.concluida else "❌ Pendente"
            print(f'{i}. {tarefa.descricao} - {status}')
           

minhas_tarefas = Tarefa('Estudar Python')
meu_projeto = Projeto('Criar App')
meu_projeto.adicionar_tarefa(minhas_tarefas)
minhas_tarefas.marcar_concluida()
meu_projeto.listar_tarefas()



        

