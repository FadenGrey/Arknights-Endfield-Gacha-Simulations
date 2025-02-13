from typing import List

class PullChances:
    @staticmethod
    def get_chances(path = "pull_chances.csv") -> List:
        #Import pull chances
        import csv
        from pathlib import Path
        file = Path(__file__).with_name(path)
        with file.open("r", encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            chances = []
            for row in reader:
                for value in row:
                    chances.append(float(value))
        return(chances)