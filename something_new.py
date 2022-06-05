while True:
    try:
        entrada = input("").split(" ")
        comprimento_total = int(entrada[0])
        velocidade_ana = float(entrada[1]) / 100
        velocidade_bia = int(entrada[2]) / 100
        tempo_chegada_khan = int(entrada[3]) * 60
        distancia_inicio = int(entrada[4])

        distancia_complementar = comprimento_total - distancia_inicio
        tempo_pri_ana = distancia_complementar / velocidade_ana
        tempo_pri_bia = distancia_complementar / velocidade_bia

        if tempo_pri_bia >= tempo_chegada_khan or tempo_pri_ana >= tempo_chegada_khan:
            if tempo_pri_ana > tempo_pri_bia:
                print("Bia")
            else:
                print("Ana")
        else:
            tempo_vol_ana = comprimento_total / velocidade_ana
            tempo_vol_bia = comprimento_total / velocidade_bia

            quant_volta_ana = (tempo_chegada_khan - tempo_pri_ana) / tempo_vol_ana
            quant_volta_bia = (tempo_chegada_khan - tempo_vol_bia) / tempo_vol_bia

            tempo_rest_bia = 0
            tempo_rest_ana = 0

            if quant_volta_ana == int(quant_volta_ana) or quant_volta_bia == int(quant_volta_bia):
                if quant_volta_ana == int(quant_volta_ana) and quant_volta_bia == int(quant_volta_bia):
                    print("Ana")
                elif quant_volta_bia == int(quant_volta_bia):
                    print("Bia")
                else:
                    print("Ana")
            else:
                if quant_volta_ana != int(quant_volta_ana):
                    tempo_rest_ana = ((int(quant_volta_ana) + 1) - quant_volta_ana) * tempo_vol_ana

                if quant_volta_bia != int(quant_volta_bia):
                    tempo_rest_bia = ((int(quant_volta_bia) + 1) - quant_volta_bia) * tempo_vol_bia

                tempo_tot_ana = tempo_rest_ana + (quant_volta_ana * tempo_vol_ana) + tempo_pri_ana
                tempo_tot_bia = tempo_rest_bia + (quant_volta_bia * tempo_vol_bia) + tempo_pri_bia

                #prever quanto tempo para terminar a volta, vendo quanto tempo vai faltar arredondando a quant de volta pra cima

                if tempo_tot_ana > tempo_tot_bia:
                    print("Bia")
                else:
                    print("Ana")

    except EOFError:
        break
