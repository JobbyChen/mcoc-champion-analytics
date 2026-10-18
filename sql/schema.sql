CREATE TABLE IF NOT EXISTS champions (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL UNIQUE,
 class TEXT NOT NULL,
 immunities TEXT,
 offense REAL,
 survivability REAL,
 utility REAL,
 source TEXT NOT NULL
);
