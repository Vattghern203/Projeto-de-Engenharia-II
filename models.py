class Tarefa:
    def __init__(self, nome, descricao, tipo, status, prioridade, id=None):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._tipo = tipo
        self._status = status
        self._prioridade = prioridade 
        
class Usuario:
    def __init__(self, nome, email, senha, id=None):
        self._id = id
        self._nome = nome
        self._email = email
        self._senha = senha 

tarefa01 = Tarefa('Estudar Matemática', 'estudar logaritmo', 'em andamento', 'Estudos', 'Alta')
tarefa02 = Tarefa('Compras', 'Comprar Pão', 'Afazeres Domésticos', 'A Fazer', 'Alta')

lista = [tarefa01, tarefa02]