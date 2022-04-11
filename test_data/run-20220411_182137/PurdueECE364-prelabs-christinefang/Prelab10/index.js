var express=require('express');
var bodyParser = require('body-parser');
const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('model/user.db');
var uuid = require('uuid');
var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

 
// db.run(
//    `CREATE TABLE users(id INT, first_name TEXT, last_name TEXT, username TEXT, password TEXT)`
// );

// db.run(
//    `CREATE TABLE posts (postid INT, username TEXT, title TEXT, content TEXT, timestamp TEXT, votecounter INT)`
// );
     
app.get("/register", function (req, res) {
  res.render("register");
});

// Handling user signup
app.post("/register", function (req, res) {
  var first_name = req.body.first_name
  var last_name = req.body.last_name
  var username = req.body.username
  var password = req.body.password
  var hashcode = uuid.v4()


  db.run("INSERT INTO users (id,first_name, last_name, username, password) VALUES (?,?, ?, ?, ?)", [hashcode, first_name, last_name, username, password], (err) => {
    if (err) {
      console.log(err);
    }
  })
  res.redirect('/' + username + '/profile') //goes to user page
        });

  app.get("/:username/profile",function(req,res){ //user's profile
    var username = req.params.username
      db.all( "SELECT title,content,timestamp,votecounter FROM posts WHERE username=?",[username],(err,sql)=>{
      return res.render("profile", {username, sql});
    })
  })
    
app.get("/:username/create", function(req,res){
  var name = req.params.username

  res.render("message",{name});
})

app.post("/:username/messages",function(req,res) {
  var username = req.params.username
  var title = req.body.Title
  var content = req.body.messageText
  var timestamp = new Date().toLocaleTimeString()
  var votecounter = 0
  var hashcode = uuid.v4()
    db.run("INSERT INTO posts (postid, username, title, content, timestamp, votecounter) VALUES (?, ?, ?, ?, ?, ?)", [hashcode, username, title, content, timestamp, votecounter])
    res.redirect('/' + req.params.username + '/profile')

})

app.get("/posts/:title",function(req,res){
  var titles = req.params.title
  db.all( "SELECT username,title,content,timestamp,votecounter FROM posts WHERE title=?",[titles],(err,sql)=>{
    return res.render("posts", {sql});
  })
})

app.get("/:username/:title/delete",function(req,res){
    db.run('DELETE FROM posts WHERE title = ?',[req.params.title])
    res.redirect('/' + req.params.username + '/profile')
})

app.listen(8080,() =>{
  console.log('listening on localhost:3000')
})