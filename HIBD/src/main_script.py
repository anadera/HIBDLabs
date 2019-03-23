from src.MySqlScheme import MySqlScheme
from src.OracleScheme import OracleScheme
from src.ResultScheme import ResultScheme


def generateNewPersonWithEmployeeFromMySql(person, maxEmployeeId):
    names = person.full_name.split(' ')
    employeeCollection = generateEmployeesFromMysql(person, maxEmployeeId)
    return result.Person_result(id=person.id, surname=names[0],
                                name=names[1] if names.size() > 1 else None,
                                patronymic=names[2] if names.size() > 2 else None,
                                dateofbirth=person.dateofbirth,
                                employeeCollection=employeeCollection)


def generateEmployeesFromMysql(person, maxEmployeeId):
    employeeCollection = []
    for project in person.project_member_collection:
        employeeCollection.append(result.Employee_result(id=maxEmployeeId, position=person.position_name,
                                                         startdate=project.start_date, enddate=project.end_date,
                                                         project_members_collection=[
                                                             result.Project_member_result(id=project.id,
                                                                                          project_name=project.project_name,
                                                                                          member_id=maxEmployeeId)]))
    return employeeCollection


def generateEmployeesFromOracle(person):
    employeeCollection = []
    for employee in person.employee_collection:
        employeeCollection.append(result.Employee_result(id=employee.id,
                                                         subdivision_name=employee.subdivision_name,
                                                         position=employee.position,
                                                         startdate=employee.startdate,
                                                         enddate=employee.enddate))
    return employeeCollection


oracle = OracleScheme("oracle://first:12345@127.0.0.1:1521")
mysql = MySqlScheme('mysql://root:12345@localhost/university_info')
result = ResultScheme('oracle://result:PASS1@127.0.0.1:1521')

persons_oracle = oracle.oracle_config.session.query(oracle.Person_oracle).all()
years_oracle = oracle.oracle_config.session.query(oracle.Year_oracle).all()
subdivision_oracle = oracle.oracle_config.session.query(oracle.Subdivision_oracle).all()
subjects_oracle = oracle.oracle_config.session.query(oracle.Subject_oracle).all()
programs_oracle = oracle.oracle_config.session.query(oracle.Program_oracle).all()

persons_mysql = mysql.my_sql_config.session.query(mysql.Person_mysql).all()
conferences_mysql = mysql.my_sql_config.session.query(mysql.Conference_mysql).all()
projects_mysql = mysql.my_sql_config.session.query(mysql.Scientific_project_mysql).all()
publishers_mysql = mysql.my_sql_config.session.query(mysql.Publisher_mysql).all()

result_people = {}

result.clear()

for year in years_oracle:
    result.result_config.session.add(
        result.Year_result(year_name=year.name, startdate=year.startdate, enddate=year.enddate))
    result.result_config.session.commit()
for subdivision in subdivision_oracle:
    result.result_config.session.add(
        result.Subdivision_result(name=subdivision.name))
    result.result_config.session.commit()
for project in projects_mysql:
    result.result_config.session.add(
        result.Scientific_project_result(name=project.name))
    result.result_config.session.commit()
for subject in subjects_oracle:
    result.result_config.session.add(
        result.Subject_result(name=subject.name))
    result.result_config.session.commit()
for program in programs_oracle:
    result.result_config.session.add(
        result.Program_result(id=program.id, name=program.name, code=program.code))
    result.result_config.session.commit()

maxEmployeeId = max(oracle.oracle_config.session.query(oracle.Employee_oracle).all(), key=lambda x: x.id).id
for person in persons_oracle:
    result_people[person.id] = result.Person_result(id=person.id, surname=person.surname, name=person.name,
                                                    patronymic=person.patronymic, dateofbirth=person.dateofbirth,
                                                    placeofbirth=person.placeofbirth,
                                                    employee_collection=generateEmployeesFromOracle(person))

for person in persons_mysql:
    maxEmployeeId = maxEmployeeId + 1
    if (person.id not in result_people.keys()):
        result_people[person.id] = generateNewPersonWithEmployeeFromMySql(person, maxEmployeeId)
    else:
        original_person = result_people[person.id]
        result_people[person.id] = result.Person_result(id=original_person.id, surname=original_person.surname,
                                                        name=original_person.name,
                                                        patronymic=original_person.patronymic,
                                                        dateofbirth=original_person.dateofbirth,
                                                        placeofbirth=original_person.placeofbirth,
                                                        employee_collection=generateEmployeesFromMysql(
                                                            person, maxEmployeeId) + generateEmployeesFromOracle(
                                                            original_person))

for person in result_people.values():
    result.result_config.session.add(person)
    result.result_config.session.commit()
