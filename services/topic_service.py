from typing import List
from DTOs.ReferenceTopicDto import ReferenceTopicDto
from DTOs.ShortPostDto import ShortPostDto
from DTOs.TopicProfileDto import TopicProfileDto
from repositories.PostRepository import PostRepository
from repositories.TopicRepository import TopicRepository


def get_topic_profile(topic_id: int) -> TopicProfileDto:
    topic: ReferenceTopicDto = None
    with TopicRepository() as topic_repository:
        topic = topic_repository.get_topic(topic_id)

    posts: List[ShortPostDto] = None
    with PostRepository() as post_repository:
        posts = post_repository.get_short_posts_by_topic_id(topic_id)

    topic_profile: TopicProfileDto = TopicProfileDto(topic.topic_id, topic.name, topic.eng_descr, posts)
    return topic_profile