from ..libs import Gacha
from ..data import PullChances
import random

# Pulling simulations
class CharacterGacha:
    @staticmethod
    def roll_the_gacha(pull_target, target_batch, target_rate_up_number) -> Gacha:
        pull_target = pull_target
        target_batch = target_batch
        target_rate_up_number = target_rate_up_number

        gacha = Gacha(target_batch, target_rate_up_number)

        target_rolls = PullChances.get_chances()

        for _ in range (pull_target):
            gacha.pull()
            if gacha.get_rate_up_pity() == 120: gacha.rateUpWon(0, 0)
            else:
                base_roll = random.random()
                if base_roll <= target_rolls[gacha.get_common_pity()-1]:
                    rate_up_roll = random.random()
                    if rate_up_roll<0.5: gacha.rateUpWon(base_roll, rate_up_roll)
                    else: gacha.standardWon(base_roll, rate_up_roll)
                else: gacha.standardLose(base_roll)
        
        return gacha