import random
import armors
import weapons
import os
import time

class Karakter:
    def __init__(self, ugyesseg, eletero):
        self.ugyesseg = ugyesseg
        self.eletero = eletero


class Jatekos(Karakter):
    def __init__(self, ugyesseg, eletero, szerencse):
        super(Jatekos, self).__init__(ugyesseg, eletero)
        self.nev = 'Játékos'
        self.szerencse = szerencse
        self.akt_ugyesseg = ugyesseg
        self.akt_eletero = eletero
        self.akt_szerencse = szerencse
        self.cutting_weapons = 0
        self.splitting_weapons = 0
        self.crushing_weapons = 0
        self.fiber_weapons = 0
        self.wearing_armor = 0
        self.athletics = 0
        self.weapon = weapons.okol()
        self.armor = armors.ruházat()
        self.payload = 0
        self.felszereles = {}
        self.arany = 0
        self.elelmiszer = 0
        self.ido = 0
        self.kodszavak = []
        self.jegyzetek = []

    def print_inf(self):
        print('-' * 48)
        print('Ügyesség:  {}/{}'.format(self.ugyesseg, self.akt_ugyesseg))
        print('Életerő:   {}/{}'.format(self.eletero, self.akt_eletero))
        print('Szerencse: {}/{}'.format(self.szerencse, self.akt_szerencse))
        print('Terheltség:  {}'.format(format(self.payload)))
        print('-' * 48)
        print('Vágófegyverek:   {}  Hasítófegyverek: {}'.format(self.cutting_weapons, self.splitting_weapons))
        print('Ütőfegyverek:    {}  Szálfegyverek:   {}'.format(self.crushing_weapons, self.fiber_weapons))
        print('Páncélviselet:   {}  Körkörös harc:   {}'.format(self.wearing_armor, self.athletics))
        print('-' * 48)


class Enemy(Karakter):
    def __init__(self, nev, ugyesseg, eletero):
        super(Enemy, self).__init__(ugyesseg, eletero)
        self.nev = nev
        self.akt_ugyesseg = ugyesseg
        self.akt_eletero = eletero
        self.weapon = ''
        self.shield = ''
        self.armor = None
        self.items = []
        self.gold = 0


def create_character():
    points = 5
    agility = 6
    health = 12
    luck = 7
    while points > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('TULAJDONSÁG PONTOK: ', points)
        print('[0] Ügyesség  {}'.format(agility))
        print('[1] Életerő   {}'.format(health))
        print('[2] Szerencse {}'.format(luck))
        print('[3] VISSZAÁLLÍTÁS')
        decision = input('-->')
        if not decision.isnumeric():
            continue
        decision = int(decision)
        if decision == 0:
            if agility < 9:
                agility += 1
                points -= 1
            else:
                print('Maximum 3 pontot tehetsz a tulajdonságra!')
                time.sleep(2)
        elif decision == 1:
            if health < 18:
                health += 2
                points -= 1
            else:
                print('Maximum 3 pontot tehetsz a tulajdonságra!')
                time.sleep(2)
        elif decision == 2:
            if luck < 9:
                luck += 1
                points -= 1
            else:
                print('Maximum 3 pontot tehetsz a tulajdonságra!')
                time.sleep(2)
        elif decision == 3:
            points = 5
            agility = 6
            health = 12
            luck = 7
        else:
            continue
    input('Tovább')
    player = Jatekos(agility, health, luck)
    points = 4
    while points > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('KÉPESSÉG PONTOK: ', points)
        print('[0] Vágófegyverek:   {}'.format(player.cutting_weapons))
        print('[1] Hasítófegyverek: {}'.format(player.splitting_weapons))
        print('[2] Zúzófegyverek:   {}'.format(player.crushing_weapons))
        print('[3] Szálfegyverek:   {}'.format(player.fiber_weapons))
        print('[4] Páncélviselet:   {}'.format(player.wearing_armor))
        print('[5] Atlétika:        {}'.format(player.athletics))
        print('[6] VISSZAÁLLÍTÁS')
        decision = input('-->')
        if not decision.isnumeric():
            continue
        decision = int(decision)
        if decision == 0:
            if player.cutting_weapons < 2:
                player.cutting_weapons += 1
                points -= 1
            else:
                print('Maximum 2 pontot tehetsz a képességre!')
                time.sleep(2)
        elif decision == 1:
            if player.splitting_weapons < 2:
                player.splitting_weapons += 1
                points -= 1
            else:
                print('Maximum 2 pontot tehetsz a képességre!')
                time.sleep(2)
        elif decision == 2:
            if player.crushing_weapons < 2:
                player.crushing_weapons += 1
                points -= 1
            else:
                print('Maximum 2 pontot tehetsz a képességre!')
                time.sleep(2)
        elif decision == 3:
            if player.fiber_weapons < 2:
                player.fiber_weapons += 1
                points -= 1
            else:
                print('Maximum 2 pontot tehetsz a képességre!')
                time.sleep(2)
        elif decision == 4:
            if player.wearing_armor < 2:
                player.wearing_armor += 1
                points -= 1
            else:
                print('Maximum 2 pontot tehetsz a képességre!')
                time.sleep(2)
        elif decision == 5:
            if player.athletics < 2:
                player.athletics += 1
                points -= 1
            else:
                print('Maximum 2 pontot tehetsz a képességre!')
                time.sleep(2)
        elif decision == 6:
            player.cutting_weapons = 0
            player.splitting_weapons = 0
            player.crushing_weapons = 0
            player.fiber_weapons = 0
            player.wearing_armor = 0
            player.athletics = 0
            points = 0
        else:
            continue
    return player


def ork():
    ork = Enemy('Ork', random.choice([6, 7]), random.choice([6, 7, 8]))
    ork.weapon = random.choice([weapons.buzogany(), weapons.bunko(), weapons.fejsze()])
    ork.armor = random.choice([armors.borvert(), armors.bormelleny(), armors.lancing()])
    return ork


def ork_vezer():
    ork = Enemy('Ork vezér', random.choice([7, 8]), random.choice([10, 11, 12]))
    ork.weapon = random.choice([weapons.fejsze(), weapons.alabard(), weapons.csatacsillag()])
    ork.armor = random.choice([armors.sodronying(), armors.mellvert(), armors.lemezvert()])
    return ork

def ork_katona():
    ork = Enemy('Ork katona', random.choice([7, 8]), random.choice([8, 9, 10]))
    ork.weapon = random.choice([weapons.fejsze(), weapons.alabard(), weapons.csatacsillag()])
    ork.armor = random.choice([armors.lancing(), armors.sodronying(), armors.mellvert()])
    return ork

