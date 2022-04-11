function change(){
    let row_number = prompt("Enter the row number")
    let column_number = prompt("Enter the column number")
    let content = prompt("Enter the content for the table")
    row_number = row_number-1
    column_number = column_number-1
    table = document.getElementById('myTable')

    table.rows[row_number].cells[column_number].innerHTML = content
}