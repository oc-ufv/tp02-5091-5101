import functions.montador as mont

def lerArquivo(arquivo):
    print("arq => ", arquivo)
    
    try:
        nomeArq = str(arquivo).replace(".asm", "")
        with open("../entrada/assembler.bin", "w") as arq1:
            arq1.truncate(0)
            arq1.close()

        # with open("Montador_assembly/Arquivos_saida/Binario/output_"+ nomeArq +".txt", "w") as arq1:
        #     arq1.truncate(0)
        #     arq1.close()
        # with open("Montador_assembly/Arquivos_saida/Hexadecimal/output_"+ nomeArq +".txt", "w") as arq1:
        #     arq1.truncate(0)
        #     arq1.close()
        # with open("Montador_assembly/Arquivos_saida/Octal/output_"+ nomeArq +".txt", "w") as arq1:
        #     arq1.truncate(0)
        #     arq1.close()
            
        with open("Arquivos_teste/"+arquivo) as arq:
            texto = arq.readlines()
            print("\nConteudo:")
            #variavel para armzenar cada linha do comando em assembly
            x = ''
            for linha in texto :
                linha = linha.replace("\n","") #removendo "\n"
                print(linha)
                linha = linha.replace(",","") #removendo vírgulas
                linha = linha.replace("("," ") #removendo parenteses
                linha = linha.replace(")"," ")  #removendo parenteses
                linha = linha.split(" ")
                num = 1
                mont.indentificar_funcao(linha, num, arquivo)
        
            linha = "00000000000000000000000000000000"        
            with open("../entrada/assembler.bin", "a") as _arq:
                _arq.write(linha)
                _arq.close()

            arq.close()

    except FileNotFoundError:
        msg = "Infelizmente, o arquivo " + arquivo + " não existe!"
        print(msg)

def tratarConteudo(instrucao):
    #removendo vírgulas
    x = ''
    instrucao = instrucao.replace(",","")
    #removendo "\n"
    instrucao = instrucao.replace("\n","")
    #armazendo cada comando em uma posição do vetor
    #x = instrucao.split(" ")
    #identificando cada instrução
    #removendo parenteses
    instrucao = instrucao.replace("("," ")
    instrucao = instrucao.replace(")"," ")
    instrucao = instrucao.split(" ")
    num = 2
    mont.indentificar_funcao(instrucao, num, x)

def mostrar_conteudo(x):
    print("")
    # try:
    #     print("")
    #     nomeArq = str(x).replace(".asm", "")
    #     with open("../Projeto/entrada/assembler.bin") as arq1:
    #         mostrar = arq1.read()
    #         print(mostrar)  
    #     arq1.close()
    # except FileNotFoundError:
    #     msg = "Infelizmente, ocorreu um erro no arquivo de saida!"
    #     print(msg)