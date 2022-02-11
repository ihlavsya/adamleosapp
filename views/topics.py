from flask import Blueprint, render_template
from utils import get_id_from_entity_name
from DTOs.TopicProfileDto import TopicProfileDto
from repositories.PostRepository import PostRepository
from repositories.TopicRepository import TopicRepository
from services import get_topic_profile

topics = Blueprint("topics", __name__)


@topics.route('/<topic_name>')
def get_topic(topic_name: str):
    id: int = get_id_from_entity_name(topic_name)
    topic_profile: TopicProfileDto = get_topic_profile(id)
    return render_template('topic.html', topic_profile=topic_profile)