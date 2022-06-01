from math import lcm
cont = 0
for i in range(1, 20):
    for j in range(1, 20):
        for k in range(1, 20):
            if not k == i:
                quantPagDia = i
                numeroDias = j
                novaQuantPag = k
                mmc = lcm(quantPagDia, novaQuantPag)
                quantPagDia = mmc / quantPagDia
                novaQuantPag = mmc / novaQuantPag
                pag = abs((numeroDias * mmc) / (quantPagDia - novaQuantPag))
                if pag == 8:
                    cont += 1
                    print(f'{i} {j} {k} = {pag}')
print(cont)
