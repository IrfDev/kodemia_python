import file_manager
import os

current_path = os.path.dirname(__file__)
COMMENT_FILE_NAME = "comments.json"
COMMENT_FILE_PATH = current_path + f"/{COMMENT_FILE_NAME}"


class Comment:
    def __init__(self, content, created_by, article):
        self.content = content
        self.created_by = created_by
        self.article = article

    def as_dict(self):
        return {
            "content": self.content,
            "created_by": self.created_by,
            "article": self.article,
        }

    def get_all(self):
        return file_manager.read_json_file(COMMENT_FILE_PATH)

    def save(self):
        dict_comment = self.as_dict()

        try:
            file_manager.get_is_file_exist(COMMENT_FILE_PATH)
            file_manager.update_json_file(COMMENT_FILE_PATH, dict_comment, True)

        except FileNotFoundError:
            file_manager.create_json_files(COMMENT_FILE_PATH, [dict_comment])
