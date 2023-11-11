class NBAPlayer:
    def __init__(self, name):
        self.name = name

class HOF:
    @staticmethod
    def is_in_hof(player):
        # determine Hall of Fame eligibilty
        return player.in_hof

class AllStar:
    @staticmethod
    def check_all_star(player):
        num_all_star_appearances = int(input(f"How many All-Star appearances does {player.name} have? "))
        if num_all_star_appearances > 5:
            player.in_hof = True

class Rings:
    @staticmethod
    def check_rings(player):
        num_rings = int(input(f"How many rings does {player.name} have? "))
        if num_rings > 2:
            player.in_hof = True

# User will input players name they want to see is eligible for the hall of fame
player_name = input("Enter the player's name: ")
player = NBAPlayer(player_name)

AllStar.check_all_star(player)
Rings.check_rings(player)

if HOF.is_in_hof(player):
    print(f"{player.name} is in the Hall of Fame!")
else:
    print(f"Sorry, {player.name} is not in the Hall of Fame yet.")



    

    
    
