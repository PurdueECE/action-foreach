

var express=require('express');
var bodyParser = require('body-parser');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
 
const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('models/users.db');
// connection = sqlite3.connect('model/users.db');
// cur = connection.cursor();

app.get('/', function (req, res) {
    res.send('Go to /register to register!');
  });


app.get("/register", function (req, res) {
    res.render("register_bootstrap");
  });
  
  // Handling user signup
  app.post("/register", function (req, res) {
    var username = req.body.username
    var password = req.body.password
    console.log(username);
    console.log(password);
    id = (Math.random()) * (Math.random()) * 10
    db.run("INSERT INTO users (username, password, id) VALUES (?, ?, ?)", [username, password, id], (err) => {
      if (err) {
        console.log(err);
      }
    })
    db.all("SELECT username, password from users;", (err, rows) => {
      console.log(rows);
      data = rows;
      return res.render("register_complete", { id});
    })
          });
    
  
  var server=app.listen(8080,function() {});