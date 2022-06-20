import Dinosaur
import Weapon

class Robot:
    health = 100
    def __init__(self, name):
        self.name = name
        
    def attack(self, dinosaur):
        weapon = Weapon.Weapon('Power Loader', 35)
        Dinosaur.Dinosaur.health -= weapon.attack_power