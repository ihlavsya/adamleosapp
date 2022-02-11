from DTOs import ReferenceTopicDto
from utils import get_link

class ReferencePostDto():
    def __init__(self) -> None:
        pass


    def __init__(self, topic: ReferenceTopicDto, post_id: int, header: str, eng_descr: str):
        self.topic = topic
        self.post_id = post_id
        self.header = header
        self.eng_descr = eng_descr
        self.link = get_link(post_id, eng_descr)