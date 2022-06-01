from math import lcm

while True:
    try:
        entrada = input("")
        if entrada == '0':
            break
        entrada = entrada.split(" ")
        quantPagDia = int(entrada[0])
        numeroDias = int(entrada[1])
        novaQuantPag = int(entrada[2])
        mmc = lcm(quantPagDia, novaQuantPag)
        quantPagDia = mmc / quantPagDia
        novaQuantPag = mmc / novaQuantPag
        pag = (numeroDias * mmc) / (quantPagDia - novaQuantPag)
        print(f'{pag:.0f} paginas')
    except EOFError:
        break
