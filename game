from characters import create_character
import characters
import environment
import weapons
import armors
import time
import dices
import random
import os


class Battlefield:
    def __init__(self, player):
        self.player = player
        self.enemies = []
        self.target_decisions = []
        self.player_live = True

    def get_weapon_mod(self):
        if self.player.weapon.subtype == 'vágófegyver':
            skill_mod = self.player.cutting_weapons
        elif self.player.weapon.subtype == 'hasítófegyver':
            skill_mod = self.player.splitting_weapons
        elif self.player.weapon.subtype == 'ütőfegyver':
            skill_mod = self.player.crushing_weapons
        elif self.player.weapon.subtype == 'szálfegyver':
            skill_mod = self.player.fiber_weapons
        else:
            skill_mod = 0
        weapon_mod = self.player.weapon.mod + skill_mod
        return weapon_mod

    def get_over_power(self):
        actual_enemy_number = len(self.enemies)
        over_power_mod = - actual_enemy_number + 1
        over_power_mod += self.player.athletics
        if over_power_mod > 0:
            over_power_mod = 0
        return over_power_mod

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def battle_status(self):
        ugyesseg_kiir = str(self.player.ugyesseg) + '/' + str(self.player.akt_ugyesseg)
        eletero_kkir = str(self.player.eletero) + '/' + str(self.player.akt_eletero)
        szerencs_kiir = str(self.player.szerencse) + '/' + str(self.player.akt_szerencse)
        kornyezet.print_enviroment()
        print('#' * 80)
        print('{:>12}{:>15}{:>16}'.format('Ügyesség', 'Életerő', 'Szerencse'))
        print('{:^15}{:^17}{:^13}'.format(ugyesseg_kiir, eletero_kkir, szerencs_kiir))
        print('{:>11}{:>16}'.format('Túlerő', 'Fegyver'))
        print('{:^15}{:^17}'.format(self.get_over_power(), self.get_weapon_mod()))
        print('#' * 80)
        print('{:>29}{:>15}{:>13}{:>18}'.format('Ügyesség', 'Életerő', 'Fegyver', 'Páncél'))
        index = 0
        self.target_decisions = []
        for enemy in self.enemies:
            self.target_decisions.append(index)
            nev = enemy.nev
            ugyesseg = enemy.akt_ugyesseg
            eletero = enemy.akt_eletero
            fegyver = enemy.weapon.name
            if enemy.armor:
                pancel = enemy.armor.name
            else:
                pancel = ''
            print('[{}] {:<16}{:>6}{:>15}{:^25}{:^12}'.format(index, nev, ugyesseg, eletero, fegyver, pancel))
            index += 1
        print('#' * 80)

    def health_check(self):
        index = 0
        for enemy in self.enemies:
            if enemy.akt_eletero <= 0:
                self.enemies.remove(enemy)
                print(enemy.nev, 'meghalt!')
                index += 1
                time.sleep(2)

    def battle_turn(self):
        def take_damage(attacker, target):
            damage = random.choice(attacker.weapon.damage)
            resist = random.choice(target.armor.resist)
            if damage - resist <= 0:
                return 'A {} {} felfogta a sebzést! ({}-{})'.format(target.nev, target.armor.text[3], damage,
                                                                    resist), resist
            else:
                target.akt_eletero -= damage - resist
                return 'Sebzés: {} ({}-{})'.format(damage - resist, damage, resist), resist

        while True:
            decision = input('Melyik ellenséget támadod? ')
            if not decision.isnumeric():
                continue
            decision = int(decision)
            if decision not in self.target_decisions:
                print('Nincs ilyen ellenség!')
                continue
            else:
                break
        roll = dices.roll_2d6()
        player_attack = roll + self.player.akt_ugyesseg + self.get_weapon_mod() + self.get_over_power()
        enemy_counter = 0
        for enemy in self.enemies:
            roll = dices.roll_2d6()
            enemy_attack = roll + enemy.akt_ugyesseg + enemy.weapon.mod
            if decision == enemy_counter:
                if player_attack > enemy_attack:
                    print('Eltaláltad az ellenfeled! ', take_damage(self.player, enemy)[0])
                    # take_damage(self.player, enemy)
                elif player_attack < enemy_attack:
                    print('Eltaláltak! ', take_damage(enemy, self.player)[0])
                    # take_damage(enemy, self.player)
                elif player_attack == enemy_attack:
                    print('Kivédtétek egymás támadását!')
            else:
                if player_attack >= enemy_attack:
                    print('Kivédted az {} támadását!'.format(enemy.nev))
                elif player_attack < enemy_attack:
                    print('Eltaláltak! ', take_damage(enemy, self.player)[0])
                    # take_damage(enemy, self.player)
            enemy_counter += 1
            time.sleep(2)

    def fight(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            self.battle_status()
            self.battle_turn()
            self.health_check()
            os.system('cls' if os.name == 'nt' else 'clear')

            if not self.enemies:
                print('GYŐZTÉL')
                time.sleep(2)
                break
            if self.player.akt_eletero <= 0:
                print('MEGHALTÁL')
                time.sleep(3)
                break


def add_inventory(jatekos, added_item):
    included = False
    for meglevo_targy in jatekos.felszereles:
        if meglevo_targy.name in added_item.name:
            included = True
    if not included:
        jatekos.felszereles[added_item] = 1
    elif included:
        for meglevo_targy in jatekos.felszereles:
            if meglevo_targy.name == added_item.name:
                jatekos.felszereles[meglevo_targy] += 1
    jatekos.payload += added_item.weight


def remove_inventory(player, deleted_item):
    # player.payload -= list(player.felszereles)[deleted_item].weight
    if player.felszereles[list(player.felszereles)[deleted_item]] == 1:
        del player.felszereles[list(player.felszereles)[deleted_item]]
    elif player.felszereles[list(player.felszereles)[deleted_item]] > 1:
        player.felszereles[list(player.felszereles)[deleted_item]] -= 1


def get_inventory(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    index = 0
    opportunities = [0]
    player.print_inf()
    print('FELSZERELÉS')
    if player.felszereles:
        for targy in player.felszereles:
            print('[{}] {:<15}{:>3}'.format(index, targy.name, player.felszereles[targy]))
            index += 1
            opportunities.append(index)
    else:
        print('Nincs nálad semmi...')
    print('[{}] VISSZA'.format(index))
    while True:
        decision = input('Válassz: ')
        if not decision.isnumeric():
            continue
        decision = int(decision)
        if decision not in opportunities:
            print('Nincs nálad ilyen tárgy!')
            print('*' * 48)
            continue
        elif decision == index:
            break
        else:
            print('-' * 24)
            list(player.felszereles)[decision].print_info()
            print('-' * 24)
            if list(player.felszereles)[decision].type == 'Weapon':
                print('[0] Kézbevesz')
                print('[1] Kilép')
                decision2 = input('Válassz: ')
                if not decision2.isnumeric():
                    continue
                decision2 = int(decision2)
                if decision2 == 0:
                    weapon_change(player, decision)
                elif decision2 == 1:
                    pass
                else:
                    print('Nincs ilyen lehetőség...')
            elif list(player.felszereles)[decision].type == 'Armor':
                print('[0] Felvesz')
                print('[1] Kilép')
                decision2 = input('Válassz: ')
                if not decision2.isnumeric():
                    return
                decision2 = int(decision2)
                if decision2 == 0:
                    armor_change(player, decision)
                elif decision2 == 1:
                    pass
                else:
                    print('Nincs ilyen lehetőség...')
            get_inventory(player)
            break


def weapon_change(player, item):
    if player.weapon.name != 'Ököl':
        add_inventory(player, player.weapon)
        print('Eltetted az alábbi fegyvert: {}'.format(player.weapon.name))
        player.weapon = list(player.felszereles)[item]
        print('Elővetted az alábbi fegyvert: {}'.format(player.weapon.name))
        remove_inventory(player, item)
    elif player.weapon.name == 'Ököl':
        player.weapon = list(player.felszereles)[item]
        print('Elővetted az alábbi fegyvert: {}'.format(player.weapon.name))
        remove_inventory(player, item)
    print('*' * 48)
    time.sleep(2)


def weapon_off(player):
    if player.weapon.name != 'Ököl':
        add_inventory(player, player.weapon)
        print('Eltetted az alábbi fegyvert: {}'.format(player.weapon.name))
        player.weapon = weapons.okol()
    else:
        print('Nincs előkészített fegyvered!')
    print('*' * 48)
    time.sleep(2)


def get_armor_mod(player):
    armor_mod = player.armor.mod + player.wearing_armor
    if armor_mod > 0:
        armor_mod = 0
    return armor_mod


def armor_change(player, armor):
    if player.armor.name != 'Ruha':
        add_inventory(player, player.armor)
        player.akt_ugyesseg -= get_armor_mod(player)
        print('Levetted az alábbi páncélt: {}'.format(player.armor.name))
        player.armor = list(player.felszereles)[armor]
        player.akt_ugyesseg += get_armor_mod(player)
        print('Felvetted az alábbi páncélt: {}'.format(player.armor.name))
        remove_inventory(player, armor)
    else:
        player.armor = list(player.felszereles)[armor]
        player.akt_ugyesseg += get_armor_mod(player)
        print('Felvetted az alábbi páncélt: {}'.format(player.armor.name))
        remove_inventory(player, armor)
    print('*' * 48)
    print('Akt ügy: ', player.akt_ugyesseg)
    time.sleep(2)


def armor_off(player):
    if player.armor.name != 'Ruha':
        add_inventory(player, player.armor)
        player.akt_ugyesseg -= get_armor_mod(player)
        print('Levetted az alábbi páncélt: {}'.format(player.armor.name))
        player.armor = armors.ruházat()
        print('*' * 48)
    else:
        print('Nem viselsz páncélt!')
    print('*' * 48)
    time.sleep(2)


def get_arms(player):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.print_inf()
        print('Fegyver: {} ({}-{})'.format(player.weapon.name, player.weapon.damage[0], player.weapon.damage[5]))
        if player.armor.name != 'Ruha':
            print('Páncél: {} ({}-{})'.format(player.armor.name, player.armor.resist[0], player.armor.resist[5]))
        else:
            print('Páncél: nem viselsz páncélt')
        print('*' * 48)
        print('[0] Fegyer eltétele')
        print('[1] Páncél levétele')
        print('[2] VISSZA')
        decision = input('--> ')
        if not decision.isnumeric():
            continue
        decision = int(decision)
        if decision == 0:
            weapon_off(player)
        elif decision == 1:
            armor_off(player)
        elif decision == 2:
            break
        else:
            continue


weapons_list = [weapons.fejsze(), weapons.bard(), weapons.csatabard(),
                weapons.bunko(), weapons.buzogany(), weapons.csatacsillag(),
                weapons.kes(), weapons.kard(), weapons.pallos(),
                weapons.bot(), weapons.landzsa(), weapons.alabard()]
armors_list = [armors.borvert(), armors.bormelleny(), armors.lancing(), armors.sodronying(),
               armors.mellvert(), armors.lemezvert()]

jatekos = create_character()
kornyezet = environment.Environment()

for i in range(3):
    random_weapon = random.choice(weapons_list)
    add_inventory(jatekos, random_weapon)
for i in range(3):
    random_armor = random.choice(armors_list)
    add_inventory(jatekos, random_armor)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    kornyezet.add_hour(1)
    if jatekos.akt_eletero <= 0:
        break
    kornyezet.print_enviroment()
    jatekos.print_inf()
    print('[0] Felszerelés megtekintése')
    print('[1] Fegyverzet megtekintése')
    print('[2] Belépés az arénába')
    decision = input('--> ')
    if not decision.isnumeric():
        continue
    decision = int(decision)
    if decision == 0:
        get_inventory(jatekos)
    elif decision == 1:
        get_arms(jatekos)
    elif decision == 2:
        enemy_number_list = [1, 2, 2, 2, 3, 3]
        harc = Battlefield(jatekos)
        enemy_number = random.choice(enemy_number_list)
        for i in range(enemy_number):
            enemy_list = [characters.ork(), characters.ork_katona(), characters.ork_vezer()]
            enemy = random.choice(enemy_list)
            harc.add_enemy(enemy)
        kornyezet.add_hour(1)
        harc.fight()

    else:
        continue
