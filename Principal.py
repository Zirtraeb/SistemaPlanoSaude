print('Sistema de Planos, por Beatriz Avelar.')

idade        = int(input('Informe a idade do cliente: '))
valor_base   = float(input('Informe o valor base do plano: R$'))

if(idade >= 100):
  print('Não há planos a oferecer, confira a idade digitada.')
else:
  if(idade >= 0 and idade < 19):
    x = 100
  elif(idade >= 19 and idade < 29):
    x = 150
  elif(idade >= 29 and idade < 39):
    x = 225
  elif(idade >= 39 and idade < 49):
    x = 240
  elif(idade >= 49 and idade < 59):
    x = 350
  elif(idade >= 59 and idade < 100):
    x = 600

  valor_mensal = valor_base * x / 100
  print(f'O valor mensal a ser cobrado será de R${valor_mensal}.')


