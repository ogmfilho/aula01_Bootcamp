# 1) solicta ao usuário que digite seu nome
nome = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número decimal

salario = float(input("Digite o valor do seu salário: "))

# 3 Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número decimal

bonus = float(input("Digite o valor do seu bônus: "))

# 4) Calcula o valor do bônus final
bonus_fixo = 1000
bonus_final = bonus_fixo + (salario * bonus)

# 5) Imprime a mensagem personalizada, incluindo nome do usuário e o valor do bônus

print(f"O usuário {nome} recebeu bônus de R$ {bonus_final}.")
