from utils import get_link

class ReferenceTopicDto():
    def __init__(self, topic_id: int, name: str, eng_descr: str):
        self.topic_id = topic_id
        self.name = name
        self.eng_descr = eng_descr
        self.link = get_link(topic_id, eng_descr)