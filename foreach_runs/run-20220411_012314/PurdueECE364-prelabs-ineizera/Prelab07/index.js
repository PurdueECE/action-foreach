var express = require('express');
var bodyParser = require('body-parser');

var app = express();
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

const sqlite3 = require("sqlite3").verbose();
const bcrypt = require("bcrypt");
const { request } = require('express');

const db = new sqlite3.Database("model/database.db", sqlite3.OPEN_READWRITE, (err) => {
    if(err) return console.log(err.message);

    console.log("connection successful.");
});

db.run("DROP TABLE IF EXISTS users");
db.run("CREATE TABLE users (username text UNIQUE, password text) ");

app.get("/register", function (req, res){
    res.render("register_bootstrap.ejs");
});

app.post("/register", async (req, res) => {
    var username = req.body.username
    var password = req.body.password

    const hashedcode = await bcrypt.hash(password, 10)

    console.log(username);
    console.log(hashedcode);
    db.run("INSERT INTO users (username, password) VALUES (?, ?)", [username, hashedcode], (err) => {
        if(err){
            console.log(err);
        }
    })

    return res.redirect(hashedcode + "/profile", { users: hashedcode, users: username });
    //return res.redirect(hashedcode + "/profile", { users: hashedcode, users: username });
    //return res.redirect("/profile", { users: username, users: hashedcode });
    //return res.render("profile.ejs", { users: hashedcode, users: username });
});

app.get(hashedcode + "/profile", function (req, res){
    req.params.hashedcode
    return res.render("profile.ejs");
    //return res.redirect(":hashedcode/profile" + req.params.hashedcode);
});
/*
app.post(hashedcode + "/profile", (req, res) => {

    //var title = req.body.title
    //var content = req.body.content
})
*/
//db.close((err) => {
//    if(err) return console.log(err.message); 
//});

var server = app.listen(3000, function() {});