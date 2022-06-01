while True:
    try:
        entrada = input("").split(" ")
        comprimento = int(entrada[0])
        velocidade_ana = float(entrada[1]) / 100
        velocidade_bia = int(entrada[2]) / 100
        chegada_khan = int(entrada[3]) * 60
        distancia = int(entrada[4])

        percorre_ana = (velocidade_ana * chegada_khan) - distancia
        percorre_bia = (velocidade_bia * chegada_khan) - distancia

        rest_ana = distancia - (percorre_ana % comprimento)  # resto em metros
        rest_bia = distancia - (percorre_bia % comprimento)

        #rest_bia_true = (rest_bia + distancia_restante) % distancia
        #rest_ana_true = (rest_ana + distancia_restante) % distancia

        if rest_bia == 0:
            print("Bia")
        elif rest_ana == 0:
            print("Ana")
        else:
            tempo_bia = rest_bia / velocidade_bia
            tempo_ana = rest_ana / velocidade_ana
            if tempo_bia > tempo_ana:
                print("Bia")
            else:
                print("Ana")
    except EOFError:
        break
