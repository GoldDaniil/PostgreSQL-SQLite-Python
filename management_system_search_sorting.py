import sqlite3
from datetime import datetime
import difflib

#функция для создания базы данных и таблиц
def create_tables():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_date TEXT,
            added_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowers (
            borrower_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            book_id INTEGER,
            borrow_date TEXT DEFAULT CURRENT_TIMESTAMP,
            return_date TEXT,
            FOREIGN KEY (book_id) REFERENCES books(book_id)
        )
    ''')

    conn.commit()
    conn.close()

#функция для добавления новой книги в базу данных
def add_book(title, author, published_date):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO books (title, author, published_date) 
        VALUES (?, ?, ?)
    ''', (title, author, published_date))

    conn.commit()
    conn.close()
    print(f"Book '{title}' by {author} added successfully!")

#алгоритм Левенштейна для поиска похожих книг по названию
def find_similar_books(search_title, threshold=0.7):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title FROM books')
    all_titles = [row[0] for row in cursor.fetchall()]

    similar_titles = []
    for title in all_titles:
        similarity = difflib.SequenceMatcher(None, search_title.lower(), title.lower()).ratio()
        if similarity >= threshold:
            similar_titles.append((title, similarity))

    conn.close()

    #сортировка по наибольшей схожести
    similar_titles.sort(key=lambda x: x[1], reverse=True)

    return similar_titles

#функция для выдачи книги пользователю
def borrow_book(borrower_name, book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO borrowers (name, book_id) 
        VALUES (?, ?)
    ''', (borrower_name, book_id))

    conn.commit()
    conn.close()
    print(f"Borrower '{borrower_name}' borrowed book with ID {book_id}")

#функция для возврата книги
def return_book(borrower_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE borrowers 
        SET return_date = ? 
        WHERE borrower_id = ? AND return_date IS NULL
    ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), borrower_id))

    conn.commit()
    conn.close()
    print(f"Borrower with ID {borrower_id} returned their book.")

#функция для поиска книг по автору
def find_books_by_author(author):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT book_id, title, published_date FROM books WHERE author = ?
    ''', (author,))

    books = cursor.fetchall()
    conn.close()

    return books

#функция для получения всех книг
def get_all_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()

    return books

#сложный алгоритм сортировки книг по дате публикации
def sort_books_by_date():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT book_id, title, author, published_date 
        FROM books 
        WHERE published_date IS NOT NULL
    ''')

    books = cursor.fetchall()
    conn.close()

    #сортируем книги по дате публикации
    books_sorted = sorted(books, key=lambda x: datetime.strptime(x[3], '%Y-%m-%d'))

    return books_sorted

#тестирование программы
if __name__ == "__main__":
    #создаем таблицы
    create_tables()

    add_book("dkgsdg", "dsadas", "1951-07-16")
    add_book("fgdfdg", "alskdas", "1960-07-11")
    add_book("1984", "dsfsdf", "1949-06-08")

    borrow_book("asdasd", 1)

    return_book(1)

    books_by_orwell = find_books_by_author("fddf")
    print("books by:", books_by_orwell)

    similar_books = find_similar_books("asd")
    print("similar books to 'asd':", similar_books)

    sorted_books = sort_books_by_date()
    print("books sorted by date:", sorted_books)
