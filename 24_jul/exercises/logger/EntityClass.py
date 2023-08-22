import os
import decorators
import file_manager


class Entity:
    def __init__(self, name):
        current_path = os.path.dirname(__file__)
        file_name = f"{name}.json"
        self.file_path = current_path + f"/{file_name}"

    def get_all(self):
        return file_manager.read_json_file(self.file_path)

    @decorators.create_new_log
    @decorators.print_log
    def save(self):
        dict_log = self.__dict__

        try:
            file_manager.get_is_file_exist(self.file_path)
            file_manager.update_json_file(self.file_path, dict_log, True)
        except FileNotFoundError:
            file_manager.create_json_files(self.file_path, [dict_log])
