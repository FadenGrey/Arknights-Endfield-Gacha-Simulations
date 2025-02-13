from .pull import Pull
from typing import List
import math

class Banner:
    def __init__(self, pull_number=0, common_pity = 0, batch_distance = 0, target_rate_up_number = 1):
        self.pulls: List[Pull] = []
        self.target_rate_up_number = target_rate_up_number
        self.common_pity = common_pity
        self.pull_number = pull_number
        self.rate_up_pity = self.rate_up_count = 0
        self.pull_in_batch_count = 1
        self.is_rate_up_pity = True
        self.is_batch_lucky = False
        self.is_banner_complete = False

        self.batch_distance = batch_distance
        if not self.batch_distance >= 80: self.batch = 1
        self.__recalculate_target_batch()
    
    def __repr__(self):
        return (f"pulls={self.pulls}")
    
    def make_a_pull(self):
        self.pull_number += 1
        self.common_pity += 1
        if self.is_rate_up_pity: self.rate_up_pity += 1
        self.pulls.append(Pull(self.pull_number, self.common_pity, self.rate_up_pity))
        if self.batch > 0: self.__put_in_batch()

    def __put_in_batch(self):
        self.pulls[-1].pull_in_the_batch = self.pull_in_batch_count
        self.pulls[-1].batch = self.batch            
        if self.pull_in_batch_count == 10:
            if self.rate_up_count >= self.target_rate_up_number: 
                self.is_banner_complete = True
            elif self.is_batch_lucky:
                self.__restart_batch()
                return
            elif self.batch < self.target_batch:
                self.batch += 1
                self.pull_in_batch_count = 0
            else: self.batch = 0
        self.pull_in_batch_count += 1

    def __recalculate_target_batch(self):
        max_common_pity_batch = math.trunc((80-self.batch_distance-self.common_pity)/10)
        max_rate_up_pity_batch = math.trunc((120-self.rate_up_pity)/10)

        if self.batch_distance >= 80 or max_common_pity_batch == 0 or max_rate_up_pity_batch == 0:
            self.batch = 0
            self.target_batch = 0
        else:
            if max_common_pity_batch > 0 and max_rate_up_pity_batch > 0:
                if max_common_pity_batch < max_rate_up_pity_batch:  self.target_batch = max_common_pity_batch
                else: self.target_batch = max_rate_up_pity_batch
            elif max_common_pity_batch > 0: self.target_batch = max_common_pity_batch
            elif max_rate_up_pity_batch > 0: self.target_batch = max_rate_up_pity_batch
            else: self.target_batch = 0

    def __restart_batch(self):
        self.__recalculate_target_batch()
        if self.target_batch > 0:
            self.is_batch_lucky = False
            self.batch = 1
            self.pull_in_batch_count = 1

    def standardLose(self, base_roll=0):
        self.pulls[-1].base_roll = base_roll

    def standardWon(self, base_roll=0, rate_up_roll=0):
        self.common_pity = 0
        self.is_batch_lucky = True
        self.pulls[-1].base_roll = base_roll
        self.pulls[-1].rate_up_roll = rate_up_roll
        self.pulls[-1].result = "Standard"
        if self.batch == 0 or self.pulls[-1].pull_in_the_batch == 10: self.__restart_batch()

    def rateUpWon(self, base_roll=0, rate_up_roll=0):
        self.is_rate_up_pity = False
        self.is_batch_lucky = True
        self.common_pity = 0
        self.rate_up_pity = 0
        self.pull_number = 0
        self.rate_up_count += 1
        self.pulls[-1].base_roll = base_roll
        self.pulls[-1].rate_up_roll = rate_up_roll
        self.pulls[-1].result = "Rate-Up"
        if self.rate_up_count >= self.target_rate_up_number and self.batch == 0:
            self.is_banner_complete = True
        elif self.batch == 0 or self.pulls[-1].pull_in_the_batch == 10: self.__restart_batch()
        
        