function changecontent(){
    let row = prompt("Enter row number")
    let column = prompt("Enter column number")
    let edit = prompt("Enter new content")
    row -= 1;
    column -= 1;
    let myTable = document.getElementById("myTable")
    myTable.rows[row].cells[column].innerHTML = `${edit}`; 
}
