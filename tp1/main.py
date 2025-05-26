import duckdb

def query(queryStr):
  result = duckdb.query(queryStr).to_df()
  return result

def printQuery(queryStr):
  print(query(queryStr))

CLIENTES = 'clientes.csv'
FILMES = 'filmes.csv'
INGRESSOS = 'ingressos.csv'
SALAS = 'salas.csv'
SESSOES = 'sessoes.csv'

query_1 = f"""
          SELECT id, nome, email, data_nascimento
          FROM {CLIENTES} \
          WHERE id > 90 
          --AND id < 95\
          """

printQuery(query_1)
