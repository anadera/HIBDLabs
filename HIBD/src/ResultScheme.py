from src.Configuration import Configuration


class ResultScheme:
    def __init__(self, url):
        self.result_config = Configuration(url, "_result")
        self.Subdivision_result = self.result_config.Base.classes.subdivision
        self.Person_result = self.result_config.Base.classes.person
        self.Employee_result = self.result_config.Base.classes.employee
        self.Student_result = self.result_config.Base.classes.student
        self.Year_result = self.result_config.Base.classes.year
        self.Group_result = self.result_config.Base.classes.group_info
        self.Program_result = self.result_config.Base.classes.program
        self.Specialization_result = self.result_config.Base.classes.specialization
        self.Schedule_result = self.result_config.Base.classes.schedule
        self.Mark_result = self.result_config.Base.classes.mark
        self.Scientific_project_result = self.result_config.Base.classes.scientific_project
        self.Conference_result = self.result_config.Base.classes.conference
        self.Conference_info_result = self.result_config.Base.classes.conference_info
        self.Publisher_result = self.result_config.Base.classes.publisher
        self.Publication_result = self.result_config.Base.classes.publication
        self.Reading_list_result = self.result_config.Base.classes.reading_list
        self.Subject_result = self.result_config.Base.classes.subject
        self.Project_member_result = self.result_config.Base.classes.project_members

    def clear(self):
        self.result_config.session.query(self.Person_result).delete()
        self.result_config.session.query(self.Year_result).delete()
        self.result_config.session.query(self.Subject_result).delete()
        self.result_config.session.query(self.Program_result).delete()
        self.result_config.session.query(self.Mark_result).delete()
        self.result_config.session.query(self.Scientific_project_result).delete()
        self.result_config.session.query(self.Conference_result).delete()
        self.result_config.session.query(self.Publisher_result).delete()
        self.result_config.session.query(self.Subdivision_result).delete()
