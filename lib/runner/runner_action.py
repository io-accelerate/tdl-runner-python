
class RunnerAction:
    def __init__(self, name, client_action):
        self.name = name
        self.client_action = client_action


class RunnerActions:
    def __init__(self):
        pass

    get_new_round_description = RunnerAction("get_new_round_description", "stop")
    test_connectivity = RunnerAction("test_connectivity", "stop")
    deploy_to_production = RunnerAction("deploy_to_production", "publish")

    all = [
        get_new_round_description,
        test_connectivity,
        deploy_to_production,
    ]
