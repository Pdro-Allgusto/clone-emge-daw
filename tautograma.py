while True:
    try:
        tautograma = input("").lower().split()
        primeiro_char = tautograma[0][0:1]
        if primeiro_char != "*":
            status = "Y"
            for palavras in tautograma:
                if palavras[0:1] != primeiro_char:
                    status = "N"
            print(status)
    except EOFError:
        break