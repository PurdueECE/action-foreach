/////////////////////////////////////////////////////////////////////
// Author: Aedan Frazier
// Email : frazie35@purdue.edu
// ID    : ee364a06 
// Date  : 2/25/2022
/////////////////////////////////////////////////////////////////////


function multiply(){
    var a = prompt("What is the first number you want to multiply?");
    var b = prompt("What is the second number you would like to multiply?");
    var multiply = a * b;
    ret = a + " * " + b + " = " + multiply
    alert(ret);
}

function changecontent(){
    var row = prompt("Select Row") - 1;
    var col = prompt("Select Column") - 1;
    var str = prompt("Enter content");

    table = document.getElementsByTagName('table')[0];
    (table.rows[row]).cells[col].textContent = str;    
}
