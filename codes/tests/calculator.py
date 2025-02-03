import numpy as np
import math

def calculator():
    while True:
        print("\nSelecione uma operação:") #printa na tela todas as opções
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Potenciação (**)")
        print("6 - Raíz quadrada (√)")
        print("7 - Fatorial (!)")
        print("8 - Logaritmo natural (ln)")
        print("0 - Sair")

        choose = input("Digite o número da operação desejada:") #pede ao usuario qual operação ele deseja fazer

        if choose == '0': #verifica se a opção é 5 (sair) e fecha o programa
            print("Saindo...")
            break
        if choose not in ('1', '2', '3', '4', '5', '6', '7', '8'): #verifica se a opção está fora das possiveis, caso sim, retorna operação invalida e questiona novamente
            print("Opção inválida!")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))#pede ao usuario o primeiro número, apenas aceita numeros
            if choose in ('1', '2', '3', '4', '5'):
                 num2 = float(input("Digite o segundo número: ")) #pede ao usuario o segundo número, apenas aceita numeros
        except ValueError:
            print("Entrada inválida! Digite números válidos.")
            continue

        if choose == '1': #soma
            result = num1 + num2
            operator = '+'
        elif choose == '2': #subtração
            result = num1 - num2
            operator = '-'
        elif choose == '3': #multiplicação
            result = num1 * num2
            operator = '*'
        elif choose == '4': #divisão
            if num2 == 0:
                print("Divisão por zero!")
                continue
            result = num1 / num2
            operator = '/'
        elif choose == '5': #potenciação
            result = num1 ** num2
            operator = '**'
        elif choose == '6': #raiz quadrada
            if num1 < 0:
                print("Raiz quadrada de número negativo!")
                continue
            result = np.sqrt(num1)
            operator = '√'
        elif choose == '7': #fatorial
            result = math.factorial(int(num1))
            operator = '!'
        elif choose == '8': #logaritmo natural
            if num1 <= 0:
                print("Logaritmo de número negativo ou zero!")
                continue
            result = np.log(num1)
            operator = 'ln'
        
         
        print(f"{num1} {operator} {num2 if choose in ('1', '2', '3', '4', '5')else ''} = {result}") #printa na tela o resultado da operação

if __name__ == '__main__': #chama a função calculator
    calculator()