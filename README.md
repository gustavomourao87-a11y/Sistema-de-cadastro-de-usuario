# Sistema de Cadastro de Usuários

Sistema de cadastro e gerenciamento de usuários desenvolvido em Python, com foco em lógica de programação, organização de código, modularização e boas práticas de desenvolvimento.

O projeto foi desenvolvido de forma incremental durante meus estudos em Análise e Desenvolvimento de Sistemas, evoluindo de uma aplicação simples de cadastro para uma estrutura modular com persistência de dados e testes automatizados.

## 🚀 Funcionalidades

- [x] Validação das opções do menu
- [x] Cadastro de usuários
- [x] Listagem de usuários
- [x] Busca de usuários por CPF
- [x] Edição de usuários
- [x] Exclusão de usuários
- [x] Validação de nome
- [x] Validação de CPF
- [x] Verificação de CPF duplicado
- [x] Persistência dos dados em JSON
- [x] Tratamento de arquivo inexistente
- [x] Tratamento de JSON inválido
- [x] Testes automatizados com pytest
- [x] Testes de persistência de dados
- [x] Análise de cobertura de código

## 🛠️ Tecnologias

- Python
- JSON
- Pytest
- Pytest-cov
- Git
- GitHub

## 🧪 Testes

O projeto possui testes automatizados utilizando `pytest`, cobrindo os principais fluxos e comportamentos do sistema.

Atualmente, o projeto possui:

- **23 testes automatizados**
- **100% de cobertura de código**
- Testes de cadastro
- Testes de consulta
- Testes de edição
- Testes de exclusão
- Testes de validação de entrada
- Testes de carregamento dos dados
- Testes de salvamento dos dados
- Testes de tratamento de erros

### Executar os testes

Para executar todos os testes:

```bash
python -m pytest
```

Resultado atual:

```text
24 passed
```

### Executar os testes com cobertura

Para verificar a cobertura do código:

```bash
python -m pytest --cov=sistema
```

Cobertura atual:

```text
100% de cobertura
```

### Cobertura por módulo

| Módulo | Cobertura |
|---|---:|
| `cadastro.py` | 100% |
| `consulta.py` | 100% |
| `edicao.py` | 100% |
| `exclusao.py` | 100% |
| `dados.py` | 100% |
| `armazenamento.py` | 100% |
| `entrada.py` | 100% |
| **Total** | **100%** |

## 📂 Estrutura do projeto

```text
Sistema-de-cadastro-de-usuario/

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
    ├── test_armazenamento.py
    ├── test_cadastro.py
    ├── test_consulta.py
    ├── test_edicao.py
    ├── test_exclusao.py
    └── test_entrada.py
```

## 📌 Organização do projeto

O projeto foi dividido em diferentes módulos para separar as responsabilidades do sistema.

### `main.py`

Responsável por iniciar o sistema e controlar o menu principal.

### `sistema/cadastro.py`

Responsável pelo cadastro de novos usuários e pela verificação de CPF duplicado.

### `sistema/consulta.py`

Responsável pela listagem e busca de usuários.

### `sistema/edicao.py`

Responsável pela alteração dos dados de usuários existentes.

### `sistema/exclusao.py`

Responsável pela remoção de usuários.

### `sistema/entrada.py`

Responsável pelo menu e pelas funções de entrada e validação dos dados fornecidos pelo usuário.

### `sistema/armazenamento.py`

Responsável pelo carregamento e salvamento dos usuários no arquivo JSON.

### `sistema/dados.py`

Responsável pela lista de usuários utilizada pelo sistema.

### `test/`

Contém os testes automatizados responsáveis por verificar o comportamento das principais funcionalidades do sistema.

## 💾 Persistência de dados

Os usuários cadastrados são armazenados no arquivo:

```text
dados/usuarios.json
```

O projeto utiliza o módulo `json` do Python para realizar a persistência dos dados.

Os dados são carregados quando o sistema é iniciado e atualizados quando um usuário é cadastrado, editado ou excluído.

O sistema também possui tratamento para situações como:

- Arquivo de usuários inexistente
- Arquivo JSON inválido
- Erros durante o salvamento dos dados

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/gustavomourao87-a11y/Sistema-de-cadastro-de-usuario.git
```

### 2. Acesse a pasta do projeto

```bash
cd Sistema-de-cadastro-de-usuario
```

### 3. Instale as dependências

Instale o `pytest` e o `pytest-cov`:

```bash
python -m pip install pytest pytest-cov
```

### 4. Execute o sistema

```bash
python main.py
```

## 🧪 Executando os testes

Para executar todos os testes automatizados:

```bash
python -m pytest
```

Para executar os testes com análise de cobertura:

```bash
python -m pytest --cov=sistema
```

## 📚 Conceitos praticados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Lógica de programação
- Python
- Variáveis
- Funções
- Parâmetros e retornos
- Estruturas condicionais
- Estruturas de repetição
- Listas
- Dicionários
- Manipulação de strings
- Validação de dados
- Modularização
- Importação de módulos
- Manipulação de arquivos
- JSON
- Persistência de dados
- Tratamento de exceções
- Testes automatizados
- `pytest`
- `monkeypatch`
- `capsys`
- Testes com arquivos temporários
- Cobertura de código
- Organização de projetos
- Git
- GitHub

## 🎯 Objetivo

Este projeto foi desenvolvido como parte dos meus estudos em Análise e Desenvolvimento de Sistemas.

O principal objetivo é transformar os conhecimentos adquiridos durante os estudos em uma aplicação prática, desenvolvendo gradualmente uma melhor compreensão de lógica de programação, organização de código, testes e desenvolvimento de sistemas.

O projeto também serve como parte do meu portfólio de desenvolvimento.

## 📈 Evolução do projeto

O projeto está sendo desenvolvido de forma incremental.

A aplicação começou como um sistema simples de cadastro de usuários e foi evoluindo com:

1. Criação das funções principais
2. Separação das responsabilidades em módulos
3. Validação dos dados
4. Verificação de CPF duplicado
5. Persistência dos usuários em JSON
6. Tratamento de erros
7. Criação de testes automatizados
8. Testes de diferentes cenários
9. Análise da cobertura de código

Atualmente, o sistema possui **24 testes automatizados** e **100% de cobertura de código**.

Novas funcionalidades e melhorias serão adicionadas conforme o avanço dos estudos.

## 🔮 Próximos passos

Algumas melhorias que poderão ser implementadas futuramente:

- [ ] Criar um `requirements.txt`
- [ ] Melhorar as validações de entrada
- [ ] Implementar orientação a objetos
- [ ] Substituir o JSON por um banco de dados
- [ ] Criar uma API
- [ ] Criar uma interface web
- [ ] Implementar autenticação de usuários

## 👨‍💻 Sobre o projeto

Este projeto faz parte da minha jornada de aprendizado em desenvolvimento de sistemas e está sendo construído de maneira prática, buscando aplicar os conceitos estudados em projetos reais.

A proposta é continuar evoluindo o sistema conforme novos conhecimentos forem adquiridos.