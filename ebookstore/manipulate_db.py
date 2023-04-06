import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to add book to the databse
def add_book():
    # Create a window that displays options and takes input
    win = tk.Toplevel(root)
    win.title("Add a Book")
    
    id_label = tk.Label(win, text="Enter book ID")
    id_label.pack()
    id_entry = tk.Entry(win)
    id_entry.pack()
    
    title_label = tk.Label(win, text="Enter book title")
    title_label.pack()
    title_entry = tk.Entry(win)
    title_entry.pack()
    
    author_label = tk.Label(win, text="Enter author name")
    author_label.pack()
    author_entry = tk.Entry(win)
    author_entry.pack()
    
    qty_label = tk.Label(win, text="Enter Quantity")
    qty_label.pack()
    qty_entry = tk.Entry(win)
    qty_entry.pack()

    # Function to tell programm what to do when submit button is clicked
    def submit_book():
        id = id_entry.get()
        title = title_entry.get().title()
        author = author_entry.get().title()
        qty = qty_entry.get()
        
        # Ensuring 'id' and 'qty' are numbers
        if not id.isdigit():
            messagebox.showerror ("Error","id must be a number")
            return
        if not qty.isdigit():
            messagebox.showerror ("Error", "id must be a number")
            return
        try:
            db = sqlite3.connect("ebookstore.db")
            cursor = db.cursor()
            cursor.execute("SELECT * FROM books WHERE id=?",(id,))
            book = cursor.fetchone()
            if book:
                # If book already exists in the db, update it.
                new_qty = int(qty) + int(book[3])
                cursor.execute("UPDATE books SET qty=? WHERE id=?",(new_qty, id))
                db.commit()
                messagebox.showinfo("Success", "Book updated successfully.")
            else:
                # If book does not exist add a new record
                cursor.executemany("INSERT INTO books (id, title, author, qty) VALUES (?,?,?,?)",[(id, title, author, qty)])
                db.commit()
                messagebox.showinfo("Success", "Book added successfully")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            db.close()
            win.destroy()

    submit_button = tk.Button(win, text="Submit", command=submit_book)
    submit_button.pack()

def update_book():
    # Code to open a window
    win = tk.Toplevel(root)
    win.title("Update Book")
    
    # Code to add entry fields in the new window
    id_label = tk.Label(win, text="Enter ID of the Book")
    id_label.pack()
    id_entry = tk.Entry(win)
    id_entry.pack()
    
    title_label = tk.Label(win, text="Enter new Title")
    title_label.pack()
    title_entry = tk.Entry(win)
    title_entry.pack()
    
    author_label = tk.Label(win, text="Enter new Author")
    author_label.pack()
    author_entry = tk.Entry(win)
    author_entry.pack()
    
    qty_label = tk.Label(win, text="Enter new Quantity")
    qty_label.pack()
    qty_entry = tk.Entry(win)
    qty_entry.pack()
    
    # Code to submit values to the database and update selection
    def submit_update():
        id = int(id_entry.get())
        title = title_entry.get()
        author = author_entry.get()
        qty = int(qty_entry.get())
        
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()
        cursor.execute(f"UPDATE books SET title = '{title}', author = '{author}', qty = {qty} WHERE id = {id}")
        db.commit()
        db.close()
        win.destroy()
        
    # Code to add a submit button
    submit_button = tk.Button(win, text="Submit", command=submit_update)
    submit_button.pack()

# Function to delete book
def delete_book():
    win = tk.Toplevel(root)
    win.title("Delete a Book")

    id_label = tk.Label(win, text="Enter ID of book to delete")
    id_label.pack()
    id_entry = tk.Entry(win)
    id_entry.pack()

    
    def submit_delete():
        id = int(id_entry.get())
        db = sqlite3.connect("ebookstore.db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM books WHERE id=?", [(id)])
        db.commit()
        db.close()
        win.destroy()
    
    submit_button = tk.Button(win, text="Submit", command=submit_delete)
    submit_button.pack()

# Function to search for and display a book
def search_book():

    win = tk.Toplevel(root)
    win.title("Search for a Book")

    title_label = tk.Label(win, text="Enter book title".lower())
    title_label.pack()
    title_entry = tk.Entry(win)
    title_entry.pack()

    search_button = tk.Button(win, text="Search", command=lambda: display_book(title_entry.get(), win))
    search_button.pack()

def display_book(title, win):

    db = sqlite3.connect("ebookstore.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ? COLLATE NOCASE", (title,))
    book = cursor.fetchone()
    if book:
        id_label = tk.Label(win, text="ID: " + str(book[0]))
        id_label.pack()
        title_label = tk.Label(win, text="Title: " + str(book[1]))
        title_label.pack()
        author_label = tk.Label(win, text="Author: " + str(book[2]))
        author_label.pack()
        qty_label = tk.Label(win, text="Quantity: " + str(book[3]))
        qty_label.pack()
    else:
        not_found_label = tk.Label(win, text="Book not found")
        not_found_label.pack()
    db.close()


    search_button.pack()

# Functio to view the full table
def display_table():
    win = tk.Toplevel(root)
    win.title("Display Books")

    id_label = tk.Label(win, text="ID")
    id_label.grid(row=0, column=0)
    title_label = tk.Label(win, text="Title")
    title_label.grid(row=0, column=1)
    author_label = tk.Label(win, text="Author")
    author_label.grid(row=0, column=2)
    qty_label = tk.Label(win, text="Quantity")
    qty_label.grid(row=0, column=3)

    db = sqlite3.connect("ebookstore.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    db.close()

    for i, book in enumerate(books):
        id, title, author, qty = book
        id_label = tk.Label(win, text=id)
        id_label.grid(row=i+1, column=0)
        title_label = tk.Label(win, text=title)
        title_label.grid(row=i+1, column=1)
        author_label = tk.Label(win, text=author)
        author_label.grid(row=i+1, column=2)
        qty_label = tk.Label(win, text=qty)
        qty_label.grid(row=i+1, column=3)

# A tkinter window to display options to interact with the database
root = tk.Tk()
root.title("Book Database")

add_button = tk.Button(text="Add Book", command=add_book)
add_button.pack()

update_button = tk.Button(text="Update Book", command=update_book)
update_button.pack()

delete_button = tk.Button(text="Delete Book", command=delete_book)
delete_button.pack()

search_button = tk.Button(text="Search Book", command=search_book)
search_button.pack()

display_button = tk.Button(text="View All", command=display_table)
display_button.pack()

exit_button = tk.Button(text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()
