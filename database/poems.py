import random
from database.library_models import PoemModel, AuthorModel
from database.query import query, sql_templates

class Poems:
    def __init__(self, db_instance):
        self.db = db_instance
        self.poem_model = PoemModel()
        self.author_model = AuthorModel()

    def get_poem_count(self):
        sql = "SELECT COUNT(*) FROM {};".format(self.poem_model.table_name)
        count = query(self.db.cursor, sql, "one")
        return int(count[0])

    def get_poem_ids(self):
        sql = "SELECT {} FROM {};".format(self.poem_model.col_poem_id,
                                          self.poem_model.table_name)
        poem_ids = query(self.db.cursor, sql)
        return poem_ids

    def get_all_poems(self):
        sql = "SELECT * FROM {};".format(self.poem_model.table_name)
        poem_ids = query(self.db.cursor, sql)
        return poem_ids

    def get_random_poem(self):
        poems = self.get_all_poems()
        rand_num = random.randint(0, len(poems)-1)
        return poems[rand_num]
