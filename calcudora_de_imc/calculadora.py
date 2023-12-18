def calcular_imc(peso, altura):
  imc = peso/altura**2
  return imc

def tabela_imc(imc):
  if imc <= 16 or imc <= 16.9:
    return ('muito abaixo')
  elif imc <= 17 or imc <= 18.4:
    return ('baixo')
  elif imc <= 18.5 or imc <= 24.9:
    return ('normal')
  elif imc <= 25 or imc <= 29.9:
    return ('acima')
  elif imc <= 30 or imc <= 34.9:
    return ('obesidade grau l')
  elif imc <= 35 or imc <= 40:
    return ('obesidade grau ll')
  elif imc > 40:
    return('obesidade grau lll')

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sau alura em m: '))

imc = calcular_imc(peso, altura)

classificacao = tabela_imc(imc)
print(f'Seu imc é: {imc:.2f}')
print(f'classificação: {classificacao}')