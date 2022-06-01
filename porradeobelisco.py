while True:
    try:
        entrada = input("").split(" ")
        comprimento_total = int(entrada[0])
        velocidade_ana = float(entrada[1]) / 100
        velocidade_bia = int(entrada[2]) / 100
        tempo_chegada_khan = int(entrada[3]) * 60
        distancia_inicio = int(entrada[4])

        # metros e segundos

        # khan chegou tempo 0
        # mesma velocidade

        # distancian_khan = comprimento_total - distancia_inicio

        percorre_ana = velocidade_ana * tempo_chegada_khan  # qt. percorrida antes da chegada
        percorre_bia = velocidade_bia * tempo_chegada_khan

        if tempo_chegada_khan == 0 and distancia_inicio == 0:
            print("Ana")
        else:
            if tempo_chegada_khan == 0:
                local_ana = distancia_inicio
                local_bia = distancia_inicio
            else:
                local_ana = ((percorre_ana % comprimento_total) + distancia_inicio) % comprimento_total  # local (em metros) onde ela está na chegada do Khan
                local_bia = ((percorre_bia % comprimento_total) + distancia_inicio) % comprimento_total

            rest_ana = comprimento_total - local_ana  # distancia que falta para chegar ao Khan
            rest_bia = comprimento_total - local_bia

            if local_ana == 0:
                print("Ana")
            elif local_bia == 0:
                print("Bia")
            else:
                tempo_ana = rest_ana / velocidade_ana  # tempo que falta para chegar ao Khan
                tempo_bia = rest_bia / velocidade_bia
                if tempo_bia < tempo_ana:
                    print("Bia")
                else:
                    print("Ana")
    except EOFError:
        break

