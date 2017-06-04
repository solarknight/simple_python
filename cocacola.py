class Cocacola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def __init__(self):
        self.local_logo = 'coca!'
        for element in self.formula:
            print('Coke has {}'.format(element))

    def drink(self):
        print('Energy!')

    @classmethod
    def hello(cls):
        return "hello from %s" % cls.__name__

ice_coke = Cocacola()
ice_coke.drink()
print(Cocacola.hello())
print(ice_coke.local_logo)

class CaffeineFree(Cocacola):
    caffeine = 0

coke_a = CaffeineFree()
coke_a.drink()
