# Sistema de Cadastro de Usuários

Sistema de cadastro e gerenciamento de usuários desenvolvido em Python, com foco em lógica de programação, organização de código, modularização e boas práticas de desenvolvimento.

## 🚀 Funcionalidades

- [x] Cadastro de usuários
- [x] Listagem de usuários
- [x] Busca de usuários
- [x] Edição de usuários
- [x] Exclusão de usuários
- [x] Validação de dados
- [x] Verificação de CPF duplicado
- [x] Persistência dos dados em JSON
- [x] Testes automatizados com pytest

## 🛠️ Tecnologias

- Python
- JSON
- Pytest

## 🧪 Testes

O projeto possui testes automatizados utilizando `pytest`, cobrindo os principais fluxos do sistema.

Atualmente, o projeto possui **10 testes automatizados**.

Para executar os testes:

```bash
python -m pytest
```

Resultado atual:

```text
10 passed
```

## 📂 Estrutura do projeto

```text
sistema-cadastro-usuarios/
│
├── main.py
├── README.md
├── .gitignore
│
├── dados/
│   └── usuarios.json
│
├── sistema/
│   ├── __init__.py
│   ├── armazenamento.py
│   ├── cadastro.py
│   ├── consulta.py
│   ├── edicao.py
│   ├── exclusao.py
│   ├── entrada.py
│   └── dados.py
│
└── test/
    ├── test_cadastro.py
    ├── test_consulta.py
    ├── test_edicao.py
    ├── test_exclusao.py
    └── test_entrada.py
```

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/gustavomourao87-a11y/Sistema-de-cadastro-de-usuario.git
```

### 2. Acesse a pasta do projeto

```bash
cd sistema-cadastro-usuarios
```

### 3. Execute o sistema

```bash
python main.py
```

## 🧪 Executando os testes

Para executar todos os testes automatizados:

```bash
python -m pytest
```

## 📚 Objetivo

Este projeto foi desenvolvido como parte dos meus estudos em Análise e Desenvolvimento de Sistemas.

O objetivo é colocar em prática conceitos de:

- Lógica de programação
- Python
- Funções
- Estruturas de repetição e decisão
- Manipulação de listas e dicionários
- Modularização
- Validação de dados
- Manipulação de arquivos JSON
- Persistência de dados
- Tratamento de erros
- Testes automatizados
- Organização de projetos

## 📈 Evolução do projeto

O projeto está sendo desenvolvido de forma incremental, começando com um sistema simples de cadastro e evoluindo gradualmente com novas funcionalidades, melhorias na organização do código e testes automatizados.

Novas funcionalidades e melhorias serão adicionadas conforme o avanço dos estudos.