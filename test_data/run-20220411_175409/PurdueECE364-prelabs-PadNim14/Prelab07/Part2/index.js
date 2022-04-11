var express=require('express');
var bodyParser = require('body-parser');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
// console.log("It's here")
const sqlite3 = require('sqlite3');
const res = require('express/lib/response');
const crypto = require('crypto')
const db = new sqlite3.Database('models/database.db');

// console.log(uuid4)
app.get("/register", function (req, res) {
  res.render("register"), {};
});
app.post("/register", function (req, res) {
  // console.log("It's here")

  var username = req.body.username
  var password = req.body.password
  console.log(username);
  console.log(password);
  var id = crypto.randomUUID();
  db.run("INSERT INTO users (username, password, id) VALUES (?, ?, ?)", [username, password, id], (err) => {
    if (err) {
      console.log(err);
    }
  })
  // db.all("SELECT username, password from users;", (err, rows) => {
  //   console.log(rows);
  //   // console.log("It's here")

  //   data = rows;
    return res.render("profile", {name: username})
    // res.send(username);
    // console.log(username)
    // res.render('profile', {username});
    // res.send("/profile/user/")
  });

app.get("/profile/user/:name", function(req, res){
  
  data = db.get("SELECT * from posts where id = ?", [req.params.name], (err) => {
    if(err){
      console.log(err);
    }
  })
  console.log(req.params.id)
  console.log(data)
  res.render('profile', {name: req.params.name});
  // res.render("profile"), {}
});
// app.get("/:id/create", function (req, res) {
//   res.render("create"), {};
// });

// app.get("/:id/create", function(req, res) {
//     // var id = req.params.id;
//     // var title = req.body.title;
//     // var content = req.body.content;
//     // var time = req.body.time;
//     // var vote_count = req.body.vote_count;
//     // res.send(title)
//     // res.send(content)
//     // res.send(time)
//     // res.send(vote_count)
//     // console.log(title)
//     return res.render("create", {});
// });

// app.post("/:id/create", function (req, res) {
//   var id = req.params.id;
//   //console.log(id)
 
//   var title = req.body.title;
//   var content = req.body.content;
//   var time = req.body.time;
//   var vote_count = req.body.vote_count;
//   console.log(title)
//   // db.run("INSERT INTO posts (title, content, CURRENT_TIMESTAMP, vote_counter) VALUES (?, ?, ?, ?)", 
//   // [title, content, time, vote_count], (err) => {
//   //   if(err){
//   //     console.log(err);
//   //   }
//   // });
//   //console.log(id)
//   return res.render("create", {test: id})
// });


app.post("/:name/create", function(req, res){
  // res.send("HIIIIIII im ISHJ")
  // var id = req.params.id;
  // var title = req.body.title;
  // var content = req.body.content;
  // var time = req.body.time;
  // var vote_count = req.body.vote_count;
  
  // db.run("INSERT INTO posts (title, content, CURRENT_TIMESTAMP, vote_counter) VALUES (?, ?, ?, ?)", 
  // [title, content, time, vote_count], (err) => {
  //   if(err){
  //     console.log(err);
  //   }
  // });
  // console.log(id)
  // console.log(title)
  var id = crypto.randomUUID();
  return res.render("create", {id: id})
});
app.post("/:id/posts", function(req, res){
  var id = req.params.id;
  var title = req.body.title;
  var content = req.body.content;
  var time = req.body.time;
  var vote_count = 0;
  var id = crypto.randomUUID();
  db.run("INSERT INTO posts (title, content, CURRENT_TIMESTAMP, vote_counter) VALUES (?, ?, ?, ?)", 
  [title, content, time, vote_count], (err) => {
    if(err){
      console.log(err);
    }
  });
  // console.log(content)
  // console.log("Made it here")
  // console.log(vote_count)
  // res.send(content)
  // res.send(title)
  // res.send(vote_count)
  return res.render("post", {con: content, title: title, score: vote_count});
});

app.post("/profile/user/:name", function(req, res) {
  allposts = db.get("SELECT * from posts ORDER BY title DESC LIMIT 1")
  console.log(allposts)
  return res.render("post", {con: content, title: title, score: vote_count});

});


var server=app.listen(3000,function() {});