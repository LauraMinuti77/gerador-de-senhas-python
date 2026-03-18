import random 
import string

# Solicita ao usuário o tamanho da senha
tamanho = int(input("Digite o tamanho da sua senha: "))

# Conjunto de caracteres possíveis: letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Inicializa a senha vazia
senha = "" 

# Gera a senha escolhendo caracteres aleatórios
for i in range(tamanho):
    senha += random.choice(caracteres)

# Exibe a senha gerada
print("Senha gerada:", senha)
