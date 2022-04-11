var express=require('express');
var bodyParser = require('body-parser');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
 
const sqlite3 = require('sqlite3');
const {v4:uuidv4} = require('uuid')

const db = new sqlite3.Database('model/database.db');

app.get("/", (req, res) => {
  res.redirect('/register')
})

app.get("/register", function (req, res) {
  res.render("register_bootstrap");
});

// Handling user signup
app.post("/register", function (req, res) {
  var username = req.body.username
  var password = req.body.password
  console.log(username);
  console.log(password);
  var uniqueID = uuidv4();
  db.run("INSERT INTO users (uniqueID, username, password) VALUES (?, ?, ?)", [uniqueID, username, password], (err) => {
    if (err) {
      console.log(err);
    }
  })

  res.redirect("/" + uniqueID + "/profile");
});

app.get("/{uniqueID}/profile", function (req, res) {
  db.run("SELECT * FROM posts WHERE uniqueID=?", uniqueID, (err, result) => {
    if (err) {
      console.log(err);
    }
    posts = result
    return res.render("index", { posts: result })
  })
});

var server=app.listen(3000, function(err) {
  if (err) console.log("Error in server setup")
  console.log("Server listening on Port", 3000);
});