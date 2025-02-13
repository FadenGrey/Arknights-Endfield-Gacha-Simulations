import json

class Inputs:
    def __init__(self):

        config_path = "app/configs/inputs.json"
        try:
            with open(config_path, 'r') as f:
                inputs = json.load(f)

                for input in inputs.get('inputs',[]):
                    if input['name'] == "pull_target": self.pull_target = input['number']
                    if input['name'] == "target_rate_up_number": self.target_rate_up_number = input['number']
                    if input['name'] == "batch_distance": self.batch_distance = input['number']

        except FileNotFoundError:
            print(f"The file {config_path} was not found.")
        except json.JSONDecodeError:
            print("The file could not be parsed as JSON. Check the file format.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

class Outputs:
    def __init__(self):
        config_path = "app/configs/outputs.json"
        try:
            with open(config_path, 'r') as f:
                outputs = json.load(f)
                for output in outputs.get('outputs',[]):
                    if output['name'] == "individual_pulls_info":
                        self.individual_pulls_info = self.IndividualPullsInfo(
                            output['parameters']['number_of_banners'],
                            output['parameters']['enable']
                            )
                    if output['name'] == "summary":
                        self.summary = output['parameters']['enable']
                    if output['name'] == "burned_resources":
                        self.burned_resources = output['parameters']['enable']
                    if output['name'] == "sums":
                        self.sums = output['parameters']['enable']
                    if output['name'] == "graph":
                        self.graph = self.Graph(
                            output['parameters']['x_range'],
                            output['parameters']['y_range'],
                            output['parameters']['enable']
                        )
                    

        except FileNotFoundError:
            print(f"The file {config_path} was not found.")
        except json.JSONDecodeError:
            print("The file could not be parsed as JSON. Check the file format.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    class Enabler():
        def __init__(self, enable: bool):
            self.enable = enable
        def __repr__(self):
            return (f"enable={self.enable}")

    class IndividualPullsInfo(Enabler):
        def __init__(self, number_of_banners: int, enable: bool):
            self.number_of_banners = number_of_banners
            super().__init__(enable)

        def __repr__(self):
            return (
                f"number_of_banners={self.number_of_banners}"
                )
        
    class Graph(Enabler):
        def __init__(self, x_range: int, y_range: int, enable: bool):
            self.x_range = x_range
            self.y_range = y_range
            super().__init__(enable)

        def __repr__(self):
            return (
                f"x_range={self.x_range}, "
                f"y_range={self.y_range}"
                )

