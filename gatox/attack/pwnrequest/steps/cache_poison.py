from gatox.attack.pwnrequest.steps.attack_step import AttackStep


class CachePoison(AttackStep):
    """ """

    def __init__(self, payload_path: str):
        """ """
        self.poison_payload = payload_path

    def preflight(self, previous_results=None):
        """Validates preconditions for executing this step."""
        pass

    def execute(self, api):
        """ """
        pass

    def handoff(self):
        """ """
        pass