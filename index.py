print("ATENÇÃO! DEVE SE USAR O '.' NO LUGAR DA ',' PARA RELACIONAR AS MEDIDAS")
print("RESPONDER APENAS AS UNIDADES EM NÚMEROS")

nome = str(input("Digite seu nome:"))
alt = float(input("Digite sua altura em metros(ex: 1.76):"))
peso = float(input("Digite seu peso em kg(ex: 76.5):"))

imc = peso/(alt**2)

if (imc <= 18.5):
    print("{}, de acordo com os cálculos seu indíce de massa corporal corresponde a {:.1f} e você se encotra {}!".format(nome,imc,"abaixo do peso"))
if ((imc >= 18.6) and (imc <= 24.9)):
    print("{}, de acordo com os cálculos seu indíce de massa corporal corresponde a {:.1f} e você se encotra {}!".format(nome,imc,"no peso ideal"))
if ((imc >= 25.0) and (imc <= 29.9)):
     print("{}, de acordo com os cálculos seu indíce de massa corporal corresponde a {:.1f} e você se encotra {}!".format(nome,imc,"acima do peso"))
if ((imc >= 30.0) and (imc <= 39.9)):
    print("{}, de acordo com os cálculos seu indíce de massa corporal corresponde a {:.1f} e você se encotra {}!".format(nome,imc,"com obesidade"))
else:
    print("{}, de acordo com os cálculos seu indíce de massa corporal corresponde a {:.1f} e você se encotra {}!".format(nome,imc,"com obesidade grave"))




    
    

