from flask import Blueprint, render_template
from utils import get_id_from_entity_name
from DTOs.FullPostDto import FullPostDto
from models.Post import Post
from repositories.PostRepository import PostRepository

posts = Blueprint("posts", __name__)


@posts.route('/<post_name>')
def get_post(post_name: str):
    id: int = get_id_from_entity_name(post_name)
    with PostRepository() as post_repository:
        post: FullPostDto = post_repository.get_fullpost(id)
        return render_template('post.html', post=post)


# @posts.route('/<topic_id>')
# def add_post(topic_id: int):
#     # id: int = get_id_from_entity_name(post_name)
#     with PostRepository() as post_repository:
#         post_repository.add_post(
#             Post(1, "check", "text", "refe", "smth", 3, 1, "descr"))
#     # return render_template('post.html')