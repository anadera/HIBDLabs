from src.Configuration import Configuration


class OracleScheme:
    def __init__(self, url):
        self.oracle_config = Configuration(url, "_oracle")
        self.Person_oracle = self.oracle_config.Base.classes.person
        self.Year_oracle = self.oracle_config.Base.classes.year
        self.Program_oracle = self.oracle_config.Base.classes.program
        self.Mark_oracle = self.oracle_config.Base.classes.mark
        self.Subject_oracle = self.oracle_config.Base.classes.subject
        self.Subdivision_oracle = self.oracle_config.Base.classes.subdivision
        self.Employee_oracle = self.oracle_config.Base.classes.employee




