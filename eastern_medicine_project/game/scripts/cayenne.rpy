init python:
    class Cayenne(object):
        def __init__(self):
            # Basic
            self.NAME = "Cayenne"
            self.AGE = 183
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
            self.BLOOD_POTENCY = 1
            self.MAX_HUNGER = 5

        def lose_health(self, damage):
            self.health -= damage

        def lose_willpower(self, willpower_lost):
            self.willpower -= willpower_lost
        
        def _is_too_hungry(self):
            if self.hunger >= self.MAX_HUNGER:
                return True
            return False

        def get_hungry(self, plus_hunger_points):
            self.hunger += plus_hunger_points
            return self._is_too_hungry()

        def feed(self, blood_points):
            self.hunger -= blood_points
