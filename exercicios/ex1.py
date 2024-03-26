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

raio = float(input("Digite o raio da esfera: "))

comprimento = 2 * raio
print("Comprimento da esfeta: ", comprimento)

area = raio ** 2
print("Área da esfera: ", area)

volume = (4/3) * 3.14159265359 * raio ** 3
print("Volume da esfera: ", volume)