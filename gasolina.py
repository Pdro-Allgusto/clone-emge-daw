tempoDias = int(input())
ano = tempoDias // 365
dias = (tempoDias % 365) % 30
meses = (tempoDias % 365) // 30
print(f"{ano:.0f} ano(s)\n{meses:.0f} mes(es)\n{dias:.0f} dia(s)")