class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def attack(self, goblin):
        goblin.health -= hero.power
        print("You do %d damage to the goblin." % hero.power)
        if goblin.health <= 0:
            print("The goblin is dead.")
            
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
        
class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def attack(self, hero):
        hero.health -= goblin.power
        print("The goblin does %d damage to you." % goblin.power)
        if hero.health <= 0:
            print("You are dead.")
            
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():
    
    while goblin.alive() and hero.alive():
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)

main()