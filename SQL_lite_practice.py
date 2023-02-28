import sqlite3

conn  = sqlite3.connect('data.db')

c = conn.cursor()

#c.execute("""CREATE TABLE students (
#    first text,
#    last text,
#    id integer
#    ) """)

#c.execute("INSERT INTO students VALUES ('Mike', 'Terekhov', 12345)")

c.execute("SELECT * FROM students WHERE first = 'Mike'")
print(c.fetchall())

conn.commit()