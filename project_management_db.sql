CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(200) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_id INT REFERENCES users(user_id)
);

CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    task_name VARCHAR(200) NOT NULL,
    description TEXT,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'in progress', 'completed')),
    due_date DATE,
    project_id INT REFERENCES projects(project_id),
    assigned_to INT REFERENCES users(user_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--таблица для аудита изменений задач
CREATE TABLE task_audit (
    audit_id SERIAL PRIMARY KEY,
    task_id INT REFERENCES tasks(task_id),
    changed_by INT REFERENCES users(user_id),
    old_status VARCHAR(20),
    new_status VARCHAR(20),
    change_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--таблица комментариев к задачам
CREATE TABLE task_comments (
    comment_id SERIAL PRIMARY KEY,
    task_id INT REFERENCES tasks(task_id),
    user_id INT REFERENCES users(user_id),
    comment TEXT,
    commented_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION audit_task_status_change() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.status <> OLD.status THEN
        INSERT INTO task_audit(task_id, changed_by, old_status, new_status)
        VALUES (OLD.task_id, NEW.assigned_to, OLD.status, NEW.status);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

--триггер для вызова функции аудита при обновлении задачи
CREATE TRIGGER trg_task_status_change
AFTER UPDATE ON tasks
FOR EACH ROW
EXECUTE FUNCTION audit_task_status_change();

CREATE VIEW project_tasks_view AS
SELECT 
    p.project_id, 
    p.project_name, 
    p.description AS project_description, 
    t.task_id, 
    t.task_name, 
    t.status, 
    t.due_date, 
    u.username AS assigned_to
FROM 
    projects p
JOIN 
    tasks t ON p.project_id = t.project_id
LEFT JOIN 
    users u ON t.assigned_to = u.user_id;

--функция для автоматической проверки просроченных задач и их обновления
CREATE OR REPLACE FUNCTION update_overdue_tasks() RETURNS VOID AS $$
BEGIN
    UPDATE tasks
    SET status = 'pending'
    WHERE due_date < CURRENT_DATE AND status <> 'completed';
END;
$$ LANGUAGE plpgsql;

--планировщик для автоматического запуска проверки просроченных задач каждый день
CREATE EXTENSION IF NOT EXISTS pg_cron;

SELECT cron.schedule('0 0 * * *', $$SELECT update_overdue_tasks();$$);

--количество задач в каждом статусе по каждому проекту
SELECT 
    p.project_name,
    COUNT(CASE WHEN t.status = 'pending' THEN 1 END) AS pending_tasks,
    COUNT(CASE WHEN t.status = 'in progress' THEN 1 END) AS in_progress_tasks,
    COUNT(CASE WHEN t.status = 'completed' THEN 1 END) AS completed_tasks
FROM 
    projects p
LEFT JOIN 
    tasks t ON p.project_id = t.project_id
GROUP BY 
    p.project_name;

--запрос для получения списка пользователей с количеством назначенных задач
SELECT 
    u.username, 
    COUNT(t.task_id) AS assigned_tasks
FROM 
    users u
LEFT JOIN 
    tasks t ON u.user_id = t.assigned_to
GROUP BY 
    u.username;

-- пример вставки данных
INSERT INTO users (username, email) VALUES ('abccc', 'abc@example.com');
INSERT INTO users (username, email) VALUES ('edfff', 'edf@example.com');

INSERT INTO projects (project_name, description, owner_id) VALUES ('project Alpha', 'first project description', 1);
INSERT INTO projects (project_name, description, owner_id) VALUES ('project Beta', 'second project description', 2);

INSERT INTO tasks (task_name, description, status, due_date, project_id, assigned_to) 
VALUES ('task 1', 'description for task 1', 'pending', '2024-10-15', 1, 1);
INSERT INTO tasks (task_name, description, status, due_date, project_id, assigned_to) 
VALUES ('task 2', 'description for task 2', 'in progress', '2024-11-01', 1, 2);

UPDATE tasks SET status = 'completed' WHERE task_id = 1;

--получение всех комментариев к задаче
SELECT 
    tc.comment, 
    u.username, 
    tc.commented_at 
FROM 
    task_comments tc
JOIN 
    users u ON tc.user_id = u.user_id
WHERE 
    tc.task_id = 1;

--получение всех изменений статуса для задачи
SELECT 
    ta.old_status, 
    ta.new_status, 
    u.username AS changed_by, 
    ta.change_time 
FROM 
    task_audit ta
JOIN 
    users u ON ta.changed_by = u.user_id
WHERE 
    ta.task_id = 1;
