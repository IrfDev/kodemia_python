from EntityClass import Entity


class Comment(Entity):
    def __init__(self, content, created_by, article):
        super().__init__(type(self).__name__)
        self.content = content
        self.created_by = created_by
        self.article = article

    def as_dict(self):
        return {
            "content": self.content,
            "created_by": self.created_by,
            "article": self.article,
        }
