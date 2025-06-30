# 🏦Bank Python Functions

![alt text](image-1.png)

Atividade do curso básico de Python do Bootcamp Santander 2025

## 🧭 Objetivo

Sistema de banco possui as seguintes operações:

- Depósito
- Saque
- Visualizar Extrato

### 📑 Necessidades

- os valores devem ser exibidos no formato: R$ xxxx.xx;
- tem que mostrar de que tipo foi a operação (depósito ou saque);

### 📇 As regras para cada operação são:

1. 🪙 Depósito:

   - 1 usuário;
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

## ⚙️ Funcionamento

O sistema tem um menu de seleção, onde pode ser escolhido a operação desejada.

No menu de seleção é possível escolher uma das seguintes opções:

- d: depósito
- s: saque
- e: extrato
- q: sair

Após a seleção da operação, o sistema instrui o usuário para realização da operação desejada. Ao final da operação o resultado da mesma é informado.

## Execução

Para iniciar o sistema, basta executar o arquivo `server.py`, sendo realizado da seguinte forma:

```bash
python server.py
```

---

Software desenvolvido por [Jônatas da Silva](https://github.com/jonatas-silva), como um avaliação do Bootcamp Santander 2025.
