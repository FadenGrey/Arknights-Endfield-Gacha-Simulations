from ..libs import Gacha
from app.outputs.batch_losses import BatchLosses
from colorama import Back, init
import statistics

class GachaStatistics:
    def __init__(self):
        self.target_rate_up_number = 1
        self.chars_on_rate_up_pity_count = 0
        self.successful_pulls = []
        self.rate_up_collected = 0
        self.maxed_rate_up_collected = 0
        self.standard_collected = 0
        self.rate_up_pulls_overall = 0
        self.rate_up_pulls_overall_max = 0
        self.rate_up_pulls_overalls = []

class GachaLogs:
    @staticmethod
    def show_logs(gacha: Gacha, max_banners: int = 0):
        init()
        for index, banner in enumerate(gacha.banners):
            print(f"#########[Banner {index+1}]#########")
            for pull in banner.pulls:
                if pull.result == "Standard": print(f"\033[47m{pull}\033[49m")
                elif pull.result == "Rate-Up": print(f"\033[43m{pull}\033[49m")
                else: print(pull)
                
                if pull.pull_in_the_batch == 10:
                    print("---")
            if max_banners!=0 and index == max_banners-1: break


    @staticmethod
    def show_statistics(
        gacha: Gacha,
        is_show_summary: bool = True,
        burned_resources: bool = True,
        sums: bool = True
        ):
        stats = GachaStatistics()
        rate_up_copies_count = 0

        for banner in gacha.banners:
            stats.rate_up_pulls_overall = 0
            for pull in banner.pulls:
                if pull.rate_up_pity == 120: stats.chars_on_rate_up_pity_count+=1
                if pull.result == "Rate-Up":
                    stats.rate_up_collected+=1
                    rate_up_copies_count+=1
                    stats.successful_pulls.append(pull.pull_number)
                    stats.rate_up_pulls_overall+=pull.pull_number
                elif pull.result == "Standard": stats.standard_collected+=1
            if rate_up_copies_count >= banner.target_rate_up_number: stats.maxed_rate_up_collected+=1
            if stats.rate_up_pulls_overall > stats.rate_up_pulls_overall_max: stats.rate_up_pulls_overall_max=stats.rate_up_pulls_overall
            stats.rate_up_pulls_overalls.append(stats.rate_up_pulls_overall)

        if is_show_summary:
            print (
            f"\n"
            f"###[Summary]###\n"
            f"We got {stats.chars_on_rate_up_pity_count} character on the 120's hard pity. Which is {round(stats.chars_on_rate_up_pity_count/stats.rate_up_collected*100, 2)}%\n"
            f"Average pull: {statistics.mean(stats.successful_pulls)}\n"
            f"Median pull: {statistics.median(stats.successful_pulls)}\n"
            f"Rate-up characters collected: {stats.rate_up_collected}\n"
            f"P{gacha.target_rate_up_count-1} Rate-up characters collected: {stats.maxed_rate_up_collected}\n"
            f"Standard collected: {stats.standard_collected}\n"
            f"Characters overall (Limited+Standard+Burned) collected: {stats.rate_up_collected+stats.standard_collected}"
            )
        
        if burned_resources:
            print (
            f"\n"
            f"###[Burned Resources]###\n"
            f"Pulls lost: {BatchLosses.get_pull_losses(gacha)}\n"
            f"Pulls per banner lost: {BatchLosses.get_pull_losses_per_banner(gacha)}\n"
            f"Rate-Up characters lost: {BatchLosses.get_rate_up_losses(gacha)}\n"
            f"Rate-Up characters per banner lost: {BatchLosses.get_rate_up_losses_per_banner(gacha)}"
            )

        if sums:
            print (
            f"\n"
            f"###[Sums]###\n"
            f"Average pulls sum: {statistics.mean(stats.rate_up_pulls_overalls)}\n"
            f"Median pulls sum: {statistics.median(stats.rate_up_pulls_overalls)}\n"
            f"Max pulls sum: {stats.rate_up_pulls_overall_max}"
            )