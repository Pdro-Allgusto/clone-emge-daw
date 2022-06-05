while True:
    try:
        quantidade_testes = int(input(""))

        for x in range(1, quantidade_testes + 1):
            entrada = input("").split()
            numero_homens = int(entrada[0])
            salto = int(entrada[1])
            array = ""
            for c in range(0, numero_homens):
                array += "1"

            morte = salto

            for k in range(1, numero_homens):
                fimString = (morte + 1) % numero_homens
                if array[morte:fimString] == "0":
                    pulo = 0
                    while pulo != salto:
                        morte = (morte + 1) % numero_homens
                        if array[morte:fimString] == "1":
                            pulo += 1
                if array[morte:fimString] == "1":
                    array[morte:fimString] = "0"

            print(array)

            numero_vivo = numero_homens

            if array[0] == 0:
                for c in range(1, numero_homens):
                    if array[c]:
                        numero_vivo = c

            print(f"Case {x}: {numero_vivo}")

    except EOFError:
        break
