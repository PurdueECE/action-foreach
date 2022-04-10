var express=require('express');
var bodyParser = require('body-parser');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

var id=0;
var hash_array = new Array();
var current_hash;
 
const sqlite3 = require('sqlite3');

const db = new sqlite3.Database('model/database.db');

app.get("/register", function (req, res) {
  res.render("register_bootstrap");
});

app.get("/profile", function (req, res) {
  res.render("change");
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

    //db.all("SELECT ?, ? FROM users;", [username, password], (err, rows) => {
      //console.log(rows);
      //data = rows; })

    //if (rows.length == 0) {
        
      // If not, write user information in database

      db.run("INSERT INTO users (username, password) VALUES (?, ?)", [username, password], (err) => {
        if (err) {
          console.log(err);
        }
      })

        // Create a hashcode for the user

        hash_array.push(hashCode(id.toString()));

        current_hash = hash_array[id];
        id = id + 1;

    //}

    // Redirect to the profile page
      return res.redirect("/profile");
          
});

app.post("/profile", function (req, res) {

});

  
var server=app.listen(3000,function() {});