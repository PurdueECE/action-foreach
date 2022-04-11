var express = require('express');
var bodyParser = require('body-parser');

var app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('model/database.db');
db.all("SELECT unique_code, username, password FROM users;", (error, rows) => {
	rows.forEach((row) => {
		console.log("username: " + row.username);
		console.log("password: " + row.password);
		datausername = row.username;
		datapassword = row.password;
	})
});

function hash(input) {
	var sum = 0
	for(var i = 0; i < input.length; i++) {
		sum += input.charCodeAt(i);
	}
	return (sum % 100); // limitation: only 100 unique codes can be distributed. I'm not super comfy with hashing so give me a break. 
}

//const db = new sqlite3.Database('model/database.db');
app.get('/register', function(req,res) {
	res.render("register_bootstrap");
});

app.post('/register', function(req,res) {
	var username = req.body.username
	var password = req.body.password
	console.log("registered username: " + username);
	console.log("registered password: " + password);
	var hashed_code = hash(username);
	db.run("INSERT INTO users (unique_code, username, password) VALUES (?, ?, ?)", [hashed_code, username, password], (err) => {
		if (err) {
			console.log(err);
		}
	})
	res.redirect("/" + hashed_code.toString() + "/profile");
});

app.get('/:hashed_code/profile', function(req,res) {
	var hashed_code = req.params.hashed_code;
	db.all("SELECT title,content,timestamp,vote FROM posts WHERE user_id = (?)", [hashed_code], (err, rows) => {
		console.log(rows);
		data = rows;
		res.render("profile", { users: data, code: hashed_code});//, { code: hashed_code });
	})
});

app.get('/:hashed_code/create', function(req,res) {
	var hashed_code = req.params.hashed_code;
	res.render("create", {code: hashed_code});
});

app.post('/:hashed_code/create', function(req,res) {
	var title = req.body.title
	var content = req.body.content
	var hashed_code = req.params.hashed_code;
	var timestamp = Date.now();
	console.log(Date.now());
	var votes = 0;
	var post_hashed_code = hash(title);
	db.run("INSERT INTO posts (unique_code, title, content, timestamp, vote, user_id) VALUES (?, ?, ?, ?, ?, ?)", [post_hashed_code, title, content, timestamp, votes, hashed_code], (err) => {
		if (err) {
			console.log(err);
		}
	})
	console.log("hashed code:");
	console.log(hashed_code.toString());
	
	res.redirect("/" + hashed_code.toString() + "/profile");

});

app.get('/posts/:postid', function(req,res) {
	var postid = req.params.postid;
	db.all("SELECT title,content,timestamp,vote FROM posts WHERE unique_code = (?)", [postid], (err, rows) => {
		console.log(rows);
		data = rows;
		res.render("post", { posts : data });
	})
});

var server=app.listen(5322,function() {});
