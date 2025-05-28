# CineUFMG — Sistema de Gerenciamento de Cinema 🎥

Repositório do **Trabalho Prático 1** da disciplina **Introdução a Banco de Dados** do curso de **Sistemas de Informação - UFMG**.

## 📄 Descrição

Este projeto visa modelar e implementar um sistema de banco de dados relacional para o **CineUFMG**, uma rede fictícia de cinemas. O sistema abrange cadastros de filmes, salas, sessões, clientes e ingressos, incluindo consultas desenvolvidas em **Álgebra Relacional**, **SQL** e **Linguagem Natural**, executadas utilizando **DuckDB** via **Jupyter Notebook**.

## 📚 Conteúdo do Projeto

- **Modelo Relacional:** Definição das tabelas, atributos, chaves primárias e estrangeiras.
- **Criação do Banco de Dados:** Scripts SQL para criação das tabelas e inserção dos dados.
- **Consultas:**
  - Consultas em Álgebra Relacional
  - Consultas em Linguagem Natural
  - Consultas em SQL
- **Análise dos Resultados:** Interpretação dos dados retornados.

## 🗂️ Estrutura do Repositório

```
tp1/
├── main.py                 # Código principal
├── requirements.txt        # Requisitos para executar o código
├── tp1_bd.pdf              # Enunciado do trabalho
└── README.md               # Este arquivo
```

## 🚀 Como Executar

### ✔️ Pré-requisitos

- Python instalado (versão 3.x)
- Anaconda (recomendado) ou Jupyter Notebook instalado manualmente
- Pacotes == Versão:
  - pandas == 2.0.3
  - duckdb == 1.1.0


### 🔧 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/Lealwbs/ibd.git
```

2. Acesse a pasta do trabalho:

```bash
cd ibd/tp1
```

3. Execute o Jupyter Notebook OU rode diretamente com Python:

```bash
jupyter notebook tp1_matricula.ipynb
```

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

4. Siga as instruções das células para criar o banco de dados e executar as consultas.

## 🧠 Funcionalidades

- 🎬 Cadastro de filmes
- 🎟️ Gerenciamento de sessões e ingressos
- 🏛️ Gerenciamento de salas
- 👥 Controle de clientes
- 🔍 Consultas para apoio à gestão do cinema

## 📊 Consultas Implementadas

- ✅ Consultas em Álgebra Relacional
- ✅ Consultas em Linguagem Natural
- ✅ Consultas SQL para:
  - Filmes por gênero
  - Salas com alta capacidade
  - Sessões noturnas
  - Clientes com mais de X ingressos
  - Sessões sem ingressos vendidos
  - Análise de preço médio dos ingressos
  - E outras...

## 👨‍💻 Tecnologias Utilizadas

- DuckDB
- Python (via Jupyter Notebook)
- Pandas

## 📅 Entrega

- **Data de entrega:** 30/05/2025
- **Disciplina:** Introdução a Banco de Dados — UFMG

## 📧 Contato

- Desenvolvido por [Ítalo Leal](https://github.com/Lealwbs) e [Vitor HUgo](https://github.com/PureVice)  
- Para dúvidas ou sugestões, sinta-se à vontade para abrir uma *issue* no repositório.
