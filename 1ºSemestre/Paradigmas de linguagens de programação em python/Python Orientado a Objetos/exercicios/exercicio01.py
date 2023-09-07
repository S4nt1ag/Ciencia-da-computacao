class Veiculo:

  def __init__(self, nome, velocidadeMax,quilometroLitro):
    self.nome = nome
    self.velocidadeMax = velocidadeMax
    self.quilometroLitro = quilometroLitro

  def toStr(self):
    print(f'Nome = {self.nome}')
    print(f'VelocidadeMax = {self.velocidadeMax}')
    print(f'Quilometros percorridos por litro = {self.quilometroLitro}')

class Onibus(Veiculo):
  pass

onibusEscolar = Onibus('Scania', 120, 8)
onibusEscolar.toStr()