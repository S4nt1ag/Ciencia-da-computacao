# tratando uma api
usuario = {
    'nome' : 'Joao',
    'redes': [{
        'nome' : 'facebook',
        'imagem_profile' : "",
        'imagem_capa':"imagem2"
    }]
}

# retorna a imagem do profile
def getImagemProfile(usuario):
  for rede in usuario['redes']:
    if rede[imagem_profile]:
      return rede['imagem_profile']
  return 'default'

# retorna a imagem de capa
def getImagemCapa(usuario):
  for rede in usuario['redes']:
    if rede[imagem_capa]:
      return rede['imagem_capa']
  return 'default'

# utilizando partial
from functools import partial
def getImagem(qualImagem, usuario):
  for rede in usuario['redes']:
    if rede[qualImagem]:
      return rede[qualImagem]
  return 'default'

getImagemProfile = partial(getImagem, 'imagem_profile')
getImagemCapa = partial(getImagem, 'imagem_capa')

print('\nsaida partial final')
print(getImagemProfile(usuario))
print(getImagemCapa(usuario))