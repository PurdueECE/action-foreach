CREATE Table students(
	name text,
	curr_id int,
	dob int
);

CREATE table classes(
	class_branch text,
	class_code int
);

INSERT into students VALUES ("Jason" , 11241, 1999);
INSERT into students VALUES ("Mary", 2234235, 2000);
INSERT into students VALUES ("Smith" , 1343241 , 2002);
INSERT into students VALUES ("Roger", 543533, 1995);
INSERT into students VALUES ("Steve", 12321132 ,1998 );

INSERT into classes VALUES ("ECE", 30100);
INSERT into classes VALUES ("ECE", 39595);
INSERT into classes VALUES ("ECE", 46100);
INSERT into classes VALUES ("ECE", 46900);
INSERT into classes VALUES ("ECE", 49595);