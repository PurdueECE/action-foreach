function multiply() {
    var num1 = prompt("Enter the first number");
    var num2 = prompt("Enter the second number");
    var mult = num1 * num2;
    alert("The product of your inputs is: " + mult);
}

function changecontent(){
    var row = prompt("Enter row number");
    var column = prompt("Enter column number");
    var val = prompt("Enter number to change");
    var tab = document.getElementById("myTable");
    for (var i = 0, r; r = tab.rows[i]; i++){
        for (var j = 0, c; c = r.cells[j]; j++){
            if(i != row - 1){
                break;
            }
            if(j == column - 1){
                c.innerHTML = val;
                break;
            }
        }
    }
    return false;
}