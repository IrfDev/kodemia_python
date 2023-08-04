import EntityClass
from datetime import date


class Logger(EntityClass.Entity):
    def __init__(self, action, entity, state, payload):
        super().__init__(type(self).__name__)
        self.action = action
        self.entity = entity
        self.state = state
        self.payload = payload
        self.created_at = date.today().isoformat()
        print(self)

    def as_dict(self):
        return {
            "action": self.action,
            "entity": self.entity,
            "state": self.state,
            "payload": self.payload,
            "created_at": self.created_at,
        }
