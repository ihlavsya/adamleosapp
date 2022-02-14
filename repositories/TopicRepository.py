from typing import List
from DTOs.ReferenceTopicDto import ReferenceTopicDto
from repositories.Repository import Repository, RepositoryException
import mapper
from shared import Order


class TopicRepository(Repository):
    def get_topic(self, topic_id: int) -> ReferenceTopicDto:
        c = self.conn.cursor()
        stmt = '''
        SELECT Topics.TopicID, Topics.Name, Topics.EngDescription
        from Topics Where Topics.TopicID={0}
        '''.format(topic_id)
        c.execute(stmt)
        result = c.fetchone()
        topic: ReferenceTopicDto = mapper.FromQueryResToTopic(result)
        return topic

    def get_all_topics(self, order: Order) -> List[ReferenceTopicDto]:
        c = self.conn.cursor()
        stmt = '''
        SELECT Topics.TopicID, Topics.Name, 
        Topics.EngDescription, Topics.NumberInChronology
        from Topics ORDER BY Topics.NumberInChronology {0}'''.format(order.value)
        c.execute(stmt)
        result = c.fetchall()
        topics: List[ReferenceTopicDto] = [mapper.FromQueryResToTopic(row) for row in result]
        return topics