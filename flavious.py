while True:
    try:
        def proximo_disponivel(array, posicoes):
            cont = 0
            percorrer = posicoes + 1
            while percorrer != posicoes:
                percorrer = (percorrer + 1) % posicoes
                cont += 1
                if array[percorrer]:
                    return cont
            return cont

        quantidade_testes = int(input(""))

        for x in range(1, quantidade_testes + 1):
            entrada = input("").split()
            numero_homens = int(entrada[0])
            salto = int(entrada[1])
            array = [1 for i in range(1, numero_homens + 1)]

            morte = salto

            for k in range(1, numero_homens):


                if array[morte] == 1:
                    array[morte] = 0
                else:
                    morte = (morte + salto) % numero_homens
                    for c in range(0, salto):
                        morte = proximo_disponivel(array, numero_homens)
                        print(morte)


            numero_vivo = numero_homens

            if array[0] == 0:
                for c in range(1, numero_homens):
                    if array[c]:
                        numero_vivo = (c - 1) % numero_homens

            print(f"Case {x}: {numero_vivo}")



    except EOFError:
        break
