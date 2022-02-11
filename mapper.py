from typing import List, Tuple
from DTOs.FullPostDto import FullPostDto
from DTOs.ReferencePostDto import ReferencePostDto
from DTOs.ReferenceTopicDto import ReferenceTopicDto
from DTOs.ShortPostDto import ShortPostDto


def FromQueryResToShortPosts(result: List[Tuple[str]]) -> List[ShortPostDto]:
    short_posts: List[ShortPostDto] = []
    for row in result:
        post_id = row[0]
        header = row[1]
        eng_descr = row[2]
        short_text = row[3]
        imgpath_original = row[4]
        num_in_line = row[5]
        tag = row[6]
        short_post = ShortPostDto(
            post_id, header, eng_descr, tag, short_text, imgpath_original, num_in_line)
        short_posts.append(short_post)
    
    return short_posts
        


def FromQueryResToTopic(result: List[str]) -> ReferenceTopicDto:
    topic_id = result[0]
    name = result[1]
    eng_descr = result[2]
    topic: ReferenceTopicDto = ReferenceTopicDto(topic_id, name, eng_descr)
    return topic


def FromQueryResToPost(result: List[str]) -> FullPostDto:
    post_id = result[0]
    topic_id = result[1]
    header = result[2]
    text_html = result[3]
    references_html = result[4]
    imgpath_original = result[5]
    eng_descr = result[6]

    next_post_id = result[7]
    previous_post_id = result[8]

    prev_header = result[9]
    prev_eng_descr = result[10]
    prev_topic_id = result[15]
    prev_topic_name = result[16]
    prev_topic_eng_descr = result[17]

    next_header = result[11]
    next_eng_descr = result[12]
    next_topic_id = result[18]
    next_topic_name = result[19]
    next_topic_eng_descr = result[20]

    topic_name = result[13]
    topic_eng_descr = result[14]
    topic: ReferenceTopicDto = ReferenceTopicDto(
        topic_id, topic_name, topic_eng_descr)
    prev_topic: ReferenceTopicDto = ReferenceTopicDto(
        prev_topic_id, prev_topic_name, prev_topic_eng_descr)
    next_topic: ReferenceTopicDto = ReferenceTopicDto(
        next_topic_id, next_topic_name, next_topic_eng_descr)
    prev_post: ReferencePostDto = ReferencePostDto(
        prev_topic, previous_post_id, prev_header, prev_eng_descr)
    next_post: ReferencePostDto = ReferencePostDto(
        next_topic, next_post_id, next_header, next_eng_descr)
    post: FullPostDto = FullPostDto(post_id, header, text_html, references_html, imgpath_original, eng_descr,
                                    next_post, prev_post, topic)
    return post
