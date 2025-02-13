from app.configs import Inputs, Outputs
from app.gacha import CharacterGacha
from app.outputs import GachaLogs
from app.outputs import Graph

inputs = Inputs()
outputs = Outputs()

pull_target = inputs.pull_target
target_rate_up_number = inputs.target_rate_up_number
batch_distance = inputs.batch_distance

# Pulling happening here
gacha = CharacterGacha.roll_the_gacha(pull_target, batch_distance, target_rate_up_number)

# Show each individual pull info
if outputs.individual_pulls_info:
    GachaLogs.show_logs(gacha, outputs.individual_pulls_info.number_of_banners)

# Show statistics
if outputs.summary or outputs.burned_resources or outputs.sums:
    GachaLogs.show_statistics(gacha, outputs.summary, outputs.burned_resources, outputs.sums)

# Draw a graph
if outputs.graph.enable:
    Graph.draw(gacha, outputs.graph.x_range, outputs.graph.y_range)

