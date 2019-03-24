create table university
(
  id            integer primary key,
  name          varchar(50) not null,
  standart_type varchar(50),
  unique (name, standart_type)
);

create table faculty
(
  id            integer primary key,
  name          varchar(50) not null,
  university_id integer references university (id)
);

create table department
(
  id         integer primary key,
  name       varchar(50) not null,
  faculty_id integer references faculty (id)
);

create table major
(
  id            integer primary key,
  major_type    varchar(10),
  department_id integer references department (id)
);

create table student
(
  id       integer primary key,
  name     varchar(50) not null,
  major_id integer references major (id)
);

create table semester
(
  id       integer primary key,
  num      integer not null,
  major_id integer references major (id)
);

create table subject
(
  id       integer primary key,
  name     varchar(50) not null
);

create table subject_in_semester
(
  lectures     integer,
  practises    integer,
  labs         integer,
  control_type varchar(10),
  subject_id   integer references subject (id),
  semester_id  integer references semester (id)
);

create table scores
(
  score       integer,
  scoreDate   date,
  teacher_id  integer references teacher (id),
  subject_id  integer references subject (id),
  student_id  integer references student (id),
  semester_id integer references semester (id)
);

create table teacher
(
  id            integer primary key,
  name          varchar(50) not null,
  department_id integer references department (id)
);

create table teacher_subject
(
  teacher_id integer references teacher (id),
  subject_id integer references subject (id)
);

create table subject_major
(
  major_id   integer references major (id),
  subject_id integer references subject (id)
);



