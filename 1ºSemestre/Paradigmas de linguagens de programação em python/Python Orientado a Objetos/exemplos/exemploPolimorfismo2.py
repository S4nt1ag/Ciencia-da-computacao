class Veiculo:
  def rodar(self):
    print('reduz o consumo de combustivel')

class VeiculoEletrico(Veiculo):
  def rodar(self):
    super().rodar()
    print('esse veiculo utiliza eletricidade')

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()