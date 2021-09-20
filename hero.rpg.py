import random


class Character:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
    def alive(self, health):
        if self.health > 0:
            return True
        else:
            return False


class Items:
    def __init__(self, name, boost, cost):
        self.name = name
        self.boost = boost
        self.cost =  cost


class Hero(Character):
    hero_health = 20
    hero_power = 4
    def h_attack():
        crit_percent = [1, 2, 3, 4, 5,]
        crit_chance = random.choice(crit_percent)
        if crit_chance == 3:
            goblin.health -= (hero.power * 2)
            print("You crit the enemy for {}!".format(hero.power * 2))
        else:
            goblin.health -= hero.power
            print("You do {} damage to the enemy.".format(hero.power))
    def h_print_status():
        print("You have {} health, {} power.".format(hero.health, hero.power))


class Friend(Character):
    friend_health = 20
    friend_power = 4
    def fri_attack():
        f_atk_percent = [1, 2, 3, 4, 5,]
        f_atk_chance = random.choice(f_atk_percent)
        if f_atk_chance == 3:
            goblin.health -= (friend.power * 2)
            print("Friend crit the enemy for {}!".format(friend.power * 2))
        else:
            goblin.health -= friend.power
            print("friend does {} damage.".format(friend.power))
    def h_print_status():
        print("You have {} health and {} power.".format(friend.health, friend.power))


class Medic(Character):
    medic_health = 20
    medic_power = 2
    def m_heal():
        heal_percent = [1, 2, 3, 4, 5,]
        heal_chance = random.choice(heal_percent)
        if heal_chance == 3:
            hero.health += medic.power
            print("You have been healed for {}!".format(medic.power))
        else:
            print("Your medic missed.")


class Goblin(Character):
    goblin_health = 20
    goblin_power = 4
    def g_attack():
        if goblin.health > 0:
            hero.health -= goblin.power
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")
        if goblin.health <= 0:
            print("The goblin is dead.")
    def g_print_status():
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))


class Boss(Character):
    boss_health = 30
    boss_power = 6
    def b_attack():
        if boss.health > 0:
            hero.health -= boss.power
            print("The boss does {} damage to you.".format(boss.power))
            if hero.health <= 0:
                print("You are dead.")
    def b_print_status():
        print("The boss has {} health and {} power.".format(boss.health, boss.power))


class Zombie(Character):
    zombie_health = 20
    zombie_power = 4
    def z_attack():
        if zombie.alive == True:
            crit_percent = [1, 2, 3, 4, 5,]
            crit_chance = random.choice(crit_percent)
            if crit_chance == 3:
                zombie.health -= (hero.power * 4)
                print("You crit the enemy for {}!".format(hero.power * 4))
            else:
                print("The zombie was not hurt by your attack")
                Hero.hero_health -= Zombie.zombie_power
                print("The zombie does {} damage to you.".format(Zombie.zombie_power))
            if Hero.hero_health <= 0:
                print("You are dead.")
    def z_print_status():
        print("The zombie has {} health and {} power.".format(Zombie.zombie_health, Zombie.zombie_power))


class Shadow(Character):
    shadow_health = 1
    shadow_power = 2
    def s_hit():
        hit_percent = [1, 2, 3, 4, 5, 7, 8, 9, 10]
        hit_chance = random.choice(hit_percent)
        if hit_chance == 5:
            shadow.health -= hero.power
            print("You hit the enemy for {}!".format(shadow.power * 2))
        else:
            hero.health -= shadow.power
            print("You missed the shadow and have taken {} damage.".format(shadow.power))
        if shadow.health <= 0:
            print("The shadow is dead.")
    def s_print_status():
        print("The shadow has {} health and {} power.".format(shadow.health,shadow.power))


def shop(money):
    while True:
        print("Welcome! What can I get you?")
        print(f"You have {money} dollars")
        print("1. Super Tonic - $10 (Heals for 10 hp.)")
        print("2. Strength Juice - $10 (Gives you +2 Power.)")
        print("3. Icy Hot - $20 (Gives you 14 hp and +2 Power) ")
        print("4. leave shop")
        print("> ")
        buy = input()
        if buy == "1":
            if buy == "1" and money >= 10:
                money -= 10
                hero.health += 10
                print("You have recived a Super Tonic.")
                print(f"You now have {hero.health} HP.")
            elif buy == "1" and money <= 10:
                print("Sorry, not enough cash.")
        if buy == "2":
            if buy == "2" and money >= 10:
                money -= 10
                hero.power += 2
                print("You have recived Stregth Juice.")
                print(f"You now have {hero.power} Power")
            elif buy == "2" and money <= 10:
                print("Not enough cash for that.")
        if buy == "3":
            if buy == "3" and money >= 10:
                money -= 20
                hero.power += 2
                hero.health += 14
                print("You have recived some Icy Hot.")
                print(f"You now have {hero.health} hp and {hero.power} Power")
            elif buy == "3" and money <= 10:
                print("Not enough cash for that.")
        if buy == "4":
            return False


def enemy_select():
    print("where do you want to go?")
    Hero.h_print_status()
    print("1. Shop")
    print("2. Continue Story")
    raw_input = input(">  ")
    print(" ")
    if raw_input == "1":
        shop()
        pass
    if raw_input == "2":
        goblin_fight()


