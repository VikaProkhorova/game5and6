"""Classes for game"""
class Room():
    """Rooms of game"""
    def __init__(self, name):
        """Work with class"""
        self.name = name
        self.description = ''
        self.side = []
        self.character = None
        self.items = None

    def set_description(self, description):
        """Description of room"""
        self.description = description

    def get_details(self):
        """Print details of room"""
        print(self.name)
        print("--------------------")
        print(self.description)
        for room in self.side[::-1]:
            print(f'The {room[0].name} is {room[1]}')

    def link_room(self, other_room, side):
        """Information of linked room"""
        self.side.append([other_room, side])

    def set_character(self, character):
        """Is someone in room"""
        self.character = character

    def get_character(self):
        """Return Enemy room"""
        return self.character

    def move(self, where):
        """Move in other room"""
        for room in self.side:
            if room[1]== where:
                return room[0]

    def get_item(self):
        """Return item in room"""
        return self.items

    def set_item(self, items):
        """Add item in room"""
        self.items = items

class Character:
    """Class Character for characters in rooms"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        """Print information of character"""
        print(f'{self.name} is here!')
        print(self.description)

    def set_conversation(self, conversation):
        """Add conversation"""
        self.conversation = conversation
    def talk(self):
        """Character talk"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

class Enemy(Character):
    """Class of enemy of rooms"""
    def __init__(self, name, who):
        super().__init__(name, who)
        self.weakness = None
        self.conversation = None
        self.kills = 0

    def set_weakness(self, product):
        """Add weakness of enemy"""
        self.weakness = product

    def fight(self, item):
        """Fight with enemy"""
        if item == self.weakness:
            self.kills+=1
            print("You fend " + self.name + " off with the " + item)
            return True
        print(self.name + " crushes you, puny adventurer")
        return False

    def get_defeated(self):
        """Return number of kills enemies"""
        return self.kills

class Item():
    """Class Item for items in room"""
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        """Add description of item"""
        self.description = description

    def describe(self):
        """Print description of item"""
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        """Return name of item"""
        return self.name
