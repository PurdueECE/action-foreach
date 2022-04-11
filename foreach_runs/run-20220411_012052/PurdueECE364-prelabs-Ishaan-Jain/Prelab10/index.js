var express=require('express');
var bodyParser = require('body-parser');

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
// console.log("It's here")
const sqlite3 = require('sqlite3');
const res = require('express/lib/response');
const crypto = require('crypto')
const db = new sqlite3.Database('model/database.db');


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
  console.log(id)
  db.run("INSERT INTO users (username, password, id) VALUES (?, ?, ?)", [username, password, id], (err) => {
    if (err) {
      console.log(err);
    }
  })


  res.render("register_complete",{user:username })

  return username

});


app.post("/:name/create", function (req, res) {
  // console.log("It's here")
  var id = req.params.name
  var title = req.body.title
  var content = req.body.content
  var time = req.body.time
  var vote_count = req.body.vote_count;



 return  res.render("form")


});









 



// Handling user signup
// app.post("/register", function (req, res) {
//   var username = req.body.username
//   var password = req.body.password
//   console.log(username);
//   console.log(password);
//   db.run("INSERT INTO users (username, password) VALUES (?, ?)", [username, password], (err) => {
//     if (err) {
//       console.log(err);
//     }
//   })
//   db.all("SELECT username, password from users;", (err, rows) => {
//     console.log(rows);
//     data = rows;
//     return res.render("register_complete", { users: data });
//   })
//         });

var server=app.listen(8000,function() {});



