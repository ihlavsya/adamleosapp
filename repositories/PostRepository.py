from repositories.Repository import Repository, RepositoryException
from DTOs.FullPostDto import FullPostDto
from DTOs.ShortPostDto import ShortPostDto
from models.Post import Post
import mapper


class PostRepository(Repository):
    def get_fullpost(self, post_id: int) -> FullPostDto:
        c = self.conn.cursor()
        stmt = '''
        SELECT cur.PostID, cur.TopicID, cur.Header, 
        cur.TextHtml, cur.ReferencesHtml, 
        cur.ImagePath_Original, cur.EngDescription, 
        cur.NextPostId, cur.PreviousPostID,
        prev.Header, prev.EngDescription, next.Header, next.EngDescription, 
        Topics.Name, Topics.EngDescription,
        t_prev.TopicID, t_prev.Name, t_prev.EngDescription,
        t_next.TopicID, t_next.Name, t_next.EngDescription
        FROM Posts cur
        INNER JOIN Topics On cur.TopicID=Topics.TopicID
        INNER JOIN Posts prev On prev.PostID=cur.PreviousPostID
        INNER JOIN Posts next On next.PostID=cur.NextPostID
        INNER JOIN Topics t_prev On prev.TopicID=t_prev.TopicID
        INNER JOIN Topics t_next On next.TopicID=t_next.TopicID
        where cur.PostID={0}
        '''.format(post_id)
        c.execute(stmt)
        result = c.fetchone()
        post: FullPostDto = mapper.FromQueryResToPost(result)
        return post

    def get_short_posts_by_topic_id(self, topic_id: int) -> list[ShortPostDto]:
        c = self.conn.cursor()
        stmt = '''
        SELECT p.PostID, p.Header, p.EngDescription, 
        p.ShortText, p.ImagePath_Original, 
        p.NumberInLine, Tags.Name
        from Posts p
        INNER JOIN Topics ON p.TopicID=Topics.TopicID
        INNER JOIN PostsTags pt ON p.PostID=pt.PostID
        INNER JOIN Tags ON pt.TagID=Tags.TagID
        WHERE Topics.TopicID={0}
        ORDER BY p.NumberInLine ASC
        '''.format(topic_id)
        c.execute(stmt)
        result = c.fetchall()
        posts: list[ShortPostDto] = mapper.FromQueryResToShortPosts(result)
        return posts

    def add_post(self, post: Post):
        try:
            c = self.conn.cursor()
            # insert_stmnt: str = '''INSERT INTO Posts
            # (TopicID, NextPostID,
            # PreviousPostID, Header,
            # ReferencesHtml, TextHtml,
            # EngDescription, ImagePath_Original)
            # VALUES (%d, %d, %d, %s, %s, %s, %s, %s)'''
            # post_data = (post.topic_id, post.next_post_id, post.previous_post_id,
            #              post.header, post.references_html, post.text_html, post.eng_descr, post.imgpath_original)
            # c.execute(insert_stmnt, post_data)
            # for result in c.execute("select * from Posts", multi=True):
            #     if result.with_rows:
            #         print("Rows produced by statement '{}':".format(
            #         result.statement))
            #         print(result.fetchall())
            #     else:
            #         print("Number of rows affected by statement '{}': {}".format(
            #         result.statement, result.rowcount))
            # insert_stmnt = '''INSERT INTO Posts
            # (TopicID, NextPostID,
            # PreviousPostID)
            # VALUES (%d, %d, %d)'''
            # post_data = (post.topic_id, post.next_post_id, post.previous_post_id)
            # c.execute(insert_stmnt, post_data)
            # this needs an appropriate table
            # c.execute('''INSERT INTO Posts (TopicID, Header,
            # ImagePath_Original, NextPostID,
            # PreviousPostID, ReferencesHtml,
            # TextHtml, EngDescription) VALUES (%d, %s, %s, %d, %d, %s, %s, %s)''', (post.topic_id, post.header, post.imgpath_original,
            #           post.next_post_id, post.previous_post_id, post.references_html, post.text_html, post.eng_descr))
        except Exception as e:
            raise RepositoryException('error storing post')
