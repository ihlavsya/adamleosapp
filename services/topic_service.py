from typing import List, Optional
from DTOs.ReferenceTopicDto import ReferenceTopicDto
from DTOs.ShortPostDto import ShortPostDto
from DTOs.TopicProfileDto import TopicProfileDto
from repositories.PostRepository import PostRepository
from repositories.TopicRepository import TopicRepository
from shared import Order


def get_topic_profile(topic_id: int) -> TopicProfileDto:
    topic: ReferenceTopicDto = None
    with TopicRepository() as topic_repository:
        topic = topic_repository.get_topic(topic_id)

    posts: List[ShortPostDto] = None
    with PostRepository() as post_repository:
        posts = post_repository.get_short_posts_by_topic_id(topic_id, Order.ASC)

    topic_profile: TopicProfileDto = TopicProfileDto(topic.topic_id, topic.name, topic.eng_descr, posts)
    return topic_profile


def get_latest_topics(order: Optional[Order]=Order.DESC) -> List[TopicProfileDto]:
    topics: List[ReferenceTopicDto] = None
    with TopicRepository() as topic_repository:
        topics = topic_repository.get_all_topics(order)

    topic_profiles: List[TopicProfileDto] = list()
    for topic in topics:
        posts: List[ShortPostDto] = None
        with PostRepository() as post_repository:
            posts = post_repository.get_short_posts_by_topic_id(topic.topic_id, Order.DESC, 2)
        topic_profile: TopicProfileDto = TopicProfileDto(topic.topic_id, topic.name, topic.eng_descr, posts)
        topic_profiles.append(topic_profile)
    return topic_profiles