hero = Character("Hero", 20, 4, 2)
friend = Character("Friend", 10, 2, 1)
medic = Character("Medic", 10, 2, 1)
goblin = Character("Goblin", 12, 4, 2)
zombie = Character("Zombie", 20, 4, 1)
shadow = Character("Shadow", 1, 2, 1)
boss = Character("Boss", 30, 6, 2)
shop(20)


def goblin_fight():
    while goblin.health >= 0:
        Hero.h_print_status()
        Goblin.g_print_status()
        print()
        print("What do you want to do?")
        print("1. Attack goblin")
        print("2. Ask for heals")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print(" ")
        if raw_input == "1":
            Hero.h_attack()
            Friend.fri_attack()
            Goblin.g_attack()
            print()
        elif raw_input == "2":
            Medic.m_heal()
        elif raw_input == "3":
            print("Goodbye.")
            enemy_select()
        else:
            print("Invalid input {}".format(raw_input))


def zombie_fight():
    while zombie.health >= 0:
        Hero.h_print_status()
        Zombie.z_print_status()
        print()
        print("What do you want to do?")
        print("1. Attack zombie")
        print("2. Ask for heals")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print(" ")
        if raw_input == "1":
            crit_percent = [1, 2, 3, 4, 5,]
            crit_chance = random.choice(crit_percent)
            if crit_chance == 3:
                zombie.health -= (hero.power * 4)
                print("You crit the enemy for {}!".format(hero.power * 4))
            else:
                print("The zombie was not hurt by your attack")
            f_atk_percent = [1, 2, 3, 4, 5,]
            f_atk_chance = random.choice(f_atk_percent)
            if f_atk_chance == 3:
                zombie.health -= (friend.power * 2)
                print("Friend crit the enemy for {}!".format(friend.power * 2))
            else:
                print("Friends attack missed the zombie.")
            if zombie.alive == True:
                Hero.hero_health -= Zombie.zombie_power
                print("The zombie does {} damage to you.".format(Zombie.zombie_power))
            if Hero.hero_health <= 0:
                print("You are dead.")
            print()
        elif raw_input == "2":
            Medic.m_heal()
        elif raw_input == "3":
            print("Goodbye.")
            enemy_select()
        else:
            print("Invalid input {}".format(raw_input))


def shadow_fight():
    while shadow.health >= 0:
        Hero.h_print_status()
        Shadow.s_print_status()
        print()
        print("What do you want to do?")
        print("1. Attack shadow")
        print("2. Ask for heals")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        print(" ")
        if raw_input == "1":
            hit_percent = [1, 2, 3, 4, 5, 7, 8, 9, 10]
            hit_chance = random.choice(hit_percent)
            if hit_chance == 5:
                shadow.health -= hero.power
                print("You hit the enemy for {}!".format(shadow.power * 2))
            else:
                hero.health -= shadow.power
                print("You missed the shadow and have taken {} damage.".format(shadow.power))
            if shadow.health <= 0:
                print("The shadow is dead.")
            if shadow.alive == True:
                Hero.hero_health -= shadow.shadow_power
                print("The shadow does {} damage to you.".format(shadow.shadow_power))
            if Hero.hero_health <= 0:
                print("You are dead.")
            print()
        elif raw_input == "2":
            Medic.m_heal()
        elif raw_input == "3":
            print("Goodbye.")
            enemy_select()
        else:
            print("Invalid input {}".format(raw_input))


def boss_fight():
    while boss.health >= 0:
        Hero.h_print_status()
        Boss.b_print_status()
        print()
        print("What do you want to do?")
        print("1. Attack boss")
        print("2. Ask for heals")
        print("3. flee")
        print("> ", end=' ')
        print(" ")
        raw_input = input()
        if raw_input == "1":
            hit_percent = [1, 2, 3,]
            hit_chance = random.choice(hit_percent)
            if hit_chance == 2:
                boss.health -= hero.power
                print("You hit the enemy for {}!".format(hero.power * 2))
            else:
                hero.health -= boss.power
                print("You missed the boss and have taken {} damage.".format(boss.power))
            if boss.health <= 0:
                print("The boss is dead.")
            if boss.alive == True:
                hit_percent = [1, 2, 3,]
                hit_chance = random.choice(hit_percent)
                if hit_chance == 2:
                    Hero.hero_health -= boss.boss_power
                    print("You have been hit for {}!".format(boss.power))
                else:
                    print("You evaded the boss's attack")
            if Hero.hero_health <= 0:
                print("You are dead.")
            print()
        elif raw_input == "2":
            Medic.m_heal()
        elif raw_input == "3":
            print("Goodbye.")
            enemy_select()
        else:
            print("Invalid input {}".format(raw_input))


enemy_select() # go to shop or start story
goblin_fight() # basic enemy
print("The goblin dropped $10")
shop(10)
enemy_select()
zombie_fight() # can only die from crit
print("The zombie dropped $10")
shop(10)
enemy_select()
shadow_fight() # 1 out of 10 chance to hit
print("The shadow dropped $10")
shop(20)
enemy_select()
boss_fight() # can evade attacks, if hit, your attack crits & he will not attack that turn



