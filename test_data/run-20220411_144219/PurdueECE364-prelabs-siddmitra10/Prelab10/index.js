const express = require("express");
const sqlite3 = require('sqlite3');
var bodyParser = require('body-parser');
const uuid = require('uuid');
const db = new sqlite3.Database('model/users.db');

const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
 
app.get("/register", (req, res) => {
    console.log(`GET: /register`);
    res.render("registerHomepage");
});

app.post("/register", (req, res) =>{
    console.log(`POST: /register`);
    var firstName = req.body.firstname;
    var lastName = req.body.lastname;
    var username = firstName.toLowerCase() + "_" + lastName.toLowerCase()
    var password = req.body.password;
    var id = uuid.v1();

    db.run(`INSERT INTO users VALUES("${id}", "${username}", "${password}")`, (err) => {
        if(err){
            db.get(`SELECT id FROM users WHERE username="${username}";`, (err, row) => {
                if(err){
                    console.log("badd");
                }
                console.log(`\t${row.id}`);
                res.redirect(`/${row.id}/profile`)
                // res.render("reg_return", {username:username, id:row.id});
            });
        }else{
            console.log(`\t${id}`);
            res.redirect(`/${id}/profile`)
            // res.render("reg_return", {username:username, id:id});
        }
    });
});

app.get("/:hashcode/profile", (req, res) => {
    id = req.params.hashcode;
    console.log(`GET: /${id}/profile`);
    db.all(`SELECT * FROM posts WHERE userID="${id}";`, (err, rows) => {
        if(err){
            res.send("ERROR 500");
        }else{
            // console.log(rows);
            db.get(`SELECT username FROM users WHERE id="${id}";`, (err, row) => {
                if(err){
                    res.send("ERROR 501");
                }
                else{
                    res.render("profile", {hashcode:id, data:rows, username:row.username});      
                }
            })
        }
        
    })
    // res.render("profile", {hashcode:id});
});

app.get("/:hashcode/create", (req, res) => {
    userid = req.params.hashcode;
    console.log(`GET: /${userid}/create`);
    postID = uuid.v1()
    res.render("createPost")
    // res.send({userid, postID})
});

app.post("/:hashcode/create", (req, res) => {
    userid = req.params.hashcode;
    console.log(`POST: /${userid}/create`);
    postID = req.body.postID;
    title = req.body.title;
    content = req.body.content;
    timestamp = Date.now();
    vote = 0;
    db.run(`INSERT INTO posts VALUES("${postID}", "${userid}", "${title}", "${content}", "${timestamp}", ${vote});`, (err) => {
        if(err){
            res.send("Error 500");
        }else{
            res.redirect(`/${userid}/profile`);
        }
    });
});

app.get("/post/:postid", (req, res) => {
    postID = req.params.postid
    console.log(`GET: /post/${postID}`);
    db.get(`SELECT * FROM posts WHERE postID="${postID}";`, (err,row) => {
        if(err){
            res.send("Error :(");
        }else{
            db.get(`SELECT username FROM users WHERE id="${id}";`, (err, user) => {
                if(err){
                    res.send("oops");
                }else{
                    res.render("post", {row, user})
                }                
            });
        }
    });
});

app.listen(5000)