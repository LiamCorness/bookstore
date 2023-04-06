import sqlite3

# Create databse call ebookstore
db = sqlite3.connect("ebookstore.db")

# Assign cursore
cursor = db.cursor()

# Create table called books
cursor.execute('''
CREATE TABLE books(
id int PRIMARY KEY NOT NULL,
title text,
author text,
qty int
)
''')

# Create list to add to table
book_list = [
    (3001, 'Harry Potter And The Philosopehers Stone', 'JK Rowling', 40),
    (3002, 'The Lion The Witch And The Wardrobe', 'CS Lewis', 25),
    (3003, 'The Lord Of The Rings', 'JRR Tolkein', 25),
    (3004, 'Alice in Wonderland', 'Lewis Carrol', 12),
    (3005, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3006, 'Animal Farm', 'George Orwell', 45),
    (3007, 'The Handmaids Tale', 'Maragaret Attwood', 20),
    (3008, 'We', 'Yevgeny Zamyatin', 10),
    (3009, 'The Mandibles', 'Lionel Shriver', 15),
    (3010, 'War and Peace', 'Leo Tolstoy', 30)
]

# Add the list
cursor.executemany('INSERT INTO books VALUES (?,?,?,?)', book_list)

# Commit changes
db.commit()

