init python:
    class Janos(object):
        def __init__(self):
            # Basic
            self.NAME = "Janos"
            self.ASSUMED_GENDER = "gentleman"
            self.AGE = 250
            self.CLAN = "Nosferatu"
            self.QUOTE = "But I cheated and deformed by dissembling nature am determined to weigh upon the shoulder of the world."
            self.GENERATION = 10

            # Attributes
            self.STRENGTH = 4
            self.DEXTERITY = 4
            self.STAMINA = 3

            self.CHARISMA = 0
            self.MANIPULATION = 3
            self.COMPOSURE = 2
            
            self.INTELLIGENCE = 3
            self.WITS = 4
            self.RESOLVE = 4

            # Skills
            self.ATHLETICS = 3
            self.BRAWL = 3
            self.CRAFT = 2
            self.DRIVE = 2
            self.FIREARMS = 3
            self.MELEE = 1
            self.LARCENY = 3
            self.STEALTH = 3
            self.SURVIVAL = 3

            self.ANIMAL_KEN = 0
            self.ETIQUETTE = 1
            self.INSIGHT = 2
            self.INTIMIDATION = 3
            self.LEADERSHIP = 0
            self.PERFORMANCE = 0
            self.PERSUASION = 3
            self.STREETWISE = 3
            self.SUBTERFUGE = 3

            self.ACADEMICS = 2
            self.AWARENESS = 4
            self.FINANCE = 0
            self.INVESTIGATION = 3
            self.MEDICINE = 0
            self.OCCULT = 3
            self.POLITICS = 1
            self.SCIENCE = 0
            self.TECHNOLOGY = 2

            # Disciplines
            self.ANIMALISM = 2
            self.AUSPEX = 1
            self.CELERITY = 1
            self.DOMINATE = 2
            self.FORTITUDE = 1
            self.OBFUSCATE = 3
            self.PRESENCE = 0
            self.POTENCE = 1

            # Dynamic
            self.health = self.STAMINA + 3 + self.FORTITUDE
            self.willpower = self.COMPOSURE + self.RESOLVE
            self.hunger = 1

            # Other
            self.BLOOD_POTENCY = 2 # actual dicepool for rouse check

        def lose_health(self, damage):
            self.health -= damage
        
        def heal(self, health_points_gained):
            self.health += health_points_gained

        def lose_willpower(self, willpower_lost):
            self.willpower -= willpower_lost
        
        def gain_willpower(self, willpower_gained):
            self.willpower += willpower_gained

        def get_hungry(self, plus_hunger_points):
            self.hunger += plus_hunger_points

        def feed(self, blood_points):
            self.hunger -= blood_points
        
        def rouse_check(self):
            hunger_success = False
            for die in range(self.BLOOD_POTENCY):
                single_roll = renpy.random.randint(1,10)
                if single_roll > 5:
                    hunger_success = True
                    break
            
            if not hunger_success:
                self.get_hungry(1)
        
        def set_hunger_to_zero(self):
            self.hunger = 0

