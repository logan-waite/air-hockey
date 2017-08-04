import sqlite3

try:
    conn = sqlite3.connect("/var/www/airhockey/airhockey.sqlite")
    conn.text_factory = str
    cur = conn.cursor()
except:
    print("Was unable to create the database")

try:
    cur.execute(""" CREATE TABLE "Matches" (
                    `match_id` INTEGER PRIMARY KEY AUTOINCREMENT,
                    `p1_id` INTEGER NOT NULL,
                    `p2_id` INTEGER NOT NULL,
                    `p1_score` INTEGER NOT NULL,
                    `p2_score` INTEGER NOT NULL,
                    `p1_weight` INTEGER,
                    `p2_weight` INTEGER,
                    FOREIGN KEY(`p1_id`) REFERENCES `Player`(`player_id`),
                    FOREIGN KEY(`p2_id`) REFERENCES `Player`(`player_id`)
                    ) """)
    cur.execute(""" CREATE TABLE "Players" (
                    `player_Id` INTEGER PRIMARY KEY AUTOINCREMENT,
                    `name` TEXT NOT NULL UNIQUE,
                    `wins` INTEGER DEFAULT 0,
                    `weight` INTEGER DEFAULT 0
                    ) """)
except:
    print("Was unable to create the tables")

print("Success!")
conn.commit()
conn.close()
