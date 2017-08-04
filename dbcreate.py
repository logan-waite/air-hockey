import sqlite3

try:
    print("Creating airhockey.sqlite...")
    conn = sqlite3.connect("/var/www/airhockey/airhockey.sqlite")
    conn.text_factory = str
    cur = conn.cursor()
    print("Database created!")
except:
    print("Was unable to create the database")

try:
    print("Creating Matches and Players tables...")
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
    print("Tables created!")
except:
    print("Was unable to create the tables")

conn.commit()
conn.close()
