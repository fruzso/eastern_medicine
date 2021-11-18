$ compel_pool = pc_sheet.CHARISMA + pc_sheet.DOMINATE

init python:
    import random

    class Roll(object):
        def __init__(self, dice_pool, difficulty, n_hunger_dice):
            self.dice_pool = dice_pool
            self.difficulty = difficulty
            self.n_hunger_dice = n_hunger_dice

            self.n_success_simple = 0
            self.n_success_critical = 0
            self.n_failure_critical = 0
            self.success_sum = 0

            self.is_success = False
            self.is_failure = False
            self.is_bestial_failure = False
            self.margin_of_success = 0

        def _set_success_sum(self):
            self.success_sum = self.n_success_simple
            self.success_sum += self.n_success_critical if self.n_success_critical < 2 else self.n_success_critical * 2

        def _set_outcome(self):
            if self.success_sum >= self.difficulty:
                self.is_success = True
            else:
                # check for hunger dice
                if self.n_failure_critical > 0:
                    # a die has 1/dicepool probability to be a hunger die
                    # where the dicepool decreases by one with each dice roll
                    # until we reach the number of hunger dice 
                    denominator = self.dice_pool
                    for hunger_die in range(self.n_hunger_dice):
                        if random.randint(1,denominator) == 1:
                            self.is_bestial_failure = True 
                            break
                        denominator -= 1
                        if denominator == 0:
                            break
                else:
                    self.is_failure = True

        def _set_margin_of_success(self):
            self.margin_of_success = self.success_sum - self.difficulty

        def roll(self):
            for die in range(self.dice_pool):
                single_roll = random.randint(1,10)
                if single_roll > 5:
                    if single_roll == 10:
                        self.n_success_critical += 1
                    else:
                        self.n_success_simple += 1
                else:
                    if single_roll == 1:
                        self.n_failure_critical += 1
            
            self._set_success_sum()
            self._set_outcome()
            self._set_margin_of_success()




            
                
                

                        
            

