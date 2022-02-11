from DTOs.ShortPostDto import ShortPostDto
from utils import get_link


class TopicProfileDto():
    def __init__(self, topic_id: int, name: str, eng_descr: str, posts: list[ShortPostDto]):
        self.topic_id = topic_id
        self.name = name
        self.eng_descr = eng_descr
        self.posts = posts
