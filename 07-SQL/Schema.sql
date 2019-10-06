-- Drop all tables if exist

DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;

--  Create schema  &&  IMport CSV to SQL QUERY TOOL
CREATE TABLE departments (
  dept_no character varying(45) NOT NULL,
  dept_name character varying(45) NOT NULL
);
COPY departments(dept_no, dept_name)
FROM 'D:\UNC data camp\Demo-unc\09-SQL\HomeWork\data\departments.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM departments;

CREATE TABLE dept_emp (
  emp_no integer NOT NULL ,
  dept_no character varying(45) NOT NULL,
  from_date DATE ,
  to_date DATE
);
COPY dept_emp(emp_no, dept_no, from_date, to_date)
FROM 'D:\UNC data camp\Demo-unc\09-SQL\HomeWork\data\dept_emp.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM dept_emp;

CREATE TABLE dept_manager (
  emp_no integer NOT NULL,
  dept_no character varying(45) NOT NULL,
  from_date DATE ,
  to_date DATE
);
COPY dept_manager(dept_no,	emp_no,	from_date,	to_date)
FROM 'D:\UNC data camp\Demo-unc\09-SQL\HomeWork\data\dept_manager.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM dept_manager;

CREATE TABLE employees (
  emp_no integer PRIMARY KEY NOT NULL,
  birth_date DATE ,
  first_name character varying(30) NOT NULL,
  last_name character varying(30) NOT NULL,
  gender CHAR(1) NOT NULL,
  hire_date DATE
);
COPY employees(emp_no,	birth_date,	first_name,	last_name,	gender,	hire_date)
FROM 'D:\UNC data camp\Demo-unc\09-SQL\HomeWork\data\employees.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM employees;

CREATE TABLE salaries (
  emp_no integer PRIMARY KEY NOT NULL,
  salary integer NOT NULL ,
  from_date DATE ,
  to_date DATE
);
COPY salaries(emp_no,	salary,	from_date,	to_date)
FROM 'D:\UNC data camp\Demo-unc\09-SQL\HomeWork\data\salaries.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM salaries;

CREATE TABLE titles (
  emp_no integer NOT NULL,
  title character varying(45) NOT NULL ,
  from_date DATE ,
  to_date DATE
);
COPY titles(emp_no,	title, from_date, to_date)
FROM 'D:\UNC data camp\Demo-unc\09-SQL\HomeWork\data\titles.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM titles;

