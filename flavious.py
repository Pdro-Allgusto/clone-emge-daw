while True:
    try:
        quantidade_testes = int(input(""))

        for x in range(1, quantidade_testes + 1):
            entrada = input("").split()
            numero_homens = int(entrada[0])
            salto = int(entrada[1])
            array = [1 for i in range(1, numero_homens + 1)]

            morte = salto

            for k in range(1, numero_homens):
                if array[morte] == 0:
                    pulo = 0
                    while pulo != salto:
                        morte = (morte + 1) % numero_homens
                        if array[morte]:
                            pulo += 1
                if array[morte] == 1:
                    array[morte] = 0

            numero_vivo = numero_homens

            if array[0] == 0:
                for c in range(1, numero_homens):
                    if array[c]:
                        numero_vivo = c

            print(f"Case {x}: {numero_vivo}")

    except EOFError:
        break
