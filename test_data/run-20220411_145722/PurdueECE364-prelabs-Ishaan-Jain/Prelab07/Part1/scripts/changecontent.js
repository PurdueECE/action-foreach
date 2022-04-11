function changecontent(){
    var row = prompt("Enter row number") ;
    row = row - 1;
    var col = prompt("Enter column number");
    col = col - 1;
    var myTable = document.getElementById("myTable");
    myTable.rows[row].cells[col].innerHTML = "Changes";
}