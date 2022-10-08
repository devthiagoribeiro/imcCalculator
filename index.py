print("----ATENÇÃO! DEVE SE USAR O '.' NO LUGAR DA ',' PARA RELACIONAR AS MEDIDAS----")
print("----RESPONDER APENAS AS UNIDADES EM NÚMEROS-----")

nome = str(input("Digite seu nome:"))
alt = float(input("Digite sua altura em metros(ex: 1.76):"))
peso = float(input("Digite seu peso em kg(ex: 76.5):"))

imc = peso/(alt**2)

if imc < 18.5:
    print(f"{nome}, de acordo com os cálculos seu indíce de massa corporal corresponde a {imc:.1f} e você se encotra abaixo do peso!")
elif (imc > 18.5) and (imc < 24.9):
    print(f"{nome}, de acordo com os cálculos seu indíce de massa corporal corresponde a {imc:.1f} e você se encotra no peso ideal!")
elif ((imc > 24.9) and (imc < 29.9)):
     print(f"{nome}, de acordo com os cálculos seu indíce de massa corporal corresponde a {imc:.1f} e você se encotra acima do peso!")
elif ((imc > 29.9) and (imc < 39.9)):
    print(f"{nome}, de acordo com os cálculos seu indíce de massa corporal corresponde a {imc:.1f} e você se encotra em estado de obesidade!")
else:
    print(f"{nome}, de acordo com os cálculos seu indíce de massa corporal corresponde a {imc:.1f} e você se encotra em obesidade morbida!")

#desenvolvido pro Thiago Ribeiro


    
    

