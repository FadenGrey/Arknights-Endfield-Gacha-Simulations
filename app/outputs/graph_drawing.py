#Draw the graph
from ..libs.gacha import Gacha
from collections import Counter
import pandas as pd
import plotly.express as px
import statistics

class Graph:
    @staticmethod
    def draw(gacha: Gacha, x:int = 1300, y:int = 100000):
        x_range = [-2,x]
        y_range = [-10,y]
        successfulPulls = []
        for banner in gacha.banners:
            for pull in banner.pulls:
                if pull.result == "Rate-Up": successfulPulls.append(pull.pull_number)

        frequency = Counter(successfulPulls)
        df = pd.DataFrame(frequency.items(), columns=['Pull','Frequency'])
        df = df.sort_values('Pull')
        fig = px.scatter(df, x='Pull', y='Frequency', title=('Rate-Up Characters Rolls (Arknights Endfield)'))
        fig.add_vline(
            x = statistics.median(successfulPulls),
            line_color = "red",
            annotation_text = f"Median: {statistics.median(successfulPulls):.2f}",
            annotation_position = "top right"
            )
        fig.update_xaxes(title_text='Pull',range=x_range)
        fig.update_yaxes(title_text='Frequency',range=y_range)
        fig.update_traces(mode='lines+markers', line_shape='spline',line_color='orange',marker_color='orange')
        fig.show()