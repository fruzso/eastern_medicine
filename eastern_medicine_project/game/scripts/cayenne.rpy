init python:
    class Cayenne(object):
        def __init__(self):
            # Basic
            self.NAME = "Cayenne"
            self.ASSUMED_GENDER = "lady"
            self.AGE = 183
            self.SEX = "Female"
            self.CLAN = "Malkavian"
            self.QUOTE = "Wildflower; pick up your pretty little head, it will get easier, your dreams are not dead."
            self.GENERATION = 10

            # Attributes
            self.STRENGTH = 2
            self.DEXTERITY = 4
            self.STAMINA = 2

            self.CHARISMA = 3
            self.MANIPULATION = 3
            self.COMPOSURE = 2
            
            self.INTELLIGENCE = 4
            self.WITS = 2
            self.RESOLVE = 3

            # Skills
            self.ATHLETICS = 3
            self.BRAWL = 3
            self.CRAFT = 1
            self.DRIVE = 0
            self.FIREARMS = 1
            self.MELEE = 3
            self.LARCENY = 3
            self.STEALTH = 2
            self.SURVIVAL = 0

            self.ANIMAL_KEN = 0
            self.ETIQUETTE = 0
            self.INSIGHT = 4
            self.INTIMIDATION = 1
            self.LEADERSHIP = 0
            self.PERFORMANCE = 3
            self.PERSUASION = 2
            self.STREETWISE = 0
            self.SUBTERFUGE = 0

            self.ACADEMICS = 3
            self.AWARENESS = 4
            self.FINANCE = 0
            self.INVESTIGATION = 2
            self.MEDICINE = 0
            self.OCCULT = 0
            self.POLITICS = 1
            self.SCIENCE = 2
            self.TECHNOLOGY = 1

            # Disciplines
            self.ANIMALISM = 0
            self.AUSPEX = 3
            self.CELERITY = 1
            self.DOMINATE = 2
            self.FORTITUDE = 0
            self.OBFUSCATE = 3
            self.PRESENCE = 0
            self.POTENCE = 0

            # Dynamic
            self.health = self.STAMINA + 3 + self.FORTITUDE
            self.willpower = self.COMPOSURE + self.RESOLVE
            self.hunger = 1

            # Other
            self.BLOOD_POTENCY = 1 # actual dicepool for rouse check

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

