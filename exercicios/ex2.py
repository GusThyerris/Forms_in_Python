# 2)Faça o exercício 1, só que agora crie três funções que retornem o valor do comprimento,
# área e do volume. Depois, faça a média aritimética dos volumes de 3 esferas com raio 30, 40 e 50mm.

def calcular_comprimento(raio):
    return 2 * raio

def calcular_area(raio):
    return raio ** 2

def calcular_volume(raio):
    return (4/3) * 3.141592 * raio ** 3

raios = [30, 40, 50]
volumes = [calcular_volume(raio) for raio in raios]

media_volumes = sum(volumes) / len(volumes)
print("Média do volume das esferas: ", media_volumes)