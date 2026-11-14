#Fazendo lista de exercicios
import subprocess
import os

continuar = True

while continuar == True:
    sistemaEscolhido = input("========> Escolha o sistema que você deseja?: <==========\n"
                             "---------------------------------------------------------\n"
                             "Escolha o sistema que você deseja\n"
                             "\n" 
                             "1 - Calculadora\n"
 
                             "2 - Recebendo idade e imprimindo em diferentes tempos\n"
 
                             "3 - Exibindo o dobro dos números\n"
 
                             "4 - calculo IMC\n"
 
                             "5 - Converta centimetros e polegadas\n"
 
                             "6 - Receba nome, cargo e salário e acrescente 10% \n"
 
                             "7 - Sair\n"
 
                             "\n"           
                             "---------------------------------------------------------\n"
                             "=========================================================\n"
    )

    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    if sistemaEscolhido == "1": 

        while sistemaEscolhido == "1":

            n1 = input("Escolha seu primeiro número: ")
            n2 = input("Escolha seu segundo número: ")

            try: 
                    
                n1 = float(n1)
                n2 = float(n2)
                operação = input("Porfavor escolha sua operação: ( +, -, *, /)")
                if(operação == "+"): 
                    print(f"Resposta: {(n1 + n2):.2f}")
                
                elif(operação == "-"): 
                    print(f"Resposta: {(n1 - n2):.2f}")
                
                elif(operação == "*"): 
                    print(f"Resposta: {(n1 * n2):.2f}")
                
                elif(operação == "/"): 
                    print(f"Resposta: {(n1 / n2):.2f}") 
                else: 
                    print(f"Operação invalida 😵‍💫")
                    

            except ValueError: 
                print("Erro: O input não é um número valido você"
                "provavelmente digitou letras")

            resp = int(input(
            "Deseja continuar usando o sistema?" \
            "\n" 
            "1 - Sim \n"
            "2 - Não \n"))
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            if resp != 1:
                print("obrigado por usar o sistema")
                print("\n")
                sistemaEscolhido = 0        

    elif sistemaEscolhido == "2": 

        while sistemaEscolhido == "2":

            tp = int(input("Escolha o tipo de dado: \n"
            "1 - Idade\n"
            "2 - Ano de nascimento\n"               
            ))

            if tp == 1 :
                idade = int(input("Digite sua idade: " \
                "\n"))
                escolha = input(
                    "=====> Em que tipo de unidade de tempo você deseja?:\n <====\n"
                    "------------------------------------------------------------\n"
                    "\n" 
                    " 1 - Meses\n"
                    " 2 - Dias\n"
                    " 3 - Horas\n"
                    " 4 - Minutos\n"
                    "\n" 
                    "------------------------------------------------------------\n"
                    "============================================================\n")
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

                if escolha == "1":
                    tempo = idade * 12
                    print(f"Sua idade em meses é: {tempo}")
                    print("\n")

                elif escolha == "2":
                    tempo = 0
                    for i in range(1, idade + 1):
                        resultado = i % 4
                        if  resultado != 0:
                            tempo+=365
                        else:
                            tempo+=366
                    print(f"Sua idade em dias é: {tempo}")
                    print("\n")

                elif escolha == "3":
                    tempo = 0
                    for i in range(1, idade + 1):
                        resultado = i % 4
                        if  resultado != 0:
                            tempo+=365
                        else:
                            tempo+=366
                    print(f"Sua idade em horas é: {tempo * 24}")
                    print("\n")

                elif escolha == "4":
                    tempo = 0
                    for i in range(1, idade + 1):
                        resultado = i % 4
                        if  resultado != 0:
                            tempo+=365
                        else:
                            tempo+=366
                    print(f"Sua idade em minutos é: {tempo * 24 * 60}")
                    print("\n")

                elif escolha == "4":
                    tempo = idade * 12 * 4
                    print(f"Sua idade em semanas é: {tempo}")
                    print("\n")

                else: 
                    print(f"opção invalida 😵‍💫")

            if tp == 2 :
                anoAtual = int(input("Digite o ano atual: \n"))
                anoNasc = int(input("Digite o ano em que você nasceu: \n"))
                escolha = input(
                    "=====> Em que tipo de unidade de tempo você deseja?:\n <====\n"
                    "------------------------------------------------------------\n"
                    "\n" 
                    " 1 - Meses\n"
                    " 2 - Dias\n"
                    " 3 - Horas\n"
                    " 4 - Minutos\n"
                    " 5 - Semanas\n"
                    "\n" 
                    "------------------------------------------------------------\n"
                    "============================================================\n"
                    )

                idade = anoAtual - anoNasc
                if escolha == "1":
                            tempo = idade * 12
                            print(f"Sua idade em meses é: {tempo}")
                
                elif escolha == "2":
                    tempo = 0
                    for i in range(1, idade + 1):
                        resultado = i % 4
                        if  resultado != 0:
                            tempo+=365
                        else:
                            tempo+=366
                    print(f"Sua idade em dias é: {tempo}")

                elif escolha == "3":
                    tempo = 0
                    for i in range(1, idade + 1):
                        resultado = i % 4
                        if  resultado != 0:
                            tempo+=365
                        else:
                            tempo+=366
                    print(f"Sua idade em horas é: {tempo * 24}")

                elif escolha == "4":
                    tempo = 0
                    for i in range(1, idade + 1):
                        resultado = i % 4
                        if  resultado != 0:
                            tempo+=365
                        else:
                            tempo+=366
                    print(f"Sua idade em minutos é: {tempo * 24 * 60}")
                elif escolha == "4":
                    tempo = idade * 12 * 4
                    print(f"Sua idade em semanas é: {tempo}")
                else: 
                    print(f"opção invalida 😵‍💫")

            resp = int(input(
                "Deseja continuar usando o sistema?" \
                "\n" 
                "1 - Sim \n"
                "2 - Não \n"))
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            if resp != 1:
                print("obrigado por usar o sistema")
                print("\n")
                sistemaEscolhido = 0        
        

            
    elif sistemaEscolhido == "3": 

        while sistemaEscolhido == "3":
            n1 = float(input("Escolha seu número: "))
            print(f"o dobro do seu número é {(n1 * 2):.2f}")

            resp = int(input(
                "Deseja continuar usando o sistema?" \
                "\n" 
                "1 - Sim \n"
                "2 - Não \n"))
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            if resp != 1:
                print("obrigado por usar o sistema")
                print("\n")
                sistemaEscolhido = 0 

    elif sistemaEscolhido == "4":

        while sistemaEscolhido == "4":
            nome = str(input("Digite seu nome: \n" \
            "\n"))
            peso = float(input("Digite seu peso: "
            "\n"))
            altura = float(input("Digite sua altura: " 
            "\n"))

            Imc = peso / pow(altura, 2)

            print(f"seu IMC é {Imc:.2f}")

            resp = int(input(
                "Deseja continuar usando o sistema?" \
                "\n" 
                "1 - Sim \n"
                "2 - Não \n"))
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            if resp != 1:
                print("obrigado por usar o sistema")
                print("\n")
                sistemaEscolhido = 0 

    elif sistemaEscolhido == "5":

        while sistemaEscolhido == "5":
            escolha = int(input("===========> Que medida você deseja converter? <=============\n"
                                "-------------------------------------------------------------\n"
                                "\n"
                                " 1 - centimetros\n"
                                " 2 - polegadas\n" 
                                "\n"
                                "-------------------------------------------------------------\n"
                                "=============================================================\n"
                                ))

            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            
            if escolha == 1:
                cm = float(input("Digite a medida em cm: " 
                "\n"))
                resultado = cm / 2.54
                print(f"sua medida em polegadas é {resultado:.2f}")

            else:
                pl = float(input("Digite a medida em polegadas: " 
                "\n"))
                resultado = pl * 2.54
                print(f"sua medida em centimetros é {resultado:.2f}")

            print("\n")
            
            resp = int(input(
                        "Deseja continuar usando o sistema?" \
                        "\n" 
                        "1 - Sim \n"
                        "2 - Não \n"))
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            if resp != 1:
                print("obrigado por usar o sistema")
                print("\n")
                sistemaEscolhido = 0 


    elif sistemaEscolhido == "6":

     while sistemaEscolhido == "6":

        nome = str(input("Digite seu nome: \n" \
        "\n"))
        salario = float(input("Digite seu salário: "
        "\n"))
        
        resultado = salario + (salario / 10)

        print(f"seu novo salário é {resultado:.2f}")

        resp = int(input(
                "Deseja continuar usando o sistema?" \
                "\n" 
                "1 - Sim \n"
                "2 - Não \n"))
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        if resp != 1:
            
            print("obrigado por usar o sistema")
            print("\n")
            sistemaEscolhido = 0 

    elif sistemaEscolhido == "7":

        subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
        print("muito obrigado por usar o sistema")
        print("\n")
        continuar = False;

    else:
        print("opção invalida")