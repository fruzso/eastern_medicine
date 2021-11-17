init python:
    class Almos(object):
        def __init__(self):
            # Basic
            self.NAME = "Almos"
            self.AGE = 250
            self.CLAN = "Toreador"
            self.QUOTE = "It’s not what you look at that matters, it’s what you see."

            # Attributes
            self.STRENGTH = 1
            self.DEXTERITY = 1
            self.STAMINA = 1

            self.CHARISMA = 1
            self.MANIPULATION = 1
            self.COMPOSURE = 1
            
            self.INTELLIGENCE = 1
            self.WITS = 1
            self.RESOLVE = 1

            # Skills
            self.ATHLETICS = 1
            self.BRAWL = 1
            self.CRAFT = 1
            self.DRIVE = 1
            self.FIREARMS = 1
            self.MELEE = 1
            self.LARCENY = 1
            self.STEALTH = 1
            self.SURVIVAL = 1

            self.ANIMAL_KEN = 1
            self.ETIQUETTE = 1
            self.INSIGHT = 1
            self.INTIMIDATION = 1
            self.LEADERSHIP = 1
            self.PERFORMANCE = 1
            self.PERSUASION = 1
            self.STREETWISE = 1
            self.SUBTERFUGE = 1

            self.ACADEMICS = 1
            self.AWARENESS = 1
            self.FINANCE = 1
            self.INVESTIGATION = 1
            self.MEDICINE = 1
            self.OCCULT = 1
            self.POLITICS = 1
            self.SCIENCE = 1
            self.TECHNOLOGY = 1

            # Almos Disciplines
            self.AUSPEX = 1
            self.CELERITY = 1
            self.PRESENCE = 1

            # Other disciplines
            self.OBFUSCATE = 0
            self.DOMINATE = 0
            self.FORTITUDE = 0
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
