import mysql.connector

def get_connection():
    return mysql.connector.connect(user='root', database='adamleos', password='RJ!n6iey!8qE32ne')

class RepositoryException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors


# base Repository class
class Repository():
    def __init__(self):
        try:
            self.conn = get_connection()
        except Exception as e:
            raise RepositoryException(*e.args, **e.kwargs)
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        # can test for type and handle different situations
        self.close()

    def complete(self):
        self._complete = True

    def close(self):
        if self.conn:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                raise RepositoryException(*e.args)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    raise RepositoryException(*e.args)
