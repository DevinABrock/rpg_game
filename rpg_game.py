# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        # self.name = name
        # self.health = health
        # self.ower = power
    def attack(self, name, health, power):
        pass



class Hero:
    hero_health = 20
    hero_power = 4
    def h_attack():
        Goblin.goblin_health -= Hero.hero_power
        print("You do {} damage to the goblin.".format(Hero.hero_power))
        if Goblin.goblin_health <= 0:
            print("The goblin is dead.")
    def h_print_status():
        print("You have {} health and {} power.".format(Hero.hero_health, Hero.hero_power))

hero
class Goblin:
    goblin_health = 20
    goblin_power = 4
    def g_attack():
        if Goblin.goblin_health > 0:
            Hero.hero_health -= Goblin.goblin_power
            print("The goblin does {} damage to you.".format(Goblin.goblin_power))
            if Hero.hero_health <= 0:
                print("You are dead.")
    def g_print_status():
        print("The goblin has {} health and {} power.".format(Goblin.goblin_health, Goblin.goblin_power))


class Zombie:
    zombie_health = 20
    zombie_power = 4
    def z_attack():
        if Zombie.zombie_health > 0:
            Hero.hero_health -= Zombie.zombie_power
            print("The goblin does {} damage to you.".format(Zombie.zombie_power))
            if Hero.hero_health <= 0:
                print("You are dead.")
    def g_print_status():
        print("The goblin has {} health and {} power.".format(Zombie.zombie_health, Zombie.zombie_power))


# class Attack:
#     Goblin.goblin_health -= Hero.hero_power
#     print("You do {} damage to the goblin.".format(Hero.hero_power))
#     if Goblin.goblin_health <= 0:
#         print("The goblin is dead.")

def main():

    while Goblin.goblin_health > 0 and Hero.hero_health > 0:
        # Hero.h_print_status()
        # Goblin.g_print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            Hero.h_attack()
            Goblin.g_attack()
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

main()