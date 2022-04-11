var express=require('express')
var bodyParser = require('body-parser')

var app = express();
app.set("view engine",'ejs')
app.use(bodyParser.urlencoded({ extended: true}));

const sqlite3 = require('sqlite3');

const db = new sqlite3.Database('model/database.db');

function hashingFunction()
{
    return Math.floor(Math.random()*1000000000);
}

app.get('/', function(req, res){
  res.send('Hello World');
});

app.get("/register",function(req,res)
{
    res.render("register_bootstrap");
});

app.post("/register",function(req,res)
{
    var username = req.body.username;
    var password = req.body.password;

    var hashcode = hashingFunction();

    var found = 0;
    db.all("SELECT username, password from users;", (err,rows) => 
    {
        data = rows;
        for (let i = 0; i < data.length; i++) {
            console.log(data[i].username)
            console.log(username)
            console.log(data[i].password)
            console.log(password)
            if (data[i].username == username && data[i].password == password)
            {
                found = 1;
            }
        }
        if (found == 0)
        {
            db.run("INSERT INTO users (username, password, hash) VALUES (?, ?, ?)", [username, password, hashcode], (err) => {
                if (err) {
                    console.log(err);
                }
            })
        }
        else
        {

        }
    })

    db.all("SELECT username, hash from users;", (err, rows) => {
        data = rows;
        console.log(data)
        return res.render("register_complete", { users: data });
      })
});

app.get("/profile/:hashedcode",function(req,res)
{
    res.render("profile")
    return res.render("posted")
});


var server = app.listen(3000, function() {
  console.log('Listening on port %d', server.address().port);
});