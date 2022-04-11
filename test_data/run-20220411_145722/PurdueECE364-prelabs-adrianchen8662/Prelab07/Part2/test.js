var express=require('express')
var bodyParser = require('body-parser')

var app = express();
app.set("view engine",'ejs')
app.use(bodyParser.urlencoded({ extended: true}));

const sqlite3 = require('sqlite3');

const db = new sqlite3.Database('model/database.db');

app.get('/', function(req, res){
  res.send('Hello World');
});

app.get("/register",function(req,res)
{
    res.render("register_bootstrap");
});

app.post("/register",function(req,res)
{
    var username = req.body.username
    var password = req.body.password

    var hashcode = hashingFunction();

    

    /* Look for things in database*/
});

app.get("/profile/:hashedcode",function(req,res)
{
    res.render("register_bootstrap")
    res.send("hashedcode is set to " + req.params.hashedcode);
});


var server = app.listen(3000, function() {
  console.log('Listening on port %d', server.address().port);
});