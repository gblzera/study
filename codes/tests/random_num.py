import random

def generate_random_number():
    return random.randint(1, 100)

number = generate_random_number()

print("Digite um número entre 1 - 100.")

while True:
    try:
        guess = int(input("Sua aposta: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
    
    if guess < number:
        print("Número muito baixo, tente novamente.")
    elif guess > number:
        print("Número muito alto, tente novamente.")
    else:
        print(f"Você acertou! O número era {number}.")
        break