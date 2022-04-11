var express=require('express');
var bodyParser = require('body-parser');

var app=express();
// Convert ejs into html
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
 
const sqlite3 = require('sqlite3');
const { title } = require('process');
const db = new sqlite3.Database('model/database.db');

// Hash function
// Adapted from: https://werxltd.com/wp/2010/05/13/javascript-implementation-of-javas-string-hashcode-method/
String.prototype.hashCode = function() {
    var hash = 0, i, chr;
    if (this.length === 0) return hash;
    for (i = 0; i < this.length; i++) {
      chr   = this.charCodeAt(i);
      hash  = ((hash << 5) - hash) + chr;
      hash |= 0; // Convert to 32bit integer
    }
    return hash;
  };

app.get("/register", function (req, res) {
  res.render("register_bootstrap");
});

// Handling user signup
app.post("/register", function (req, res) {
    var username = req.body.username
    var password = req.body.password
    // console.log(username);
    // console.log(password);
    var unique_code = username.hashCode()
    // Remove information if user already exists
    db.run("DELETE FROM users WHERE username=?", username, (err) => {
      if (err) {
        console.log(err);
      }
      console.log("Repeated user detected");
      // if (data.length != 0) {
      //   res.render("register_duplicate", {users: data});
      // }
    });
    db.run("INSERT INTO users (username, password, unique_code) VALUES (?, ?, ?)", [username, password, unique_code], (err) => {
      if (err) {
        console.log(err);
      }
    });
    db.all("SELECT username, password, unique_code from users;", (err, rows) => {
      // console.log(rows);
    });
    res.redirect("/" + unique_code + '/profile');
          });

          
app.get("/:unique_code/profile", function (req, res) {
  var data = req.params.unique_code;
  console.log(data)
  res.render("user_profile", {unique_code: data});
});

app.post("/:unique_code/profile", function (req, res) {
  var data = req.params.unique_code;
  console.log("After post: " + data)
  res.redirect("/" + req.params.unique_code + "/create")
});

app.get("/:unique_code/create", function (req, res) {
  var data = req.params.unique_code;
  res.render("create", {unique_code: data});
});

app.post("/:unique_code/create", function (req, res) {
  var title = req.body.title
  var content = req.body.content
  var timestamp = Math.floor(Date.now() / 1000);
  var vote = 0
  var postid = timestamp.toString().hashCode()
  db.run("INSERT INTO blog (title, content, timestamp, vote_counter, postid) VALUES (?, ?, ?, ?, ?)", [title, content, timestamp, vote, postid], (err) => {
    if (err) {
      console.log(err);
    }
  });
  res.redirect('/' + req.params.unique_code + '/profile');
});

// Individual Posts
app.get("/posts/:postid", function (req, res) {
  var postid = req.params.postid
  db.all("SELECT title, content, timestamp, vote_counter, postid FROM blog WHERE postid=?;", postid, (err, rows) => {
    var title = rows[0].title;
    var content = rows[0].content;
    var vote = rows[0].vote_counter;
    console.log(typeof rows[0]);
    console.log(rows[0]);
  });
  res.render("show_blog", {title: title, content: content, vote: vote})
});


app.post("/posts/:postid", function (req, res) {
  res.render("/" + req.params.postid)
});

var server=app.listen(8080,function() {});
