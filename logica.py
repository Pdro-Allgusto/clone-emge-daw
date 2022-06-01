
while True:
    try:
        entrada = input("").split(" ")
        comprimento_total = int(entrada[0])
        velocidade_ana = float(entrada[1]) / 100
        velocidade_bia = int(entrada[2]) / 100
        tempo_chegada_khan = int(entrada[3]) * 60
        distancia_inicio = int(entrada[4])

        pri_volta_tempo_ana = (comprimento_total - distancia_inicio) / velocidade_ana
        pri_volta_tempo_bia = (comprimento_total - distancia_inicio) / velocidade_bia

        if tempo_chegada_khan == 0 and distancia_inicio == 0:           # Khan chega no inicio e elas começam a corrida no inicio
            print("Ana")
        elif tempo_chegada_khan == 0:                                   # Khan chega no inicio e elas começam a corrida depois
            if pri_volta_tempo_ana > pri_volta_tempo_bia:
                print("Bia")
            else: 
                print("Ana")
        elif pri_volta_tempo_ana > tempo_chegada_khan:                  # volta incompleta
            tempo_khan_ana = pri_volta_tempo_ana - tempo_chegada_khan
            tempo_khan_bia = pri_volta_tempo_bia - tempo_chegada_khan
            if tempo_khan_ana > tempo_khan_bia:
                print("Bia")
            else:
                print("Ana")
        else:                                                           # Mais que uma volta, elas começam e Khan chega depois
            tempo_volta_ana = comprimento_total / velocidade_ana
            tempo_volta_bia = comprimento_total / velocidade_bia

            k = 0
            while (pri_volta_tempo_ana + (tempo_volta_ana * k) < tempo_chegada_khan):
                k += 1
            
            x = 0
            while (pri_volta_tempo_bia + (tempo_volta_bia * x) < tempo_chegada_khan):
                x += 1

            tempo_khan_ana = tempo_chegada_khan - (pri_volta_tempo_ana + (tempo_volta_ana * k))

            tempo_khan_bia = tempo_chegada_khan - (pri_volta_tempo_bia + (tempo_volta_bia * x))
            if abs(tempo_khan_ana) > abs(tempo_khan_bia):
                print("Bia")
            else:
                print("Ana")
    
    except EOFError:
        break