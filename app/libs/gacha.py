from .banner import Banner
from typing import List

class Gacha:
    def __init__(self, batch_distance = 0, target_rate_up_count = 1):
        self.banners: List[Banner] = []
        self.batch_distance = batch_distance
        self.target_rate_up_count = target_rate_up_count
        self.banners.append(Banner(0, 0, batch_distance, target_rate_up_count))

    def __repr__(self):
        return (f"banners={self.banners}")

    def pull(self):
        if self.banners[-1].is_banner_complete:
            last_banner = self.banners[-1]
            self.banners.append(Banner(last_banner.pull_number, last_banner.common_pity, self.batch_distance, self.target_rate_up_count))
        self.banners[-1].make_a_pull()

    def get_rate_up_pity(self):
        return self.banners[-1].rate_up_pity
    
    def get_common_pity(self):
        return self.banners[-1].common_pity
    
    def rateUpWon(self, base_roll=0, rate_up_roll=0):
        self.banners[-1].rateUpWon(base_roll, rate_up_roll)

    def standardWon(self, base_roll, rate_up_roll):
        self.banners[-1].standardWon(base_roll, rate_up_roll)

    def standardLose(self, base_roll):
        self.banners[-1].standardLose(base_roll)