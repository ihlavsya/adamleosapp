class Post():
    def __init__(self) -> None:
        pass


    def __init__(self, topic_id, post_id, header, text_html, references_html,
                 imgpath_original, next_post_id, previous_post_id, eng_descr):
        self.topic_id = topic_id
        self.post_id = post_id
        self.header = header
        self.text_html = text_html
        self.references_html = references_html
        self.imgpath_original = imgpath_original
        self.next_post_id = next_post_id
        self.previous_post_id = previous_post_id
        self.eng_descr = eng_descr

