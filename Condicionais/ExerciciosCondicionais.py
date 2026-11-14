


print("|-------------------------------------------------------------------|\n")
print("|------------------------ Programa Reajuste ------------------------|\n")
print("|-------------------------------------------------------------------|\n")



nome = str(input("Digite seu nome: \n"))
cargo = str(input("Digite seu cargo: \n"))
salario = float(input("Digite seu salário: \n"))



if salario <= 1000 :
    salario = salario + (salario / 10)
    print(f"salário final de {nome} e do cargo de {cargo}, será de {salario:.2f}")

else : 
    print("Salario sem direito a reajuste: \n"
          f"Nome: {nome}\n" 
          f"Cargo: {cargo}\n"
          f"Salário: {salario:.2f}\n"
          )