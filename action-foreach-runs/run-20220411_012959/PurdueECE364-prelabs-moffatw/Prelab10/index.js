var express=require('express');
var bodyParser = require('body-parser');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
 
current_user = ""
hashcode = 0

const sqlite3 = require('sqlite3');

const db = new sqlite3.Database('model/database.db');

app.get('/', function(req, res){
  res.redirect('/register');
});

app.get("/register", function (req, res) {
  res.render("register_bootstrap");
});

app.get("/:code/profile", function (req, res) {
  const code = hashcode.toString()

  //db.get("SELECT * FROM posts where username = ?;", [current_user], (err, rows) => {
  db.all("SELECT * FROM posts;", (err, rows) => {
    console.log(rows); 
    console.log(rows[1].ID);

    //row_length = rows.length

    res.render("profile_page", {data: rows, length: rows.length});
  })
});

hashCode = function(s) {
  var h = 0, l = s.length, i = 0;
  if ( l > 0 )
    while (i < l)
      h = (h << 5) - h + s.charCodeAt(i++) | 0;
  return h;
};

// Handling user signup
app.post("/register", function (req, res) {
    var username = req.body.username
    var password = req.body.password
    console.log(username);
    console.log(password);

    // Check if user is already in database

    exists = false

    db.get("SELECT ?, ? FROM users;", [username, password], (err, rows) => {
      console.log(rows);
      data = rows; 
    
      if (rows.length != 0) {
        exists = true
      }
    })

    if (exists == false) {
        
      // If not, write user information in database

      db.run("INSERT INTO users (username, password) VALUES (?, ?)", [username, password], (err) => {
        if (err) {
          console.log(err);
        }
      })
    }

    // Create a hashcode for the user

    id_db = 0

    db.get("SELECT id FROM users where username = ? and password = ?", [username, password], (err, id) => {
      if (err) {
        console.log(err)
      }

      id_db = id
    }) 

    current_user = username
    hashcode = hashCode(id_db.toString())
    console.log(hashcode.toString())

    // Redirect to the profile page
      return res.redirect("" + hashcode.toString() + "/profile");
          
});

app.post("/:code/profile", function (req, res) {
  const code = hashcode.toString()

  // 
});

  
var server=app.listen(8080,function() {});