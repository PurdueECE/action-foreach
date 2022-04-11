-- SQLite
CREATE TABLE posts(title TEXT,content TEXT,CURRENT_TIME,vote_counter INTEGER,username TEXT);

CREATE TABLE users (
id TEXT PRIMARY KEY,
username TEXT,
password TEXT,
unique (username)
);