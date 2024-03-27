# 1) Faça um progama que receba o raio de uma esfera, calcule e mostre:
#
# a) o comprimento de uma esfera ;
# sabe-se que C = 2 x R;
# 
# b) a área de uma esfera;
# sabe-se que A = R;
#  
# c) o volume de uma esfera;
# sabe-se que V = (4/3) x R³.
# 
# obs.: sem usar a idéia da função.
# 

# Criação da variável raio e atribuíção do valor como um número real digitado pelo usuário
raio = float(input("Digite o raio da esfera: "))

# Criação da variável comprimento e atribuindo a formula, depois imprimindo o valor
comprimento = 2 * raio
print("Comprimento da esfeta: ", comprimento)

# Criação da variável area e atribuindo a formula, depois imprimindo o valor
area = raio ** 2
print("Área da esfera: ", area)

# Criação da variável volume e atribuindo a formula(considerando pi = 3.14159265359), depois imprimindo o valor
volume = (4/3) * 3.14159265359 * raio ** 3
print("Volume da esfera: ", volume)