import sqlite3

conn = sqlite3.connect('noticias.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO games (nome,arquivo,width,height) VALUES (?,?)    
               """,(""))

conn.commit()
conn.close()
