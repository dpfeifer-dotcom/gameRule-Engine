import random
import os

class Weapon:
    def __init__(self, name, subtype, damage, mod, text, details, weight, price):
        self.name = name
        self.type = 'Weapon'
        self.subtype = subtype
        self.damage = damage
        self.mod = mod
        self.text = text
        self.details = details
        self.weight = weight
        self.price = price

    def print_info(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.name)
        print('Típus: {}'.format(self.subtype))
        print('Támadás módosító: {}'.format(self.mod))
        print('Sebzés: {}-{}'.format(self.damage[0], self.damage[5]))
        print('Súly: {} kg'.format(self.weight))
        print(random.choice(self.details))


LOW_DMG = [1, 2, 2, 2, 2, 3]
MED_DMG = [2, 3, 3, 3, 3, 4]
HGH_DMG = [2, 3, 3, 4, 4, 5]
LOW_PRICE = 1
MED_PRICE = 30
HGH_PRICE = 80


def okol():
    text = ['ököl',
            'öklöd',
            'öklöddel',
            'ökle',
            'öklével']
    details = ['Praktus, hiszen mindig kéznél van.',
               'Többször kihúzott a bajból, mikor mindenem elveszett',
               'Mint a többi fegyver, ez se törhetetlen.']
    return Weapon('Ököl', 'Egyéb', [1, 1, 1, 1, 2, 2], 0, text, details, 0, 0)


def kes():
    text = ['kés',
            'késed',
            'késeddel',
            'kése',
            'késével']
    details = [
        'A kés egy egyszerű hétköznapi használati eszköz. Viszont hozzáértő kézben halálos fegyverré is válhat.']
    return Weapon('Kés', 'vágófegyver', LOW_DMG, 0, text, details, 0.5, LOW_PRICE)


def kard():
    text = ['kard',
            'kardod',
            'kardoddal',
            'kardja',
            'kardjával']
    details = ['nincs']
    return Weapon('Kard', 'vágófegyver', MED_DMG, 0, text, details, 1, MED_PRICE)


def pallos():
    text = ['pallos',
            'pallosod',
            'pallosoddal',
            'pallosa',
            'pallosával']
    details = ['nincs']
    return Weapon('Pallos', 'vágófegyver', HGH_DMG, -1, text, details, 3, HGH_PRICE)


def fejsze():
    text = ['fejsze',
            'fejszéd',
            'fejszéddel',
            'pallosa',
            'pallosával']
    details = ['nincs']
    return Weapon('Fejsze', 'hasítófegyver', LOW_DMG, 0, text, details, 0.5, LOW_PRICE)


def bard():
    text = ['bárd',
            'bárdod',
            'bárdoddal',
            'bárdja',
            'bárdjával']
    details = ['nincs']
    return Weapon('Bárd', 'hasítófegyver', MED_DMG, 0, text, details, 1, MED_PRICE)


def csatabard():
    text = ['csatabárd',
            'csatabárdod',
            'csatabárdoddal',
            'csatabárdja',
            'csatabárdjával']
    details = ['nincs']
    return Weapon('Csatabárd', 'hasítófegyver', HGH_DMG, -1, text, details, 3, HGH_PRICE)


def bunko():
    text = ['bunkó',
            'bunkód',
            'bunkóddal',
            'bunkója',
            'bunkójával']
    details = ['nincs']
    return Weapon('Bunkó', 'ütőfegyver', LOW_DMG, 0, text, details, 0.5, LOW_PRICE)


def buzogany():
    text = ['buzogány',
            'buzogányod',
            'buzogányoddal',
            'buzogánya',
            'buzogányával']
    details = ['nincs']
    return Weapon('Buzogány', 'ütőfegyver', MED_DMG, 0, text, details, 1, MED_PRICE)


def csatacsillag():
    text = ['csatacsillag',
            'csatacsillagod',
            'csatacsillagoddal',
            'csatacsillagja',
            'csatacsillagjával']
    details = ['nincs']
    return Weapon('Csatacsillag', 'ütőfegyver', HGH_DMG, -1, text, details, 3, HGH_PRICE)


def bot():
    text = ['bot',
            'botod',
            'botoddal',
            'botja',
            'botjával']
    details = ['nincs']
    return Weapon('Bot', 'szálfegyver', LOW_DMG, 0, text, details, 0.5, LOW_PRICE)


def landzsa():
    text = ['lándzsa',
            'lándzsád',
            'lándzsáddal',
            'lándzsája',
            'lándzsájával']
    details = ['nincs']
    return Weapon('Lándzsa', 'szálfegyver', MED_DMG, 0, text, details, 1, MED_PRICE)


def alabard():
    text = ['alabárd',
            'alabárdod',
            'alabároddal',
            'alabárdja',
            'alabárdjával']
    details = ['nincs']
    return Weapon('Alabárd', 'szálfegyver', HGH_DMG, -1, text, details, 3, HGH_PRICE)


if __name__ == "__main__":
    pass
