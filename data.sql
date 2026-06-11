CREATE TABLE Employees (
    EmpID INT,
    Name VARCHAR(30),
    Department VARCHAR(50),
    Salary INT
);

INSERT INTO Employees (EmpID, Name, Department, Salary)
VALUES 
(1, 'Rahul', 'CSE', 45000),
(2, 'ram', 'AI', 70000),
(3, 'ramu', 'ML', 60000);

SELECT 
    department,
    COUNT(*) AS Total_employees,
    SUM(salary) AS total_payroll,
    AVG(salary) AS Average_salary
FROM employees 
GROUP BY department;

SELECT 
    department,
    AVG(salary) AS average_salary
FROM employees 
GROUP BY department 
HAVING AVG(salary) > 55000;

