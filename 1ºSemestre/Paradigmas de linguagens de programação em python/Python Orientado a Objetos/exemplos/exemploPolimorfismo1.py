class Argentina():
  def capital(self):
    print('Buenos Aires é a capital da Argentina')

  def linguaOficial(self):
    print("o espanhol é a lingua oficial da argentina.")

class Brasil():
  def capital(self):
    print('Brasilia é a capital do brasil')

  def linguaOficial(self):
    print('o portugues é a lingua oficial do brasil')

obj_arg = Argentina()
obj_bra = Brasil()
for pais in (obj_arg, obj_bra):
  pais.capital()
  pais.linguaOficial()