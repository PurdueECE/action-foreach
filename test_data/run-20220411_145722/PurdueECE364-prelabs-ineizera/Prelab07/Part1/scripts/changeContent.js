function changecontent(){
    var row = prompt("Enter row number of cell you want to change");
    var column = prompt("Enter column number of the cell you want to change");
    var content = prompt("Enter your desired cell content");
    var x = document.getElementById('myTable').rows[parseInt(row-1)].cells;
    x[parseInt(column-1)].innerHTML=content;
}