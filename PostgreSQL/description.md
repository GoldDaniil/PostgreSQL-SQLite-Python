brew install postgresql

brew services start postgresql

psql postgres

CREATE DATABASE my_database;

я выбрал PostgreSQL  - и написал это: gold@MacBook-Pro-Gold ~ % psql postgres
psql (14.13 (Homebrew))
Type "help" for help.
postgres=# CREATE DATABASE my_database;
CREATE DATABASE
postgres=#   что делать дальше?

\c my_database

CREATE TABLE Students (
  student_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  birthdate DATE,
  course_id INT
);

CREATE TABLE Courses (
  course_id SERIAL PRIMARY KEY,
  course_name VARCHAR(100)
);

CREATE TABLE Instructors (
  instructor_id SERIAL PRIMARY KEY,
  instructor_name VARCHAR(100),
  course_id INT REFERENCES Courses(course_id)
);

INSERT INTO Courses (course_name)
VALUES 
('Mathematics'),
('Physics'),
('Computer Science');

INSERT INTO Students (first_name, last_name, birthdate, course_id)
VALUES 
('John', 'Doe', '2000-05-21', 1),
('Jane', 'Smith', '1999-03-15', 2),
('Mike', 'Brown', '2001-07-09', 3);

INSERT INTO Instructors (instructor_name, course_id)
VALUES 
('Dr. John Williams', 1),
('Dr. Lisa Thompson', 2),
('Dr. Emily Davis', 3);

SELECT s.first_name, s.last_name, c.course_name
FROM Students s
JOIN Courses c ON s.course_id = c.course_id;

SELECT c.course_name, i.instructor_name
FROM Courses c
JOIN Instructors i ON c.course_id = i.course_id;

SELECT s.first_name, s.last_name
FROM Students s
JOIN Courses c ON s.course_id = c.course_id
WHERE c.course_name = 'Computer Science';


<img width="773" alt="Screenshot 2024-10-05 at 23 06 08" src="https://github.com/user-attachments/assets/eea49f0f-79c4-4b52-b6ef-5ce2af9129c6">






------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------



1. PostgreSQL
Для PostgreSQL вам нужно установить саму СУБД и выбрать среду для написания SQL-запросов:

Установка PostgreSQL:

Откройте терминал и введите следующую команду для установки PostgreSQL через Homebrew (если Homebrew не установлен, его нужно установить здесь):
brew install postgresql

После установки запустите PostgreSQL:
brew services start postgresql

Теперь вы можете подключиться к базе данных через psql (интерфейс командной строки для работы с PostgreSQL):
psql postgres

В psql вы сможете писать SQL-код напрямую:
CREATE DATABASE my_database;

Использование pgAdmin (графический интерфейс для работы с PostgreSQL):
Загрузите и установите pgAdmin для macOS.
Подключитесь к локальной базе данных PostgreSQL, запущенной через Homebrew, используя pgAdmin.
В pgAdmin можно создавать базы данных, таблицы и писать SQL-запросы через удобный интерфейс.

2. SQLite3
SQLite3 является более простым вариантом, так как не требует установки серверной части. Вы можете работать с файлами баз данных прямо на вашем MacBook.

Установка SQLite3:

SQLite уже предустановлен на macOS. Чтобы проверить, установлена ли она, введите в терминале:
sqlite3 --version

Чтобы начать работу с базой данных SQLite, выполните команду:
sqlite3 my_database.db

Откроется интерфейс командной строки для работы с базой данных, где можно писать SQL-запросы:
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    birthdate TEXT,
    course_id INTEGER
);

Использование SQLiteStudio (графический интерфейс для SQLite):

Загрузите и установите SQLiteStudio.
Откройте SQLiteStudio и создайте новый файл базы данных.
В SQLiteStudio можно создавать таблицы и писать SQL-запросы в графическом интерфейсе.
3. PyCharm (или любой текстовый редактор)
Если вы используете PyCharm или любой другой текстовый редактор, вы можете писать SQL-запросы в отдельном файле, а затем запускать их через SQLite или PostgreSQL.

Для SQLite:

Создайте файл с расширением .sql и напишите SQL-код.
Запустите файл через SQLite в терминале:
sqlite3 my_database.db < файл.sql

Для PostgreSQL:

То же самое, но для выполнения файла используйте psql:
psql -d my_database -f файл.sql

Резюме:
PostgreSQL: Используйте pgAdmin или команду psql в терминале.
SQLite3: Используйте встроенный sqlite3 в терминале или SQLiteStudio.
Вы можете писать SQL-код в любом текстовом редакторе и запускать его через командную строку.
