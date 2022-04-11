-- SQLite
CREATE TABLE posts (title TEXT, 
content TEXT, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
vote_counter INTEGER);

CREATE TABLE users (
id TEXT PRIMARY KEY,
username TEXT,
password TEXT,
unique (username)
);