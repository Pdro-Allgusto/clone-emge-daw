while True:
    try:
        primeira_entrada = input("").split()
        segunda_entrada = input("").split()
        status = "Y"
        for k in range(0, len(segunda_entrada)):
            if int(primeira_entrada[k]) + int(segunda_entrada[k]) != 1:
                status = "N"
        print(status)
    except EOFError:
        break