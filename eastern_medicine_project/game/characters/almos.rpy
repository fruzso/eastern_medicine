init python:
    class Almos(object):
        def __init__(self):
            # Basic
            self.NAME = "Almos"
            self.ASSUMED_GENDER = "gentleman"
            self.AGE = 179
            self.SEX = "Male"
            self.CLAN = "Toreador"
            self.QUOTE = "It’s not what you look at that matters, it’s what you see."
            self.GENERATION = 10

            # Attributes
            self.STRENGTH = 3
            self.DEXTERITY = 3
            self.STAMINA = 3

            self.CHARISMA = 4
            self.MANIPULATION = 3
            self.COMPOSURE = 3
            
            self.INTELLIGENCE = 3
            self.WITS = 2
            self.RESOLVE = 3

            # Skills
            self.ATHLETICS = 3
            self.BRAWL = 2
            self.CRAFT = 1
            self.DRIVE = 2
            self.FIREARMS = 2
            self.MELEE = 2
            self.LARCENY = 0
            self.STEALTH = 0
            self.SURVIVAL = 2

            self.ANIMAL_KEN = 1
            self.ETIQUETTE = 3
            self.INSIGHT = 3
            self.INTIMIDATION = 2
            self.LEADERSHIP = 3
            self.PERFORMANCE = 3
            self.PERSUASION = 4
            self.STREETWISE = 2
            self.SUBTERFUGE = 2

            self.ACADEMICS = 3
            self.AWARENESS = 3
            self.FINANCE = 1
            self.INVESTIGATION = 2
            self.MEDICINE = 0
            self.OCCULT = 0
            self.POLITICS = 1
            self.SCIENCE = 2
            self.TECHNOLOGY = 3

            # Disciplines
            self.ANIMALISM = 0
            self.AUSPEX = 3
            self.CELERITY = 3
            self.DOMINATE = 0
            self.FORTITUDE = 1
            self.OBFUSCATE = 0
            self.PRESENCE = 3
            self.POTENCE = 0

            # Dynamic
            self.health = self.STAMINA + 3 + self.FORTITUDE
            self.willpower = self.COMPOSURE + self.RESOLVE
            self.hunger = 1

            # Other
            self.BLOOD_POTENCY = 1 # actual dicepool for rouse check
            self.MAX_WILLPOWER = self.COMPOSURE + self.RESOLVE
        
        def lose_health(self, damage):
            self.health -= damage
        
        def heal(self, health_points_gained):
            self.health += health_points_gained

        def lose_willpower(self, willpower_lost):
            self.willpower -= willpower_lost
        
        def gain_willpower(self, willpower_gained):
            if (self.willpower + willpower_gained) > self.MAX_WILLPOWER:
                self.willpower = self.MAX_WILLPOWER
            else:
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

            return hunger_success
        
        def set_hunger_to_zero(self):
            self.hunger = 0


