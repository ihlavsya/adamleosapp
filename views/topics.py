from flask import Blueprint, render_template
from utils import get_id_from_entity_name
from DTOs.TopicProfileDto import TopicProfileDto
from services import get_latest_topics, get_topic_profile
from typing import List

topics = Blueprint("topics", __name__)

@topics.route('/')
@topics.route('index.html')
def index():
    topic_profiles: List[TopicProfileDto] = get_latest_topics()
    return render_template('topics/index.html', topic_profiles=topic_profiles)

@topics.route('/<topic_name>')
def get_topic(topic_name: str):
    id: int = get_id_from_entity_name(topic_name)
    topic_profile: TopicProfileDto = get_topic_profile(id)
    return render_template('topic.html', topic_profile=topic_profile)