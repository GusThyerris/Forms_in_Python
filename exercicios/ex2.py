# 2)Faça o exercício 1, só que agora crie três funções que retornem o valor do comprimento,
# área e do volume. Depois, faça a média aritimética dos volumes de 3 esferas com raio 30, 40 e 50mm.

# Criação da função que executará o calculo do comprimento
def calcular_comprimento(raio):
    return 2 * raio

# Criação da função que executará o calculo da área
def calcular_area(raio):
    return raio ** 2

# Criação da função que executará o calculo do volume(considerando pi = 3.141592)
def calcular_volume(raio):
    return (4/3) * 3.141592 * raio ** 3

# Atribuindo valores ao vetor raio, depois calculando o volume com cada valor do vetor
raios = [30, 40, 50]
volumes = [calcular_volume(raio) for raio in raios]

# Criando a variável que recebe o calculo da média aritmética dos volumes, depois imprimindo o valor para o usuário
media_volumes = sum(volumes) / len(volumes)
print("Média do volume das esferas: ", media_volumes)