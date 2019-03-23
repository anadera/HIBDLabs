create table person (
    id integer primary key,
    surname varchar(50) not null,
    name varchar(50) not null,
    patronymic varchar(50),
    date_of_birth date not null,
    place_of_birth varchar(50),
    unique(surname, name, patronymic, date_of_birth, place_of_birth)
);


create table year (
    name varchar(4) primary key,
    startDate date,
    endDate date
);

create table program (
    id integer primary key,
    name varchar(50),
    code varchar(25)
);

create table specialization (
    id integer primary key,
    name varchar(50),
    code varchar(50),
    program_id references program(id)
);

create table subdivision (
    name varchar(50) primary key,
    type varchar(1)
);

create table group_info (
    id integer primary key,
    name varchar(50),
    year_name references year(name), 
    subdivision_name varchar(50) references subdivision(name),
    specialization_id integer references specialization(id),
    courseNumber integer
);

create table student (
    id integer primary key,
    person_id integer references person(id),
    group_id integer references group_info(id),
    type_of_study varchar(2),
    form_of_study varchar(1),
    qualification varchar(10)
);

create table employee (
    id integer primary key,
    person_id integer references person(id),
    subdivision_name varchar(50) references subdivision(name),
    position varchar(20),
    startDate date,
    endDate date,
    unique(person_id, subdivision_name, position, startDate)
);

drop table group_schedule;
drop table employee;


create table subject (
    name varchar(100) primary key
);

create table schedule_info (
    id integer primary key,
    subject_name varchar(100) references subject(name),
    teacher_id integer references employee(id),
    day_of_week integer not null,
    start_time date,
    end_time date,
    type_of_week varchar(2),
    room varchar(5)
);

create table group_schedule (
    id integer primary key,
    group_id integer references group_info(id),
    schedule_id integer references schedule_info(id)
);

create table mark (
    name integer primary key,
    letter varchar(1)
);


create table result (
    id integer primary key,
    subject_name  varchar(100) references subject(name),
    mark_value integer references mark(name),
    student_id references student(id)
);



insert into person values (1, 'Ivanov', 'Ivan', 'Ivanovich', to_date('1997-02-03', 'yyyy-mm-dd'), 'Saint-Petersburg');
insert into person values (2, 'Ivanov', 'Petr', 'Petrovich', to_date('1983-01-01', 'yyyy-mm-dd'), 'Moscow');
insert into person values (3, 'Petrova', 'Maria', null, to_date('1998-01-01', 'yyyy-mm-dd'), 'Pskov');
insert into person values (4, 'Sidorov', 'Aleksandr', 'Petrovich', to_date('2000-01-03', 'yyyy-mm-dd'), 'Moscow');

insert into year values (2017, to_date('2017-09-01', 'yyyy-mm-dd'), to_date('2018-05-31', 'yyyy-mm-dd') );

insert into program values (1, 'Software engineering', '09.03.04');

insert into specialization values (1, 'spec1', '09.03.04.01', 1);

insert into subdivision values ('subdivisio1', '1');

insert into group_info values (1, 'P1111', 2017, 'subdivisio1', 1, 1);

insert into subject values ('HIBD');
insert into subject values ('networks');

insert into mark values (5, 'A');
insert into mark values (4, 'B');
insert into mark values (3, 'C');
insert into mark values (2, 'D');

insert into employee values (1, 1, 'subdivisio1', 'teacher', to_date('2014-09-01', 'yyyy-mm-dd'), null);
insert into employee values (2, 2, 'subdivisio1', 'dean', to_date('2014-09-01', 'yyyy-mm-dd'), null);

insert into student values (1, 3, 1, '1', '1', null);
insert into student values (2, 4, 1, '2', '1', null);

insert into result values (1, 'HIBD', 4, 1);
insert into result values (2, 'HIBD', 5, 2);

insert into schedule_info values (1, 'HIBD', 1, 1, to_date('10:30', 'hh24:mi'),   to_date('12:00', 'hh24:mi'), null, '234');
insert into group_schedule values (1, 1, 1);

commit;




