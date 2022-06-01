segEntrada = int(input())
horas = segEntrada // 3600
segundos = (segEntrada % 3600) % 60
minutos = (segEntrada % 3600) // 60
print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")
