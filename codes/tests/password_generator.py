import random
import string

def generate_random_password(length=12):
    # Define all possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(characters) for _ in range(length))
    return senha

# pergunta ao usuario o tamanho da senha desejada
try:
    lenghtSenha = int(input("Digite o tamanho da senha desejada: "))
    if lenghtSenha < 6:
        print("O tamanho mínimo recomendado é 6 caracteres")
        lenghtSenha = 6 
except ValueError:
    print("Entrada inválida, usando tamanho padrão de 12 caracteres")
    lenghtSenha = 12

#gera e exibe a senha

senha = generate_random_password(lenghtSenha)
print(f"Sua senha gerada é: {senha}")