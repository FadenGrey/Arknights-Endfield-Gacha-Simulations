class Pull:
    def __init__(self, pull_number=0, common_pity=0, rate_up_pity=0, batch=0, pull_in_the_batch=0, base_roll=0, rate_up_roll=0):
        self.pull_number = pull_number
        self.common_pity = common_pity
        self.rate_up_pity = rate_up_pity
        self.batch = batch
        self.pull_in_the_batch = pull_in_the_batch
        self.base_roll = base_roll
        self.rate_up_roll = rate_up_roll
        self.result = "None" # "None", "Standard", "Rate-Up"
    
    def __repr__(self):
        return (f"pull_number={self.pull_number}, "
                f"common_pity={self.common_pity}, "
                f"rate_up_pity={self.rate_up_pity}, "
                f"batch={self.batch}, "
                f"pull_in_the_batch={self.pull_in_the_batch}), "
                f"base_roll={self.base_roll}), "
                f"rate_up_roll={self.rate_up_roll}), "
                f"result={self.result})")