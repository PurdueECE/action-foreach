var express=require('express');
var bodyParser = require('body-parser');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

 const sqlite3 = require('sqlite3');
 const database = new sqlite3.Database('model/users.db');

app.get('/',function(req,res)
{
res.render('home',{})});

app.get("/register", function (req, res) {
    res.render("register");
  });
  
  // Handling user signup
app.post("/register", function (req, res) {
    
    var username = req.body.username;
    var password = req.body.password;

    var hash = 0;
    for(var i = 0; i < (username.length); i ++){
        console.log(username[i].charCodeAt(0));
        hash += username[i].charCodeAt(0) * (i+1);
    }
    console.log(username);
    console.log(password);
    console.log(hash)
    var posts = "INIT"
    database.run("INSERT INTO users (username, password, hash, posts) VALUES (?, ?, ?, ?)", [username, password, hash, posts]);

    database.all("SELECT username, password, hash from users where username = ?;", username, (err, rows) => {
      console.log(rows);
      d = rows[0]

      var init_posts = ["NO POSTS YET"];

      data = {"username": d["username"], 
            "password": d["password"], 
            "hash": d["hash"],
            "posts": {}
            };
      console.log(data);
      return res.render("profile", {users: data});
      })


});









  app.get("/:hashcode/profile", function (req, res) {
    database.all("SELECT username, password, hash, posts from users where hash = ?;", req.params.hashcode, (err, rows) => {
        console.log(rows);
        d = rows[0]
        
        posts = rows[0]["posts"];
        arr = posts.split(",");
      ``
        database.all("SELECT title, pid, post from posts WHERE hash = ?",rows[0]["hash"],(err, rows) => {
          console.log(rows);
          data = {"username": d["username"], 
                "password": d["password"], 
                "hash": d["hash"],
                "posts": rows
              };
        console.log(data);
          return res.render("profile", {users: data});
        });
      });
  });




  app.get("/:pid/delete", function (req, res) {

    pid = req.params.pid;
    hash = pid.split("_")[0]
    database.run("DELETE FROM posts WHERE pid = ?;", pid);
    console.log("DELETED POST WITH PID " + pid);
    database.all("SELECT username, password, hash, posts from users where hash = ?;", hash, (err, rows) => {
        console.log(rows);
        d = rows[0]
        
        posts = rows[0]["posts"];
        arr = posts.split(",");
      ``
        database.all("SELECT title, pid, post from posts WHERE hash = ?",rows[0]["hash"],(err, rows) => {
          console.log(rows);
          data = {"username": d["username"], 
                "password": d["password"], 
                "hash": d["hash"],
                "posts": rows
              };
        console.log(data);
          return res.render("profile", {users: data});
        });
      });
  });









  app.post("/:hashcode/create", function (req, res) {
    database.all("SELECT username, password, hash, posts from users where hash = ?;", req.params.hashcode, (err, rows) => {
        //console.log(rows);
        d = rows[0]
        
        posts = rows[0]["posts"];
        posts = "INIT," +posts; 
        arr = posts.split(",");

        database.all("SELECT title, pid, post from posts WHERE hash = ?;",req.params.hashcode, (err, rows) => {
          console.log(rows);
          posts = rows[0];
          posts = "INIT," +posts; 
          rows["0"] = "INIT";
          data = {"username": d["username"], 
                "password": d["password"], 
                "hash": d["hash"],
                "posts": rows
              };
          console.log(data);
          return res.render("create", {users: data});
        });
     
    });
  });



  app.get("/:hashcode/create", function (req, res, next) {
    var title = req.query.title;
    var content = req.query.content;
    var timestamp = req.query.timestamp;
    var votecounter = req.query.votecounter;
    var pid = req.query.pid;

    console.log("Title: " + title);
    console.log("Content: " + content);
    console.log("Timestamp: " + timestamp);
    console.log("Votecounter: " + votecounter);
    console.log("PID: " + pid);

    hash = req.params.hashcode
    pid = hash + "_" + pid
    console.log(pid)

    database.all("SELECT hash,username, posts from users where hash = ?;", hash, (err, rows) => {
      database.run("INSERT INTO posts (hash,title,pid,post) VALUES (?, ?, ?, ?)", [hash,title,pid, content]);
      database.all("SELECT username, password, hash, posts from users where hash = ?;", req.params.hashcode, (err, rows) => {
        //console.log(rows);
        d = rows[0]

        console.log("get Create");

        database.all("SELECT title, pid, post from posts WHERE hash = ?;",hash, (err, rows) => {
          console.log(rows);
          data = {"username": d["username"], 
                "password": d["password"], 
                "hash": d["hash"],
                "posts": rows
              };
        console.log(data);
          return res.render("profile", {users: data});
        });
      });
    })
  });

var server=app.listen(8080,function(err) {
    if(err){
        console.log("ERROR");
    }
});