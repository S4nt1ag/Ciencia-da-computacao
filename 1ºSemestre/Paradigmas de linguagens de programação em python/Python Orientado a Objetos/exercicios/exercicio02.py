class Veiculo:

  def __init__(self, nome, velocidadeMax,quilometroLitro):
    self.nome = nome
    self.velocidadeMax = velocidadeMax
    self.quilometroLitro = quilometroLitro

  def capacidadeAssentos(self, quantidadeAssentos):
    print(f'a capacidade maxima de assentos do veiculo é {quantidadeAssentos}')

  def toStr(self):
    print(f'Nome = {self.nome}')
    print(f'VelocidadeMax = {self.velocidadeMax}')
    print(f'Quilometros percorridos por litro = {self.quilometroLitro}')

class Onibus(Veiculo):

  def capacidadeAssentos(self, quantidadeAssentos=70 ):
    super().capacidadeAssentos(quantidadeAssentos=70)

onibusEscolar = Onibus('Scania', 120, 8)
onibusEscolar.toStr()
onibusEscolar.capacidadeAssentos()