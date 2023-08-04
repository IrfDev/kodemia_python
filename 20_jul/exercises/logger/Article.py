from EntityClass import Entity


class Article(Entity):
    def __init__(self, title, content, status, image, created_by):
        super().__init__(type(self).__name__)
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by

    def as_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "status": self.status,
            "image": self.image,
            "created_by": self.created_by,
        }
