#include <iostream>
#include <libpq-fe.h>

using namespace std;

// функция для подключения к базе данных PostgreSQL
PGconn* connectToDB() {
    PGconn* conn = PQconnectdb("user=your_username dbname=your_dbname password=your_password hostaddr=127.0.0.1 port=5432");
    
    if (PQstatus(conn) != CONNECTION_OK) {
        cerr << "connection to database failed: " << PQerrorMessage(conn) << endl;
        PQfinish(conn);
        exit(1);
    }

    cout << "connected to database successfully!" << endl;
    return conn;
}

// функция для создания таблиц в базе данных
void createTables(PGconn* conn) {
    const char* query = R"(
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS tasks (
            task_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            status VARCHAR(50) NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            due_date DATE,
            user_id INTEGER REFERENCES users(user_id)
        );
    )";
    
    PGresult* res = PQexec(conn, query);
    
    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
        cerr << "error creating tables: " << PQerrorMessage(conn) << endl;
        PQclear(res);
        PQfinish(conn);
        exit(1);
    }
    
    PQclear(res);
    cout << "tables created successfully!" << endl;
}

// функция для добавления пользователя
void addUser(PGconn* conn, const string& username, const string& email) {
    const char* query = "INSERT INTO users (username, email) VALUES ($1, $2)";
    
    const char* values[2] = {username.c_str(), email.c_str()};
    int lengths[2] = {(int)username.length(), (int)email.length()};
    int formats[2] = {0, 0};  // используем текстовые параметры

    PGresult* res = PQexecParams(conn, query, 2, nullptr, values, lengths, formats, 0);

    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
        cerr << "error adding user: " << PQerrorMessage(conn) << endl;
        PQclear(res);
        PQfinish(conn);
        exit(1);
    }
    
    PQclear(res);
    cout << "user added successfully!" << endl;
}

//функция для добавления задачи
void addTask(PGconn* conn, const string& title, const string& description, const string& due_date, int user_id) {
    const char* query = "INSERT INTO tasks (title, description, due_date, user_id) VALUES ($1, $2, $3, $4)";

    const char* values[4] = {title.c_str(), description.c_str(), due_date.c_str(), to_string(user_id).c_str()};
    int lengths[4] = {(int)title.length(), (int)description.length(), (int)due_date.length(), (int)to_string(user_id).length()};
    int formats[4] = {0, 0, 0, 0};  //используем текстовые параметры

    PGresult* res = PQexecParams(conn, query, 4, nullptr, values, lengths, formats, 0);

    if (PQresultStatus(res) != PGRES_COMMAND_OK) {
        cerr << "Error adding task: " << PQerrorMessage(conn) << endl;
        PQclear(res);
        PQfinish(conn);
        exit(1);
    }
    
    PQclear(res);
    cout << "task added successfully!" << endl;
}

void listTasks(PGconn* conn) {
    const char* query = "sELECT task_id, title, description, status, due_date, user_id FROM tasks";

    PGresult* res = PQexec(conn, query);

    if (PQresultStatus(res) != PGRES_TUPLES_OK) {
        cerr << "error fetching tasks: " << PQerrorMessage(conn) << endl;
        PQclear(res);
        PQfinish(conn);
        exit(1);
    }

    int rows = PQntuples(res);
    cout << "tasks: " << endl;

    for (int i = 0; i < rows; ++i) {
        cout << "task ID: " << PQgetvalue(res, i, 0) << endl;
        cout << "title: " << PQgetvalue(res, i, 1) << endl;
        cout << "description: " << PQgetvalue(res, i, 2) << endl;
        cout << "status: " << PQgetvalue(res, i, 3) << endl;
        cout << "due Date: " << PQgetvalue(res, i, 4) << endl;
        cout << "assigned to User ID: " << PQgetvalue(res, i, 5) << endl;
        cout << "--------------------------------" << endl;
    }

    PQclear(res);
}

int main() {
    PGconn* conn = connectToDB();

    createTables(conn);

    // добавляем пользователей
    addUser(conn, "John Doe", "john.doe@example.com");
    addUser(conn, "Jane Smith", "jane.smith@example.com");

    // добавляем задачи
    addTask(conn, "complete Project", "ginish the main part of the project", "2024-12-01", 1);
    addTask(conn, "review Code", "go through the code for the review", "2024-10-15", 2);

    listTasks(conn);

    PQfinish(conn);
    return 0;
}
