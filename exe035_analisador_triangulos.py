"""TRI <- (L1 < L2+L3) E (L2 < L1+L3) E (L3 < L1+L2)
      Equilatero <- ((L1 = L2) E (L2 = L3)) E (TRI = VERDADEIRO)
      Escaleno <- ((L1 <> L2) E (L2 <> L3) E (L1 <> L3)) E (TRI = VERDADEIRO)
      Isosceles <- ((L1 = L2) OU (L2 = L3) OU (L1 = L3)) E (TRI = VERDADEIRO)
      Escreva ("Os valores podem formar um Triângulo? ")
              SE (TRI = VERDADEIRO) ENTAO
                 Escreval ("SIM. Continuando...")
              SENAO
                 Escreval ("NÃO! Esses valores não formam um triângulo!")
              FIMSE
      Escreva ("O Triângulo é equilátero? ")
              SE (Equilatero = VERDADEIRO) ENTAO
                 Escreval ("SIM.")
              SENAO
                 Escreval ("NÃO.")
              FIMSE
      Escreva ("O Triângulo é escaleno? ")
               SE (Escaleno = VERDADEIRO) ENTAO
                 Escreval ("SIM.")
              SENAO
                 Escreval ("NÃO.")
              FIMSE
      Escreva ("O Triângulo é isosceles? ")
              SE (Isosceles = VERDADEIRO) ENTAO
                 Escreval ("SIM.")
              SENAO
                 Escreval ("NÃO.")
              FIMSE"""
l1 = float(input('Digite o 1º lado: '))
l2 = float(input('Digite o 2º lado: '))
l3 = float(input('Digite o 3º lado: '))
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('{}, {} e {} formam um triângulo!'.format(l1, l2, l3))
else:
    print('{}, {} e {} não formam um triângulo!'.format(l1, l2, l3))