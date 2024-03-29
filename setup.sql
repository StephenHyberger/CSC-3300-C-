create database assignment4;

use assignment4;

create table department (dept_name varchar(20), building varchar(15), budget numeric(12,2) check (budget > 0), primary key (dept_name));

create table course (course_id varchar(8), title varchar(50), dept_name varchar(20), credits numeric(2,0) check (credits >0), primary key (course_id), foreign key (dept_name) references department(dept_name) on delete set null);

create table instructor (ID varchar(5), name varchar(20) not null, dept_name varchar(20), salary numeric(8,2) check (salary > 29000), primary key (ID), foreign key (dept_name) references department(dept_name) on delete set null);

INSERT INTO department (dept_name, building, budget) VALUES ('Biology', 'Watson', 90000), ('Comp. Sci.', 'Taylor', 100000), ('Elec. Eng.', 'Taylor', 85000), ('Finance', 'Painter', 120000), ('History', 'Painter', 50000), ('Music', 'Packard', 80000), ('Physics', 'Watson', 70000);

INSERT INTO course (course_id, title, dept_name, credits) VALUES ('BIO-101', 'Intro.to Biology', 'Biology', 4), ('BIO-301', 'Genetics', 'Biology', 4), ('BIO-399', 'Computational Biology', 'Biology', 3), ('CS-101', 'Intro. to Computer Science', 'Comp. Sci.', 4), ('CS-190', 'Game Design', 'Comp. Sci.', 4), ('CS-315', 'Robotics', 'Comp. Sci.', 3), ('CS-319', 'Image Processing', 'Comp. Sci.', 3), ('CS-347', 'Database System Concepts', 'Comp. Sci.', 3), ('EE-181', 'Intro. to Digital Systems', 'Elec. Eng.', 3), ('FIN-201', 'Investment Banking', 'Finance', 3), ('HIS-351', 'World History', 'History', 3), ('MU-191', 'Music Video Production', 'Music', 3), ('PHY-101', 'Physical Principles', 'Physics', 4);

INSERT INTO instructor (ID, name, dept_name, salary) VALUES ('10101', 'Srinivasan', 'Comp. Sci.', 65000), ('12121', 'Wu', 'Finance', 90000), ('15151', 'Mozart', 'Music', 40000), ('22222', 'Einstein', 'Physics', 95000), ('32343', 'El Said', 'History', 60000), ('33456',  'Gold', 'Physics', 87000), ('45565', 'Katz', 'Comp. Sci.', 75000), ('58582', 'Califieri',  'History', 62000), ('76543', 'Singh', 'Finance', 80000), ('76766', 'Crick', 'Biology',  72000), ('83821', 'Brandt', 'Comp. Sci.', 92000), ('98345', 'Kim', 'Elec. Eng.', 80000);

create user 'weak'@'localhost' identified by 'password1';
grant select on * to 'weak'@'localhost';

create user 'medium'@'localhost' identified by 'password2';
grant select, insert, update on * to 'medium'@'localhost';

create user 'strong'@'localhost' identified by 'password3';
grant all on * to 'strong'@'localhost';
