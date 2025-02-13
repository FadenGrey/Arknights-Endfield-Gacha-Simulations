from ..libs import Gacha

class BatchLosses:
    @staticmethod
    def get_pull_losses(gacha: Gacha):
        losses = 0

        for banner in gacha.banners:
            for pull in banner.pulls:
                if pull.result == "Rate-Up" and not pull.batch == 0:
                    losses += 10-pull.pull_in_the_batch
        return losses
    
    @staticmethod
    def get_pull_losses_per_banner(gacha: Gacha):
        return BatchLosses.get_pull_losses(gacha) / len(gacha.banners)
    
    @staticmethod
    def get_rate_up_losses(gacha: Gacha):
        losses = 0

        for banner in gacha.banners:
            if banner.target_rate_up_number < banner.rate_up_count:
                losses += banner.rate_up_count-banner.target_rate_up_number
        return losses
    
    @staticmethod
    def get_rate_up_losses_per_banner(gacha: Gacha):
        return BatchLosses.get_rate_up_losses(gacha) / len(gacha.banners)