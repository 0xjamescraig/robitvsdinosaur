import Robot

class Dinosaur:
    health = 100
    def __init__(self, name, attack_power):
        self.name= name
        self.attack_power = attack_power
        
    def attack(self, robot):
        Robot.Robot.health -= self.attack_power