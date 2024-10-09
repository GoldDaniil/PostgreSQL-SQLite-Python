CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT,
    salary DECIMAL(10, 2)
);

WITH RECURSIVE employee_hierarchy AS (
    SELECT id, name, manager_id, salary, 1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.id, e.name, e.manager_id, e.salary, eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.id
),
subordinate_count AS (
    SELECT manager_id, COUNT(id) AS total_subordinates
    FROM employee_hierarchy
    GROUP BY manager_id
),
average_salary AS (
    SELECT manager_id, AVG(salary) OVER (PARTITION BY manager_id) AS avg_subordinate_salary
    FROM employee_hierarchy
)
SELECT 
    eh.id, 
    eh.name, 
    eh.manager_id, 
    sc.total_subordinates, 
    avg_s.avg_subordinate_salary
FROM employee_hierarchy eh
LEFT JOIN subordinate_count sc ON eh.id = sc.manager_id
LEFT JOIN average_salary avg_s ON eh.id = avg_s.manager_id
ORDER BY eh.level, eh.id;
