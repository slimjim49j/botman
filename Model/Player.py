# Player inherits from Combatant
# Player data stored in database

# damage
# health
from Model.Combatant import Combatant


class Player(Combatant):

    def __init__(self):
        pass

    @staticmethod
    def get_player(discord_id):
        pass

    @staticmethod
    def create_player(player):
        pass

    def get_health(self, damage):
        pass

    def set_health(self, damage):
        pass

    def increment_currency(self, amount):
        pass

    def decrement_currency(self, amount):
        pass

    def level_up(self):
        pass
