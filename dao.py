from models import Tarefa, Usuario

# SQL 

# Criação
SQL_CRIA_TAREFA = 'INSERT into TAREFA (NOME, DESCRICAO, TIPO, STATUS, PRIORIDADE) Values (%s, %s, %s, %s, %s)'

# Atualização 
SQL_ATUALIZA_TAREFA = 'UPDATE TAREFA SET NOME = %s, DESCRICAO = %s, TIPO = %s, STATUS = %s, PRIORIDADE = %s where ID = %s'


class TarefaDao:
    def __init__(self, db):
        self.__db = db
        
    def salvar(self, tarefa):
        cursor = self.__db.connection.cursor()
        
        if (tarefa._id):
            cursor.execute(SQL_ATUALIZA_TAREFA, (tarefa._nome, tarefa._descricao, tarefa._tipo, tarefa._status, tarefa._prioridade))
            
        else:
            cursor.execute(SQL_CRIA_TAREFA, (tarefa._nome, tarefa._descricao, tarefa._tipo, tarefa._status, tarefa._prioridade))
            cursor._id = cursor.lastrowid
            tarefa._id = cursor._id
        
        self.__db.connection.commit()
        return tarefa        