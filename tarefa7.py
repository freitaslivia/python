raio = int(input("Digite o raio do cilindro: "))
altura = int(input("Digite a altura do cilindro: "))



if raio > 0 and altura > 0:
        
 area_base = raio * raio * 3.14

 volume = int(area_base) * altura

 print("O volume do cilindro é:", volume)
else:
 print("Os valores digitados para o raio e/ou a altura não são válidos.")

print("Fim do programa")