from src.Configuration import Configuration


class MySqlScheme:
    def __init__(self, url):
        self.my_sql_config = Configuration(url, "_my_sql")
        self.Person_mysql = self.my_sql_config.Base.classes.person
        self.Scientific_project_mysql = self.my_sql_config.Base.classes.scientific_project
        self.Conference_mysql = self.my_sql_config.Base.classes.conference
        self.Publisher_mysql = self.my_sql_config.Base.classes.publisher
