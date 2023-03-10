'''
Quantos sapatos você conseguiu vender ?
Caso tenha vendidos pelo menos 21, você receberá um aumento.
'''
meta = 21
sapatos_vendidos = input('Quantos sapatos foram vendidos ?')
if int(sapatos_vendidos) >= int(meta):
  print('Você receberá um aumento.')
else:
  print('Você não receberá um aumento.')
    