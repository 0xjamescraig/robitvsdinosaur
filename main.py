import Battlefield
import Dinosaur, Robot

battlefield = Battlefield.Battlefield()
battlefield.display_welcome()
battlefield.battle_phase()

while (Dinosaur.Dinosaur.health > 0 and Robot.Robot.health > 0):
    battlefield.run_game()
    battlefield.battle_phase()
    
battlefield.display_winner()