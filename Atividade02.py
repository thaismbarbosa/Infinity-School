#Calculadora IMC

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura * altura)
if imc < 17:
    print(f"MUITO abaixo do peso. IMC = {round(imc,2)}")
elif imc > 17 and imc <= 18.49:
    print(f"Abaixo do peso. IMC = {round(imc,2)}")
elif imc > 18.5 and imc <= 24.99:
    print(f"Peso normal. IMC = {round(imc, 2)}")
elif imc > 25 and imc <= 29.99:
    print(f"	Acima do peso. IMC = {round(imc,2)}")
elif imc > 30 and imc <= 34.99:
    print(f"Obesidade I. IMC = {round(imc,2)}")
elif imc > 35 and imc <= 39.99:
    print(f"Obesidade Morbida I. IMC = {round(imc,2)}")
elif imc > 40 and imc <= 44.99:
    print(f"Obesidade Morbida II. IMC = {round(imc,2)}")
else :
    print("Não pode faltar a altura e o peso!")    