import random


class Armor:
    def __init__(self, name, material, resist, mod, text, details, weight, price):
        self.name = name
        self.type = 'Armor'
        self.material = material
        self.resist = resist
        self.mod = mod
        self.text = text
        self.details = details
        self.weight = weight
        self.price = price

    def print_info(self):
        print(self.name)
        print('Típus: {}'.format(self.material))
        print('Mozgáscsökkentés: {}'.format(self.mod))
        print('Védelem: {}-{}'.format(self.resist[0], self.resist[5]))
        print('Súly {}'.format(self.weight))
        print(random.choice(self.details))


LOW_MOD = 0
MED_MOD = -1
HGH_MOD = -2


def ruházat():
    text = ['ruha',
            'ruhád',
            'ruháddal',
            'ruhája',
            'ruhájával']
    details = ['semmi']
    return Armor('Ruha', 'textil', [0, 0, 0, 0, 0, 0], LOW_MOD, text, details, 0, 0)


def bormelleny():
    text = ['bőrmellény',
            'bőrmellényed',
            'bőrmellényeddel',
            'bőrmellénye',
            'bőrmellényével'
            ]
    details = ['nincs']
    return Armor('Bőrmellény', 'bőr', [0, 0, 0, 0, 1, 1], LOW_MOD, text, details, 2, 20)


def borvert():
    text = ['bőrvért',
            'bőrvérted',
            'bőrvérteddel',
            'bőrvértje',
            'bőrvértjével'
            ]
    details = ['nincs']
    return Armor('Bőrvért', 'bőr', [0, 1, 1, 1, 1, 1], LOW_MOD, text, details, 3, 25)


def lancing():
    text = ['láncing',
            'láncinged',
            'láncingeddel',
            'láncingje',
            'láncingjével'
            ]
    details = ['nincs']
    return Armor('Láncing', 'lánc', [0, 0, 0, 1, 2, 2], MED_MOD, text, details, 7, 40)


def sodronying():
    text = ['sodronying',
            'sodronyinged',
            'sodronyingeddel',
            'sodronyingje',
            'sodronyingjével'
            ]
    details = ['nincs']
    return Armor('Sodronying', 'lánc', [0, 1, 2, 2, 2, 2], MED_MOD, text, details, 10, 55)


def mellvert():
    text = ['mellvért',
            'mellvérted',
            'mellvérteddel',
            'mellvértje',
            'mellvértjével'
            ]
    details = ['nincs']
    return Armor('Mellvért', 'lemez', [0, 0, 1, 2, 2, 3], HGH_MOD, text, details, 8, 65)


def lemezvert():
    text = ['lemezvért',
            'lemezvérted',
            'lemezvérteddel',
            'lemezvértje',
            'lemezvértjével'
            ]
    details = ['nincs']
    return Armor('Lemezvért', 'lemez', [1, 1, 2, 2, 3, 3], HGH_MOD, text, details, 12, 110)


if __name__ == "__main__":
    pass
