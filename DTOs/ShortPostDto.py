from utils import get_link


class ShortPostDto():
    def __init__(self, post_id: int, header: str,
                 eng_descr: str, tag: str, short_text: str, 
                 imgpath_original: str, num_in_line: int):
        self.post_id = post_id
        self.header = header
        self.eng_descr = eng_descr
        self.tag = tag
        self.short_text = short_text
        self.imgpath_original = imgpath_original
        self.num_in_line = num_in_line
        self.link = get_link(post_id, eng_descr)
