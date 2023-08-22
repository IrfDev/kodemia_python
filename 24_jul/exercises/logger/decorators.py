import Log


def create_new_log(func):
    def wrapper(entity_class):
        func(entity_class)

        entity = type(entity_class).__name__
        action = "save"
        state = "completed"
        payload = entity_class.as_dict()

        new_log = Log.Logger(action, entity, state, payload)
        new_log.save()

    return wrapper


def print_log(func):
    def wrapper(entity_class):
        func(entity_class)
        formatted_entity: dict = entity_class.as_dict()

        print(f"The new entity was created: \n {formatted_entity.items()}")

    return wrapper
