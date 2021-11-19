init python:
    class Almos(object):
        def __init__(self):
            # Basic
            self.NAME = "Almos"
            self.AGE = 179
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
            self.ANIMALISM = 2
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
