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
