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
WHERE rooms.name = "room1";
""")
# OUTPUT: [('user1',), ('user2',)]

"""Task 2: Počítať, koľko rôznych používateľov poslalo správy do jednotlivých miestností."""
print("Task 2:")
cur.execute("""
SELECT rooms.name, COUNT(DISTINCT messages.user_id)
FROM messages
JOIN rooms ON messages.room_id = rooms.id
GROUP BY rooms.name;
""")
# OUTPUT: [('room1', 2), ('room2', 3), ('room3', 1)]

"""Task 3: Nájsť miestnosti, do ktorých konkrétny používateľ (napr. user2) poslal správy."""
print("Task 3:")
cur.execute("""
SELECT DISTINCT rooms.name
FROM rooms
JOIN messages ON rooms.id = messages.room_id
JOIN users ON messages.user_id = users.id
WHERE users.username = "user2";
""")
# OUTPUT: [('room1',), ('room2',)]

"""Task 4: Zobraziť počet správ, ktoré poslal každý používateľ."""
print("Task 4:")
cur.execute("""
SELECT users.username, COUNT(messages.id)
FROM users
JOIN messages ON users.id = messages.user_id
GROUP BY users.username
""")
# OUTPUT: [('user1', 3), ('user2', 2), ('user3', 2)]

"""Task 5: Zobraziť zoznam miestností spolu s počtom správ, ktoré poslali jednotliví používatelia."""
print("Task 5:")
cur.execute("""
SELECT rooms.name, COUNT(messages.id)
FROM rooms
JOIN messages ON rooms.id = messages.room_id
GROUP BY rooms.name
""")
# OUTPUT: [('room1', 3), ('room2', 3), ('room3', 1)]

data = cur.fetchall()
print(data)
print("DONE")