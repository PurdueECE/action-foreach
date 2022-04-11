////////////////////////////////
//  Author: Denny Nowak
//  Email:  nowak32@purdue.edu
//  ID:     ee364b14
//  Date:   02/27/2022
////////////////////////////////

var express=require('express');
var bodyParser=require('body-parser');
var crypto=require('crypto'); // Hashing func

var app=express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('model/database.db');

// Registration page for user signup
app.get("/register", function(req, res) {
    res.render("register_bootstrap");
});

app.post("/register", function(req, res) {
    var username = req.body.username
    var password = req.body.password

    // Check if existing user
    db.get("SELECT id from users where username = ? and password = ?", [username, password], (error, rows) => {
        if (error) {
            console.log(error);
        }
        else {
            // Existing user
            if (typeof rows != 'undefined') {
                res.redirect("/" + rows.id + "/profile");
            }
            // Create new user
            else {
                var idVar = crypto.randomBytes(16).toString('hex');
                db.run("INSERT INTO users (username, password, id) VALUES (?, ?, ?)", [username, password, idVar], (err) => {
                    if (err) {
                        console.log(err);
                    }
                })
                res.redirect("/" + idVar + "/profile");
            }
        }
    })
});

// User profile
app.get("/:idVar/profile", function(req, res) {
    var idVar = req.params.idVar;
    
    // Get Posts from User
    db.all("SELECT id from posts where hash = ?", [idVar], (error, rows) => {
            data = rows; 
            return res.render("create", {page : "/" + idVar + "/create", posts : data});
    })
    
});

// Create post
app.get("/:idVar/create", function(req, res) {
    var idVar = req.params.idVar;

    res.render("post_bootstrap", {page2 : "/" + idVar + "/create"});
});

// Create post based on user input, all posts are shared in same table
app.post("/:idVar/create", function(req, res) {

    // Get vals
    idVar = req.params.idVar
    title = req.body.title
    content = req.body.content
    timestamp = new Date();
    votecounter = 0

    // Get username from idVar
    db.get("SELECT username from users where id = ?", [idVar], (error, rows) => {
        if (error) {
            console.log(error);
        }
        else {
            // Check if valid username
            if (typeof rows != 'undefined') {
                db.run("INSERT INTO posts (title, content, timestamp, votecounter, user, hash) VALUES (?, ?, ?, ?, ?, ?)", [title, content, timestamp.toDateString() + " " + timestamp.toTimeString(), votecounter, rows.username, idVar], (err) => {
                    if (err) {
                        console.log(err);
                    }
                })
            }
        }
    })
    return res.redirect("/" + idVar + "/profile");
});

// Display Post
app.get("/posts/:postid", function(req, res) {
    var postid = req.params.postid;
    title = ''
    db.get("SELECT title, content, timestamp, votecounter, user from posts where id = ?", [postid], (error, rows) => {
        res.render("post", {title : rows.title, content: rows.content, timestamp : rows.timestamp, votecounter : rows.votecounter, user : rows.user});
    })
    
});

// Delete Post
app.get("/delete/:postid", function(req, res) {
    var postid = req.params.postid;
    db.get("DELETE from posts where id = ?", [postid], (error, rows) => {

    })
    return res.redirect('back');
});


//var server=app.listen(8080, function() {});
app.listen(8080, () => {
    console.log("App running on port 8080");
});
