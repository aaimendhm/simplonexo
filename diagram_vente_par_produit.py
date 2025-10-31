import sqlite3

conn = sqlite3.connect('ventes.csv')
cur = conn.cursor()
cur.execute("SELECT c2; SUM (c3 * c4) AS ventes_parproduits; FROM ventes; GROUP BY c2")
conn.close()
