#!/usr/bin/python
import os
from datetime import datetime

MENU = """
=== BEM VINDO AO BANK PYTHON ===

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

# Constantes
LIMIT = 500.0
LIMIT_WITHDRAWAL = 3

# global variables
balance = 0
number_withdrawal = 0
extract = {"deposit": [], "withdraw": []}


def clear() -> None:
    # for windows
    if os.name == "nt":
        os.system("cls")
    # for mac and Linux
    else:
        os.system("clear")


def place() -> None:
    global balance, extract
    value = float(input("\nDigite o valor do deposito: "))
    new_date = datetime.now().strftime("%d/%m/%Y")
    entries = extract.get('deposit', [])

    if len(entries) > 0:
        for entry in entries:
            if new_date in entry:
                entry[new_date].append(value)
                balance += value
            else:
                entry[new_date] = [value]
                balance += value
    else:
        entries.append({new_date: [value]})
        balance += value
    
    print(f"\n   Saldo: R$ {balance:.2f}\n   Depositado: R$ {value:.2f}")
    print("\n\nDeposito realizado com sucesso!\n")
    input("Pressione Enter para continuar...")


def withdraw() -> None:
    global balance, extract, LIMIT, LIMIT_WITHDRAWAL, number_withdrawal
    
    entries = extract.get('withdraw', [])
    new_date = datetime.now().strftime("%d/%m/%Y")
    value = float(input("\nDigite o valor do saque: "))

    if (value > LIMIT):
        print("Valor diário de saque excedido, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return
    
    elif (number_withdrawal >= LIMIT_WITHDRAWAL):
        print("Limite diário de saques excedido, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return

    elif (value > balance):
        print("Saldo insuficiente, tente novamente mais tarde!")
        input("\nPressione Enter para continuar...")
        return

    else:
        balance -= value
        print(f"\n   Saldo: R$ {balance:.2f}\n   Sacado: R$ {value:.2f}")
        number_withdrawal += 1

        if len(entries) > 0:
            for entry in entries:
                if new_date in entry:
                    entry[new_date].append(value)
                else:
                    entry[new_date] = [value]
        else:
            entries.append({new_date: [value]})
        
        print("\n\nSaque realizado com sucesso!")
        input("\nPressione Enter para continuar...")


def display() -> None:
    global balance, extract
    
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
    deposit = False
    while True:
        clear()
        print(MENU)
        option = input()

        if option == "q":
            break

        elif option == "d":
           place()               

        elif option == "s":
            withdraw()

        elif option == "e":
            display()


if __name__ == "__main__":
    main()