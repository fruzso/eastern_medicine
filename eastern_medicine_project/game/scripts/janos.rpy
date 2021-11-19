init python:
    class Janos(object):
        def __init__(self):
            # Basic
            self.NAME = "Janos"
            self.AGE = 250
            self.CLAN = "Nosferatu"
            self.QUOTE = "But I cheated and deformed by dissembling nature am determined to weigh upon the shoulder of the world."
            self.GENERATION = 8

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
