function changecontent(){
    var row = prompt("Select row: ");
    var column = prompt("Select column: ");
    var content = prompt("What content do you want to replace?");
    // "-1" since rows and columns starts from index 0
    var x = document.getElementById('myTable').rows[parseInt(row,10) - 1].cells;
    x[parseInt(column,10) - 1].innerHTML = content;
}

