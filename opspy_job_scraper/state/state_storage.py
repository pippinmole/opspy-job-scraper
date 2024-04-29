import json

from cfkv import KVStore

from opspy_job_scraper import State


class StateStorage(object):
    def __init__(self, store: KVStore):
        self.store = store

    def get_current_state(self) -> State:
        state = State(0, 0)
        state_str = self.store.get("state")

        if state_str is not None:
            # Parse state_str json into state
            state = json.loads(state_str, object_hook=lambda d: State(**d))

        return state

    def set_current_state(self, state: State):
        # json_str = json.dumps(state)
        successful = self.store.set("state", state.__dict__)

        # Throw error if not successful
        if not successful:
            raise Exception("Failed to set current state")
