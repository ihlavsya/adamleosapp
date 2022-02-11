from DTOs.ReferenceTopicDto import ReferenceTopicDto
from DTOs.ReferencePostDto import ReferencePostDto
from utils import get_link


class FullPostDto():
    def __init__(self) -> None:
        pass


    def __init__(self, post_id: int, header: str, text_html: str, references_html: str,
                 imgpath_original: str, eng_descr: str, next_refPostDto: ReferencePostDto,
                 prev_refPostDto: ReferencePostDto, topic: ReferenceTopicDto):
        self.topic = topic
        self.post_id = post_id
        self.header = header
        self.text_html = text_html
        self.references_html = references_html
        self.imgpath_original = imgpath_original
        self.next_post = next_refPostDto
        self.prev_post = prev_refPostDto
        self.eng_descr = eng_descr
        self.link = get_link(post_id, eng_descr)

