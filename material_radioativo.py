"""CÓDIGO PARA CALCULAR O TEMPO DE MEIA-VIDA DE UM MATERIAL RADIOATIVO"""
#Inserção de valores
massa = float(input())
tempo = 0

#Laço para calcular enquanto a massa for maior que 0,5 gramas
while massa > 0.5:
    massa /= 2
    tempo += 50

# Cálculo do tempo em horas, minutos e segundos
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60
print(f"{horas}h {minutos}m {segundos}s")