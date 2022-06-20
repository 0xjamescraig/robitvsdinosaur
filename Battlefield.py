import Dinosaur
import Robot
import random

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur.Dinosaur('Old Lace', 35)
        self.robot = Robot.Robot('Bishop')

    def run_game(self):
        random_number = random.randint(0, 1)
        if random_number == 0:
            print('Old Lace attacked Robot Bishop with a Power Loader for 35 damage')
            self.dinosaur.attack(self.robot)
        else:
            print('Robot Bishop attacked Old Lace with a Power Loader for 35 damage')
            self.robot.attack(self.dinosaur)
            
            
    def display_welcome(self):
        print('Welcome to an epic battle for the ages!')
        print('Only one side can win!')
        print()
    
    def battle_phase(self):
        print('Old Lace has', Dinosaur.Dinosaur.health, 'health remaining!')
        print('Robot Bishop has', Robot.Robot.health, 'health remaining!')
        
    def display_winner(self):
        if Dinosaur.Dinosaur.health <= 0:
            print('Robot Wins !!!')
        elif Robot.Robot.health <= 0:
            print('Dinosaur Wins !!!')