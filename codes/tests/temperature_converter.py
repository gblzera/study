#Conversor de Temperatura – Converta graus Celsius para Fahrenheit e vice-versa.

def temperature_converter():
    print("Conversor de Temperatura")
    print("------------------------")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    print("0. Sair")

    choice = int(input("Escolha uma opção: "))
    
    if choice == 1:
        celsius = float(input("Informe a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C equivalem a {fahrenheit}°F")
        temperature_converter()
    elif choice == 2:
        fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F equivalem a {celsius}°C")
        temperature_converter()
    elif choice == 0:
        print("Saindo...")
    else:
        print("Opção inválida!")
temperature_converter()

