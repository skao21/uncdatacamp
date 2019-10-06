DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;

--  IMport CSV to SQL QUERY TOOL
CREATE TABLE departments (
  dept_no character varying(45) NOT NULL,
  dept_name character varying(45) NOT NULL
);
COPY departments(dept_no, dept_name)
FROM 'D:\UNC data camp\HomeWork\Psql\data\departments.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM departments;

CREATE TABLE dept_emp (
  emp_no integer NOT NULL ,
  dept_no character varying(45) NOT NULL,
  from_date DATE ,
  to_date DATE
);
COPY dept_emp(emp_no, dept_no, from_date, to_date)
FROM 'D:\UNC data camp\HomeWork\Psql\data\dept_emp.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM dept_emp;

CREATE TABLE dept_manager (
  emp_no integer NOT NULL,
  dept_no character varying(45) NOT NULL,
  from_date DATE ,
  to_date DATE
);
COPY dept_manager(dept_no,	emp_no,	from_date,	to_date)
FROM 'D:\UNC data camp\HomeWork\Psql\data\dept_manager.csv' DELIMITER ',' CSV HEADER;
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
FROM 'D:\UNC data camp\HomeWork\Psql\data\employees.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM employees;

CREATE TABLE salaries (
  emp_no integer PRIMARY KEY NOT NULL,
  salary integer NOT NULL ,
  from_date DATE ,
  to_date DATE
);
COPY salaries(emp_no,	salary,	from_date,	to_date)
FROM 'D:\UNC data camp\HomeWork\Psql\data\salaries.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM salaries;

CREATE TABLE titles (
  emp_no integer NOT NULL,
  title character varying(45) NOT NULL ,
  from_date DATE ,
  to_date DATE
);
COPY titles(emp_no,	title, from_date, to_date)
FROM 'D:\UNC data camp\HomeWork\Psql\data\titles.csv' DELIMITER ',' CSV HEADER;
SELECT * FROM titles;

-- List the following details of each employee: employee number, last
-- name, first name, gender, and salary.

SELECT e.emp_no, e.last_name, e.first_name, e.gender, s.salary
FROM employees as e
INNER JOIN salaries as s ON
e.emp_no = s.emp_no;

-- List employees who were hired in 1986.
SELECT last_name, first_name, hire_date FROM employees
where date_part('year',hire_date) = '1986';

-- List the manager of each department with the following information:
-- department number, department name, the manager's employee number, last
-- name, first name, and start and end employment dates.
SELECT d.dept_no, dp.dept_name, d.emp_no, e.last_name, e.first_name, d.from_date, d.to_date
FROM dept_manager as d
INNER JOIN employees as e 
ON d.emp_no = e.emp_no 
JOIN departments as dp
ON d.dept_no = dp.dept_no;

-- List the department of each employee with the following information:
-- employee number, last name, first name, and department name.
SELECT d.dept_no, e.last_name, e.first_name, dp.dept_name
FROM dept_emp as d
INNER JOIN employees as e 
ON d.emp_no = e.emp_no 
JOIN departments as dp
ON d.dept_no = dp.dept_no;

-- List all employees whose first name is "Hercules" and last names begin
-- with "B."
SELECT * FROM employees
WHERE first_name = 'Hercules' AND SUBSTR(last_name, 1, 1) = 'B' ;

-- List all employees in the Sales department, including their employee
-- number, last name, first name, and department name.
SELECT d.dept_no, e.last_name, e.first_name, dp.dept_name
FROM dept_emp as d
INNER JOIN employees as e 
ON d.emp_no = e.emp_no 
JOIN departments as dp
ON d.dept_no = dp.dept_no 
WHERE dept_name = 'Sales';

-- List all employees in the Sales and Development departments, including
-- their employee number, last name, first name, and department name.
SELECT d.dept_no, e.last_name, e.first_name, dp.dept_name
FROM dept_emp as d
INNER JOIN employees as e 
ON d.emp_no = e.emp_no 
JOIN departments as dp
ON d.dept_no = dp.dept_no 
WHERE dept_name = 'Sales' OR dept_name = 'Development';

-- In descending order, list the frequency count of employee last names,
-- i.e., how many employees share each last name.
-- SELECT  last_name, COUNT(last_name) FROM employees ORDER BY 'last name count' DESC; 
SELECT last_name,  COUNT(last_name) AS "name CNT" FROM employees 
GROUP BY last_name
ORDER BY "name CNT" DESC;

-- AVG salaries by title
SELECT t.title, ROUND(AVG(s.salary),2) AS "AVG Salary"
FROM titles as t
INNER JOIN salaries as s 
ON t.emp_no = s.emp_no
GROUP BY t.title
