# 🏦Bank Python Functions 2.0

![alt text](image-1.png)

Atividade do curso básico de Python do Bootcamp Santander 2025

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-GPLv3-blue)](https://choosealicense.com/licenses/gpl-3.0/)

## 🧭 Objetivo

Sistema de banco possui as seguintes operações:

- Criar cliente
- Criar conta corrente
- Listar contas do usuário
- Depósito
- Saque
- Visualizar Extrato

### 📑 Necessidades

- os valores devem ser exibidos no formato: R$ xxxx.xx;
- o extrato deve especificar de que tipo foi a operação (depósito ou saque);

### 📇 As regras para cada operação são:

1. 🪙 Depósito:

   - a ser realizado na conta do usuário;
   - depósitos devem ser armazenados em uma variável;
   - e deve ser exibido na operação de extrato;

2. 💸 Saque:

   - 3 saques diários;
   - limite máximo de R$500 por saque;
   - Se não tiver saldo a mensagem dizendo não tem saldo;
   - todos os saques devem ser armazenados e exibidos no extrato;

3. 🧾 Extrato:

   - listar todos os depósitos e saques;
   - deve ser exibido ao final o saldo da conta;

4. 🧓 Criar usuário:

   - registra o usuário no banco;
   - os usuários tem os seguintes dados: nome, data de nascimento, CPF, endereço;
   - não pode existir dois usuários com o mesmo CPF.

5. 🏦 Criar conta corrente:

   - registra a conta corrente no banco;
   - criar conta corrente vinculada ao usuário especificado;
   - os contas correntes tem os seguintes dados: número da conta, agência, saldo, número de saques, extrato;
   - não pode existir duas contas correntes com o mesmo número.

6. 📝 Listar contas do usuário:

   - lista as contas correntes do usuário;
   - informa os seguintes dados referente a conta corrente: número da conta, agência e saldo;

### 📝 Modularização

#### 💲Saque

A função saque recebe argumentos (keyword arguments) e realiza a operação de saque.

```python
def withdraw(*, withdrawal: float, balance: float, extract: dict, number_withdrawal: int, number_account: int, limit: float = LIMIT, limit_withdrawal: int = LIMIT_WITHDRAWAL) -> tuple[float, dict, int]
```

Os dados recebidos pela função são:

- withdrawal: referente ao valor de saque;
- balance: referente ao valor de saldo;
- extract: referente ao extrato bancário;
- number_withdrawal: referente ao limite de saques diários;
- number_account: referente ao número da conta;
- limit: referente ao limite de saque;
- limit_withdrawal: referente ao limite de saques diários;

Os retornos da função são:

- balance: referente ao valor de saldo atualizado;
- extract: referente ao extrato bancário atualizado;
- number_withdrawal: referente ao limite de saques diários atualizado.

#### 🤑 Deposito

A função deposito recebe argumentos (positional argument) e realiza a operação de deposito.

```python
def place(balance: float, deposit: float, extract: dict, /) -> tuple[float, dict]
```

Os dados recebidos pela função são:

- balance: referente ao valor de saldo;
- deposit: referente ao valor de deposito;
- extract: referente ao extrato bancário;

Os retornos da função são:

- balance: referente ao valor de saldo atualizado;
- extract: referente ao extrato bancário atualizado;

#### 🗳️ Extrato bancário

A função extrato recebe argumentos (positional e keyword arguments) e realiza a operação de exibir o extrato bancário referente a conta corrente do usuário especificada.

```python
def display(balance: float, number_account: int, agency: str, /, *, extract: dict) -> None
```

Os dados recebidos pela função são:

- balance: referente ao valor de saldo;
- number_account: referente ao número da conta;
- agency: referente à agência onde a conta corrente se encontra;
- extract: referente ao extrato bancário da conta corrente;

E não possui retornos.

#### 👤 Criar usuário

A função usuário não recebe argumentos e realiza a operação de criação de um usuário.

```python
def create_user() -> None
```

E não possui retornos.

#### 🏦 Criação de conta corrente

A função criar conta não recebe argumentos e realiza a operação de criação de uma conta corrente.

```python
def create_account() -> None
```

E não possui retornos.

#### 📝 Listagem de contas do usuário

A função listagem de contas não recebe argumentos e realiza a operação de listagem de contas do usuário.

```python
def list_accounts() -> None
```

E não possui retornos.

## ⚙️ Funcionamento

O sistema tem um menu de seleção, onde pode ser escolhido a operação desejada.

No menu de seleção é possível escolher uma das seguintes opções:

- u: criar usuário
- c: criar conta
- l: listar contas do usuário
- d: deposito
- s: saque
- e: extrato
- q: sair

Após a seleção da operação, o sistema instrui o usuário para realização da operação desejada. Ao final da operação o resultado da mesma é informado.

## Execução

Para iniciar o sistema, basta executar o arquivo `server.py`, sendo realizado da seguinte forma:

```bash
python server.py
```

ou

```bash
python3 server.py
```

---

Software desenvolvido por [Jônatas da Silva](https://github.com/jonatas-silva), como um avaliação do Bootcamp Santander 2025.
