import sqlite3

conn = sqlite3.connect("chat_app.db")
cur = conn.cursor()

"""Task 1: Nájsť používateľov, ktorí poslali správy do konkrétnej miestnosti (napr. room1)."""
print("Task 1:")
cur.execute("""
SELECT DISTINCT users.username
FROM users
JOIN messages ON users.id = messages.user_id
JOIN rooms ON messages.room_id = rooms.id
WHERE rooms.name = 'room1';
""")

"""Task 2: Počítať, koľko rôznych používateľov poslalo správy do jednotlivých miestností."""
print("Task 2:")
cur.execute("""
SELECT rooms.name, COUNT(DISTINCT messages.user_id)
FROM messages
JOIN rooms ON messages.room_id = rooms.id
GROUP BY rooms.name;
""")

"""Task 3: Nájsť miestnosti, do ktorých konkrétny používateľ (napr. user2) poslal správy."""


"""Task 4: Zobraziť počet správ, ktoré poslal každý používateľ."""

"""Task 5: Zobraziť zoznam miestností spolu s počtom správ, ktoré poslali jednotliví používatelia."""

data = cur.fetchall()
print(data)
print("DONE")