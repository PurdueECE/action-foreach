var express=require('express');
var bodyParser = require('body-parser');
//var hash=require('hash');
const crypto = require('crypto');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
 
const sqlite3 = require('sqlite3');
const { listen } = require('express/lib/application');

const db = new sqlite3.Database('model/login.db');

app.get("/register", function (req, res) {
  res.render("register");
});

// Handling user signup
app.post("/register", function (req, res) {
  var username = req.body.username
  var password = req.body.password
  var id = crypto.randomUUID();
  console.log(username);
  console.log(password);
  console.log(id);
  db.get("SELECT id FROM login_info WHERE username=? AND password=?",[username,password], (err, row)=>{
    if (err){
      return console.error(err.message)
    }
    else{
      if (row == null){
        db.run("INSERT INTO login_info (username, password, id) VALUES (?, ?, ?)", [username, password, id], (err) => {

          if (err) {

            console.log(err);
          }

        });
        res.render("profile", {name: username});
      }
      else{
          res.render("profile", {name: username});
      }
    }  
  });
});


app.get("/profile/:name", function(req, res){
  data = db.get("SELECT * from posts where id = ?", [req.params.name], (err) => {
    if(err){
      console.log(err);
    }
  })
  console.log(req.params.id)
  console.log(data)
  res.render('profile', {name: req.params.name});
});

app.post("/:name/create", function(req, res){
  var id = crypto.randomUUID();
  res.render("create", {id: id})
});

app.post("/:id/posts", function(req, res){
  var Title = req.body.title;
  var Content = req.body.content;
  var TimeStamp = req.body.time;
  var VoteCounter = 0;
  var id = crypto.randomUUID();
  db.run("INSERT INTO posts (Title, Content, TimeStamp, VoteCounter) VALUES (?, ?, ?, ?)", 
  [Title, Content, TimeStamp, VoteCounter], (err) => {
    if(err){
      console.log(err);
    }
  });
  return res.render("post", {Content: Content, Title: Title, Score: VoteCounter, Name: req.params.name});
});

app.post("/profile/:name", function(req, res) {
  allposts = db.get("SELECT * from posts ORDER BY title DESC LIMIT 1")
  console.log(allposts)
  res.render("post", {Content: Content, Title: Title, Score: VoteCounter, Name: req.params.name});
  //res.redirect("/profile/:name");
});

var server = app.listen(5022,function() {});