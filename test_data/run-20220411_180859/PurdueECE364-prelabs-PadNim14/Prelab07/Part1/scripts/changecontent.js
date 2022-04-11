function changecontent(){
    var row = Number(prompt("Enter a row number.")) - 1;
    var col = Number(prompt("Enter a column number.")) - 1;
    // var message = 'sdklfjsdkfjslkdfjlskdjflskdjf'
    var myTable = document.getElementById("myTable")
    myTable.rows[row].cells[col].innerHTML = "Change";
}
//changecontent();