# exemplo partial
import operator
from functools import partial
adicionaUm = partial(operator.add, 1)

print(adicionaUm(5))

#segundo exemplo partial
print('\nsegundo exemplo')
import collections
from operator import attrgetter
pessoa = collections.namedtuple('pessoa', 'nome idade')
pessoas = [pessoa('joao', 40), pessoa('ana', 20), pessoa('renata', 25)]

print(sorted(pessoas, key=attrgetter('nome')))
print(sorted(pessoas,key=attrgetter('idade')))

# terceiro exemplo

print('\nterceiro exemplo')
from functools import partial
sortName = partial(sorted, key=attrgetter('nome'))
sortIdade = partial(sorted, key=attrgetter('idade'))

print(sortName(pessoas))
print(sortIdade(pessoas))