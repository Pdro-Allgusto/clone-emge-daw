while True:
    try:
        entrada = input().split()
        total = int(entrada[0])
        quant_voltaram = int(entrada[1])
        quem_voltou = [False for c in range(0, total+1)]
        quem_voltou[0] = True
        voltaram_string = input("").split()
        voltaram = [int(x) for x in voltaram_string]
        for pessoas_voltaram in voltaram:
            quem_voltou[pessoas_voltaram] = True
        quem_nao_voltou = ""
        for x in range(0, len(quem_voltou)):
            if not quem_voltou[x]:
                quem_nao_voltou += str(x) + " "
        if not len(quem_nao_voltou):
            quem_nao_voltou = "*"
        print(quem_nao_voltou)

    except EOFError:
        break