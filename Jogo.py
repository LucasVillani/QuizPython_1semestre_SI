import random
import time
import sys
print("Regras do Jogo:\n1-")

input("Aperte ENTER para começar")
print("\n\n")
time.sleep(1)
dificuldade = input("Escolha uma dificuldade(facil, normal ou dificil): ")
while dificuldade != "normal" and dificuldade != "normal" and dificuldade != "dificil":
    print("Comando invalido")
    dificuldade = input("Escolha uma dificuldade(facil, normal ou dificil): ")
time.sleep(1)
if dificuldade == "facil":

#facil


    palavras = [1,2,3,4,6,7,8,9]
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i=1
    dica = 1
    respostas = 3
    dicas = 5
    bonus = 0


    if palavra == 1:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <=6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica+=1
                dicas-=1
                i+=1


            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (1/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print("Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (1/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

     ###############################################PALAVRA2###########################################
    print("\n")
    print("Proxima palavra...")
    print("\n")
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    dicas = 5
    respostas = 3
    if palavra == 1:
        print("Palavra (2/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <=6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica+=1
                dicas-=1
                i+=1


            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (2/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (2/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (2/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (2/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print("Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (2/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (2/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (2/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))
    #################################################PALAVRA3###########################################
    print("\n")
    print("Proxima palavra...")
    print("\n")
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dicas = 5
    dica = 1
    respostas = 3
    if palavra == 1:
        print("Palavra (3/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <=6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica+=1
                dicas-=1
                i+=1


            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (3/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (3/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (3/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (3/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print("Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (3/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (3/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (3/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <=6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if i !=6 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica+=1
                dicas-=1
                i+=1

            elif i == 6 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas+1

        print("Vc possui {} dicas bonus".format(bonus))


    ####################################################PALAVRA4##################################
    time.sleep(0.25)
    print("\n")
    print("Voce esta prestes a tentar adivinhar a ultima palavra, lembrando que voce tem direito a no maximo {} dicas bonus aleatorias para acerta-la".format(bonus))
    time.sleep(0.25)
    print("\n")
    palavras = [1]
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    dicas = bonus
    respostas = 3
    dicas_aleatorias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    if palavra == 1:
        print("Palavra (4/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        k=1
        while k ==1:
            print("Dicas bonus restantes: {}, tentativas de respostas restantes {}".format(dicas,respostas))
            escolha = input("Mais um DICA aleatoria ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas > 0 and escolha == "DICA":
                dica_aleatoria = random.choice(dicas_aleatorias)
                dicas_aleatorias.remove(dica_aleatoria)
                if dica_aleatoria == 1:
                    print("Dica: Os Homo erectus ja me habitaram a cerca de 500.000 a.C")
                if dica_aleatoria == 2:
                    print("Dica: Sou um país de clima tropical")
                if dica_aleatoria == 3:
                    print("Dica: Estou localizado no Sudeste Asiático")
                if dica_aleatoria == 4:
                    print("Dica: Minha moeda se chama Dongue")
                if dica_aleatoria == 5:
                    print("Dica: Estou situado na peninsula de Indochina")
                if dica_aleatoria == 6:
                    print("Dica: Me tornei independente em 938, porem fui novamente colonizada no seculo XIX")
                if dica_aleatoria == 7:
                    print("Dica: Devido a mudança na minha economia desde 1986, ocupo atualmente o  11º lugar nas economias de mais rápido crescimento.")
                if dica_aleatoria == 8:
                    print("Dica: A inflação, saúde, desigualdade e pobreza são sérios problemas q eu enfrento")
                if dica_aleatoria == 9:
                    print("Dica: Sou uma Repúblia Socialista")
                if dica_aleatoria == 10:
                    print("Dica: Faço fronteira com a República Popular da China, com Laos, com o Camboja e com o golfo da Tailândia ")
                if dica_aleatoria == 11:
                    print("Dica: Fiquei dividido por anos em 2 partes: Sul e Norte, porém em 1976, fui unificada para um unico país Socialista")
                if dica_aleatoria == 12:
                    print("Dica: Fui um palco de guerra entre os anos de 1961 à 1976")
                if dica_aleatoria == 13:
                    print("Dica: Os EUA e a URSS já protagonizaram uma guerra em meu territorio")
                if dica_aleatoria == 14:
                    print("Dica: Fui um dos palcos da Guerra Fria")
                if dica_aleatoria == 15:
                    print("Dica: Minha letra inicial eh V")
                if dica_aleatoria == 16:
                    print("Dica: Meu nome tem 6 letras")



                dicas-=1
                i+=1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas aleatorias disponiveis")
                print("\n")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VIETNA" or resposta == "VIETNÃ":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas-=1

            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if respostas == 0:
                print("Game Over")
                sys.exit()
        bonus+=dicas
    time.sleep(0.25)
    print("\n")
    print("Calculando o resultado do jogo",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".",end="")
    time.sleep(0.3)
    print(".")
    time.sleep(0.25)
    print("\n")
    print("Vc venceu o jogo com {} dicas bonus restantes!!!".format(bonus))
    time.sleep(0.15)
    if bonus <=1:
        print("Vc eh Esperto!!!")
    if bonus <=3:
        print("Vc eh um Mestre!!!")
    else:
        print("Vc eh um DEUS!!!")

if dificuldade == "normal":

    palavras = [1, 2, 3, 4, 6, 7, 8, 9]
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    respostas = 3
    dicas = 4
    bonus = 0

    if palavra == 1:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <= 6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica += 1
                dicas -= 1
                i += 1


            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (1/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print(
                        "Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print("Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (1/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    ###############################################PALAVRA2###########################################
    print("\n")
    print("Proxima palavra...")
    print("\n")
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    respostas = 3
    dicas = 4
    bonus = 0

    if palavra == 1:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <= 6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica += 1
                dicas -= 1
                i += 1


            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (1/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print("Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (1/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))
    #################################################PALAVRA3###########################################
    print("\n")
    print("Proxima palavra...")
    print("\n")
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    respostas = 3
    dicas = 4
    bonus = 0

    if palavra == 1:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <= 6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica += 1
                dicas -= 1
                i += 1


            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (1/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print(
                        "Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print(
                        "Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (1/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    ####################################################PALAVRA4##################################
    time.sleep(0.25)
    print("\n")
    print(
        "Voce esta prestes a tentar adivinhar a ultima palavra, lembrando que voce tem direito a no maximo {} dicas bonus aleatorias para acerta-la".format(
            bonus))
    time.sleep(0.25)
    print("\n")
    palavras = [1,2,3]
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    dicas = bonus
    respostas = 3
    dicas_aleatorias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    if palavra == 1:
        print("Palavra (4/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        k = 1
        while k == 1:
            print("Dicas bonus restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA aleatoria ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas > 0 and escolha == "DICA":
                dica_aleatoria = random.choice(dicas_aleatorias)
                dicas_aleatorias.remove(dica_aleatoria)
                if dica_aleatoria == 1:
                    print("Dica: Os Homo erectus ja me habitaram a cerca de 500.000 a.C")
                if dica_aleatoria == 2:
                    print("Dica: Sou um país de clima tropical")
                if dica_aleatoria == 3:
                    print("Dica: Estou localizado no Sudeste Asiático")
                if dica_aleatoria == 4:
                    print("Dica: Minha moeda se chama Dongue")
                if dica_aleatoria == 5:
                    print("Dica: Estou situado na peninsula de Indochina")
                if dica_aleatoria == 6:
                    print("Dica: Me tornei independente em 938, porem fui novamente colonizada no seculo XIX")
                if dica_aleatoria == 7:
                    print("Dica: Devido a mudança na minha economia desde 1986, ocupo atualmente o  11º lugar nas economias de mais rápido crescimento.")
                if dica_aleatoria == 8:
                    print("Dica: A inflação, saúde, desigualdade e pobreza são sérios problemas q eu enfrento")
                if dica_aleatoria == 9:
                    print("Dica: Sou uma Repúblia Socialista")
                if dica_aleatoria == 10:
                    print("Dica: Faço fronteira com a República Popular da China, com Laos, com o Camboja e com o golfo da Tailândia ")
                if dica_aleatoria == 11:
                    print("Dica: Fiquei dividido por anos em 2 partes: Sul e Norte, porém em 1976, fui unificada para um unico país Socialista")
                if dica_aleatoria == 12:
                    print("Dica: Fui um palco de guerra entre os anos de 1961 à 1976")
                if dica_aleatoria == 13:
                    print("Dica: Os EUA e a URSS já protagonizaram uma guerra em meu territorio")
                if dica_aleatoria == 14:
                    print("Dica: Fui um dos palcos da Guerra Fria")
                if dica_aleatoria == 15:
                    print("Dica: Minha letra inicial eh V")
                if dica_aleatoria == 16:
                    print("Dica: Meu nome tem 6 letras")

                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas aleatorias disponiveis")
                print("\n")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VIETNA" or resposta == "VIETNÃ":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1

            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas
    time.sleep(0.25)
    print("\n")
    print("Calculando o resultado do jogo", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".")
    time.sleep(0.25)
    print("\n")
    print("Vc venceu o jogo com {} dicas bonus restantes!!!".format(bonus))
    time.sleep(0.15)
    if bonus <= 1:
        print("Vc eh Esperto!!!")
    if bonus <= 3:
        print("Vc eh um Mestre!!!")
    else:
        print("Vc eh um DEUS!!!")
if dificuldade == "dificil":

    palavras = [1, 2, 3, 4, 6, 7, 8, 9]
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    respostas = 3
    dicas = 3
    bonus = 0

    if palavra == 1:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <= 6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica += 1
                dicas -= 1
                i += 1


            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (1/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print(
                        "Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print("Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (1/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    ###############################################PALAVRA2###########################################
    print("\n")
    print("Proxima palavra...")
    print("\n")
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    respostas = 3
    dicas = 3
    bonus = 0

    if palavra == 1:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <= 6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica += 1
                dicas -= 1
                i += 1


            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (1/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print(
                        "Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print(
                        "Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (1/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))
    #################################################PALAVRA3###########################################
    print("\n")
    print("Proxima palavra...")
    print("\n")
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    respostas = 3
    dicas = 3
    bonus = 0

    if palavra == 1:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        while i <= 6:
            time.sleep(0.5)
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Faço fronteira com o Brasil, especificamente com Acre e Amazonas")
                if dica == 2:
                    print("Meu principal ponto turístico está em cima de uma montanha")
                if dica == 3:
                    print("Tanto meu nome como minha capital são nomes também ligados a culinária")
                if dica == 4:
                    print("Meu nome tem 4 letras")
                if dica == 5:
                    print("Um dos times de futebol no meu país se chama Alianza Lima ")
                dica += 1
                dicas -= 1
                i += 1


            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "PERU":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 2:
        print("Palavra (1/4)\nEssa palavra eh um PAÍS")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Fui um dos protagonistas das 2 Guerras Mundiais")
                if dica == 2:
                    print("Dica: Estou situado na Europa")
                if dica == 3:
                    print("Dica: Minha chanceler eh tida como uma das mulheres mais poderosas do mundo")
                if dica == 4:
                    print("Dica: Possuo o titulo de 4 Copas do Mundo")
                if dica == 5:
                    print("Dica: Fui governado por um regime ditatorial chamado Nazismo")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "ALEMANHA":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 3:
        print("Palavra (1/4)\nEssa palavra eh uma cidade")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou a capital de um importante país europeu")
                if dica == 2:
                    print("Dica: A primeira ministra do meu país se chama Theresa May")
                if dica == 3:
                    print("Dica: Possuo a mais extensa rede ferroviária subterrânea do mundo")
                if dica == 4:
                    print("Dica: Possuo em meu territorio o Palácio de Buckingham")
                if dica == 5:
                    print("Dica: Um importante ponto turístico meu se chama Big Ben ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "LONDRES":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 4:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            print("\n")
            time.sleep(0.5)
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou um ditador")
                if dica == 2:
                    print("Dica: Minha ideologia causou em meu país diversas mortes, muitas inclusive for fome")
                if dica == 3:
                    print("Dica: Fui um dos protagonistas da Segunda Guerra Mundial")
                if dica == 4:
                    print("Dica: Sigo a ideologia proposta por Karl Marx")
                if dica == 5:
                    print("Dica: Fuí líder da União Soviética")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "STALIN":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 6:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print(
                        "Dica: Estou situado no norte da África, porém possuo uma peninsula na Ásia, o que me faz uma país transcontinental")
                if dica == 2:
                    print("Dica: Sou banhado pelos mares Mediterrâneo e Vermelho")
                if dica == 3:
                    print("Dica: Minha capital se chama Cairo")
                if dica == 4:
                    print(
                        "Dica: Meus monumentos são alvos de estudos até hoje, sendo também um dos principais pontos turísticos do mundo")
                if dica == 5:
                    print("Dica: Meu clima é marcado por ser desertico")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "EGITO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 7:
        print("Palavra (1/4)\nEssa palavra eh uma pessoa ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Nasci em 1929, em Atlanta, nos Estados Unidos")
                if dica == 2:
                    print("Dica: Por muito tempo fui o mais jovem ganhador do Prêmio Nobel com 35 anos")
                if dica == 3:
                    print("Dica: Sou uma das pessoas mais influentes de minha etnia")
                if dica == 4:
                    print("Dica: Fui assassinado a 7 tiros")
                if dica == 5:
                    print("Dica: Um discurso feito por mim ficou muito famoso, junto com a frase ``I have a dream´´")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "MARTIN LUTHER KING":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 8:
        print("Palavra (1/4)\nEssa palavra eh uma cidade ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma capital de um estado brasileiro ")
                if dica == 2:
                    print("Dica: Possuo o primeiro elevador do Brasil")
                if dica == 3:
                    print("Dica: Fui a primeira capital do Brasil")
                if dica == 4:
                    print("Dica: Sou a terra do carnaval")
                if dica == 5:
                    print("Dica: Estou localizado no nordeste ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "SALVADOR":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    if palavra == 9:
        print("Palavra (1/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        while i <= 6:
            print("Dicas restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas != 0 and escolha == "DICA":
                if dica == 1:
                    print("Dica: Sou uma cidade-Estado")
                if dica == 2:
                    print("Dica: Estou localizada na Europa")
                if dica == 3:
                    print("Dica: Sou considerado o menor país existente")
                if dica == 4:
                    print("Dica: Minhas linguas oficiais sao italiano e latim")
                if dica == 5:
                    print("Dica: Sou a sede da Igreja Catolica ")
                dica += 1
                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas disponiveis")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VATICANO":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1


            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if i == 7 or respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas + 1

        print("Vc possui {} dicas bonus".format(bonus))

    ####################################################PALAVRA4##################################
    time.sleep(0.25)
    print("\n")
    print(
        "Voce esta prestes a tentar adivinhar a ultima palavra, lembrando que voce tem direito a no maximo {} dicas bonus aleatorias para acerta-la".format(
            bonus))
    time.sleep(0.25)
    print("\n")
    palavras = [1,2,3]
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    i = 1
    dica = 1
    dicas = bonus
    respostas = 3
    dicas_aleatorias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    if palavra == 1:
        print("Palavra (4/4)\nEssa palavra eh um país ")
        print("\n")
        time.sleep(0.5)
        k = 1
        while k == 1:
            print("Dicas bonus restantes: {}, tentativas de respostas restantes {}".format(dicas, respostas))
            escolha = input("Mais um DICA aleatoria ou deseja tentar uma RESPOSTA?: ")
            time.sleep(0.5)
            print("\n")
            escolha = escolha.upper()
            placar = 0
            if dicas > 0 and escolha == "DICA":
                dica_aleatoria = random.choice(dicas_aleatorias)
                dicas_aleatorias.remove(dica_aleatoria)
                if dica_aleatoria == 1:
                    print("Dica: Os Homo erectus ja me habitaram a cerca de 500.000 a.C")
                if dica_aleatoria == 2:
                    print("Dica: Sou um país de clima tropical")
                if dica_aleatoria == 3:
                    print("Dica: Estou localizado no Sudeste Asiático")
                if dica_aleatoria == 4:
                    print("Dica: Minha moeda se chama Dongue")
                if dica_aleatoria == 5:
                    print("Dica: Estou situado na peninsula de Indochina")
                if dica_aleatoria == 6:
                    print("Dica: Me tornei independente em 938, porem fui novamente colonizada no seculo XIX")
                if dica_aleatoria == 7:
                    print("Dica: Devido a mudança na minha economia desde 1986, ocupo atualmente o  11º lugar nas economias de mais rápido crescimento.")
                if dica_aleatoria == 8:
                    print("Dica: A inflação, saúde, desigualdade e pobreza são sérios problemas q eu enfrento")
                if dica_aleatoria == 9:
                    print("Dica: Sou uma Repúblia Socialista")
                if dica_aleatoria == 10:
                    print("Dica: Faço fronteira com a República Popular da China, com Laos, com o Camboja e com o golfo da Tailândia ")
                if dica_aleatoria == 11:
                    print("Dica: Fiquei dividido por anos em 2 partes: Sul e Norte, porém em 1976, fui unificada para um unico país Socialista")
                if dica_aleatoria == 12:
                    print("Dica: Fui um palco de guerra entre os anos de 1961 à 1976")
                if dica_aleatoria == 13:
                    print("Dica: Os EUA e a URSS já protagonizaram uma guerra em meu territorio")
                if dica_aleatoria == 14:
                    print("Dica: Fui um dos palcos da Guerra Fria")
                if dica_aleatoria == 15:
                    print("Dica: Minha letra inicial eh V")
                if dica_aleatoria == 16:
                    print("Dica: Meu nome tem 6 letras")

                dicas -= 1
                i += 1

            elif dicas == 0 and escolha == "DICA":
                print("Vc n possui mais dicas aleatorias disponiveis")
                print("\n")

            elif escolha == "RESPOSTA":
                resposta = input("Resposta: ")
                resposta = resposta.upper()
                if resposta == "VIETNA" or resposta == "VIETNÃ":
                    print("Vc acertou!!!")
                    break
                else:
                    print("Vc errou!!!")
                    respostas -= 1

            else:
                print("Comando Invalido")
            print("\n")
            time.sleep(1)

            if respostas == 0:
                print("Game Over")
                sys.exit()
        bonus += dicas
    time.sleep(0.25)
    print("\n")
    print("Calculando o resultado do jogo", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".", end="")
    time.sleep(0.3)
    print(".")
    time.sleep(0.25)
    print("\n")
    print("Vc venceu o jogo com {} dicas bonus restantes!!!".format(bonus))
    time.sleep(0.15)
    if bonus <= 1:
        print("Vc eh Esperto!!!")
    if bonus <= 3:
        print("Vc eh um Mestre!!!")
    else:
        print("Vc eh um DEUS!!!")
















