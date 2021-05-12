class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def print_status(self, type):
        print("%s: %d health and %d power." % (type, self.health, self.power))

class Hero(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        
    def attack(self, goblin):
        goblin.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if goblin.health <= 0:
            print("The goblin is dead.")
        
class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if hero.health <= 0:
            print("You are dead.")

hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():
    
    while goblin.alive() and hero.alive():
        hero.print_status("You")
        goblin.print_status("Goblin")
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