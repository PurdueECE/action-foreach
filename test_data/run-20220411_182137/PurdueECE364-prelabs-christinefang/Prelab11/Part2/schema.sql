CREATE TABLE users (
    first_name text,
    last_name text,
    id integer primary key
);

CREATE TABLE posts (
    id integer primary key,
    title text,
    body text
);

INSERT into users VALUES ("christine" , "fang", 666);
INSERT into users VALUES ("emily", "lo", 555);
INSERT into users VALUES ("cameron" , "ha" , 111);
INSERT into users VALUES ("rickie", "fang", 222);
INSERT into users VALUES ("michelle", "huanggg" ,444);

INSERT into posts VALUES (666,"hello", "today is a good day");
INSERT into posts VALUES (555,"youtube","check out this new video");
INSERT into posts VALUES (111,"apo", "one more service hour");
INSERT into posts VALUES (222,"basketball", "dallas mavs is my favorite");
INSERT into posts VALUES (444,"thesis", "san bernardino lets goo");

CREATE TRIGGER aft_del AFTER DELETE ON users
BEGIN
    DELETE FROM posts WHERE id = OLD.id;
    
END;
