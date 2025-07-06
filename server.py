#!/usr/bin/python
import os
import re
from datetime import datetime

MENU = """
=== BEM VINDO AO BANK PYTHON 2.0 ===

[u] Criar usuário
[c] Criar conta
[l] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

# Constantes
LIMIT = 500.0
LIMIT_WITHDRAWAL = 3

# global variables
users = {}
current_account = 0

def clear() -> None:
    # for windows
    if os.name == "nt":
        os.system("cls")
    # for mac and Linux
    else:
        os.system("clear")


def validate_address(address: str) -> bool:
    """
    Validates if the address follows the format: logradouro, n° - bairro - cidade/estado
    Example valid input: "Rua das Flores, 123 - Centro - São Paulo/SP"
    """
    pattern = r'^[^,]+,\s*\d+[-\w]*\s*-\s*[^-]+\s*-\s*[^/]+/[A-Z]{2}$'
    return bool(re.match(pattern, address.strip()))


def create_user() -> None:
    global users
    
    print("\n=== CRIAÇÃO DE USUÁRIO ===\n")
    cpf = input("Digite o cpf: ")
    if (cpf in users):
        print("Usuário já cadastrado, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return
    else:
        name = input("Digite o nome: ").strip()
        date_of_birth = input("Digite a data de nascimento: ").strip()
        address = input("Digite o endereço [logradouro, n° - bairro - cidade/estado]: ").strip()
        if not validate_address(address):
            print("Endereço inválido, tente novamente mais tarde!")
            input("\nPressione Enter para continuar...")
            return
        users[cpf] = {"name": name, "date_of_birth": date_of_birth, "address": address, "accounts": {}}
    print("\n\nUsuário criado com sucesso!")
    print("    Nome: ", name)
    print("    Data de nascimento: ", date_of_birth)
    print("    Endereço: ", address)
    input("\nPressione Enter para continuar...")


def create_account() -> None:
    global users, current_account
    
    print("\n=== CRIAÇÃO DE CONTA ===\n")
    cpf = input("Digite o cpf: ")
    if len(cpf) != 11:
        print("CPF inválido, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return
    if (cpf not in users):
        print("Usuário não cadastrado, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return
    else:
        current_account += 1
        number_account = current_account
        if (number_account in users[cpf]["accounts"]):
            print("Conta já cadastrada, tente novamente mais tarde!")
            input("\nPressione Enter para continuar...")
            return
        password = input("Digite a senha: ")
        users[cpf]["accounts"][number_account] = {"number_account": number_account, "password": password, "agency": "0001", "balance": 0.0, "number_withdrawal": 0, "extract": {"deposit": [], "withdraw": []}}
    message = f"\n\nConta criada com sucesso!\n    Número da conta: {number_account}\n    Agência: 0001\n    Saldo: R$ 0.00"
    print(message)
    input("\nPressione Enter para continuar...")
    

def list_accounts() -> None:
    global users
    
    print("\n=== LISTAGEM DE CONTAS ===\n")
    print(users)
    cpf = input("Digite o cpf: ")
    if (cpf not in users):
        print("Usuário não cadastrado, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return
    for account in users[cpf].get("accounts", {}):
        print(f"\n\tNúmero da conta: {account}")
        print(f'\tAgência: {users[cpf]["accounts"][account]['agency']}')
        print(f'\tSaldo: R$ {users[cpf]["accounts"][account]['balance']:.2f}')
    
    input("\nPressione Enter para continuar...")


def place(balance: float, deposit: float, extract: dict, /) -> tuple[float, dict]:
    new_date = datetime.now().strftime("%d/%m/%Y")
    entries = extract.get('deposit', [])

    if len(entries) > 0:
        for entry in entries:
            if new_date in entry:
                entry[new_date].append(deposit)
                balance += deposit
            else:
                entry[new_date] = [deposit]
                balance += deposit
    else:
        entries.append({new_date: [deposit]})
        balance += deposit
    
    print(f"\n   Saldo: R$ {balance:.2f}\n   Depositado: R$ {deposit:.2f}")
    print("\n\nDeposito realizado com sucesso!\n")
    input("Pressione Enter para continuar...")
    return (balance, extract)


def withdraw(*,withdrawal: float, balance: float, extract: dict, number_withdrawal: int, number_account: int, limit: float = LIMIT, limit_withdrawal: int = LIMIT_WITHDRAWAL) -> tuple[float, dict, int]:    
    entries = extract.get('withdraw', [])
    new_date = datetime.now().strftime("%d/%m/%Y")

    if (withdrawal > limit):
        print("Valor diário de saque excedido, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return
    
    elif (number_withdrawal >= limit_withdrawal):
        print("Limite diário de saques excedido, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return

    elif (withdrawal > balance):
        print("Saldo insuficiente, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return

    else:
        balance -= withdrawal
        print(f"\n   Saldo: R$ {balance:.2f}\n   Sacado: R$ {withdrawal:.2f}")
        number_withdrawal += 1

        if len(entries) > 0:
            for entry in entries:
                if new_date in entry:
                    entry[new_date].append(withdrawal)
                else:
                    entry[new_date] = [withdrawal]
        else:
            entries.append({new_date: [withdrawal]})
        
        print("\n\nSaque realizado com sucesso!")
        input("\nPressione Enter para continuar...")
        return (balance, extract, number_withdrawal)


def display(balance: float, number_account: int, agency: str, /, *, extract: dict) -> None:
    message = f"\n=== EXTRATO ===\n\nNúmero da conta: {number_account}\nAgência: {agency}"
    print(message)
    for entries in extract.get('deposit', []):
        print("\nDepósitos: \n")
        for entry in entries:
            print("    ",entry, ": ", entries[entry])

    for entries in extract.get('withdraw', []):
        print("\nSaques: \n")
        for entry in entries:
            print("    ",entry, ": ", entries[entry])
    
    print(f"\n\nSaldo: R$ {balance:.2f}")
    input("\nPressione Enter para continuar...")

def main() -> None:
    global users
    
    while True:
        clear()
        print(MENU)
        option = input()

        if option == "q":
            break

        elif option == "u":
            create_user()

        elif option == "c":
            create_account()

        elif option == "l":
            list_accounts()

        elif option == "d":
            cpf = input("\nDigite o cpf: ")
            if (cpf not in users):
                print("Usuário não cadastrado, tente novamente mais tarde!")
                input("\nPressione Enter para continuar...")
            else:
                number_account = int(input("\nDigite o número da conta: "))
                password = input("\nDigite a senha: ")
                if (number_account not in users[cpf]["accounts"]) or (password != users[cpf]["accounts"][number_account]['password']):
                    print("Conta ou senha inválidos, tente novamente mais tarde!")
                    input("\nPressione Enter para continuar...")
                else:
                    deposit = float(input("\nDigite o valor do deposito: "))
                    plunder = place(users[cpf]["accounts"][number_account]['balance'], deposit, users[cpf]["accounts"][number_account]['extract'])
                    users[cpf]["accounts"][number_account]['balance'] = plunder[0]
                    users[cpf]["accounts"][number_account]['extract'] = plunder[1]

        elif option == "s":
            cpf = input("\nDigite o cpf: ")
            if (cpf not in users):
                print("Usuário não cadastrado, tente novamente mais tarde!")
                input("\nPressione Enter para continuar...")
            else:
                number_account = int(input("\nDigite o número da conta: "))
                password = input("\nDigite a senha: ")
                if (number_account not in users[cpf]["accounts"]) or (password != users[cpf]["accounts"][number_account]['password']):
                    print("Conta ou senha inválidos, tente novamente mais tarde!")
                    input("\nPressione Enter para continuar...")
                else:
                    withdrawal = float(input("\nDigite o valor do saque: "))
                    plunder = withdraw(withdrawal=withdrawal, balance=users[cpf]["accounts"][number_account]['balance'], extract=users[cpf]["accounts"][number_account]['extract'], number_withdrawal=users[cpf]["accounts"][number_account]['number_withdrawal'], number_account=number_account, limit=LIMIT, limit_withdrawal=LIMIT_WITHDRAWAL)
                    users[cpf]["accounts"][number_account]['balance'] = plunder[0]
                    users[cpf]["accounts"][number_account]['extract'] = plunder[1]
                    users[cpf]["accounts"][number_account]['number_withdrawal'] = plunder[2]

        elif option == "e":
            cpf = input("\nDigite o cpf: ")
            if (cpf not in users):
                print("Usuário não cadastrado, tente novamente mais tarde!")
                input("\nPressione Enter para continuar...")
            else:
                number_account = int(input("\nDigite o número da conta: "))
                password = input("\nDigite a senha: ")
                if (number_account not in users[cpf]["accounts"]) or (password != users[cpf]["accounts"][number_account]['password']):
                    print("Conta ou senha inválidos, tente novamente mais tarde!")
                    input("\nPressione Enter para continuar...")
                else:
                    print("\nPrezado cliente, aqui está seu extrato: ")
                    display(users[cpf]["accounts"][number_account]['balance'], number_account, users[cpf]["accounts"][number_account]['agency'], extract=users[cpf]["accounts"][number_account]['extract'])


if __name__ == "__main__":
    main()