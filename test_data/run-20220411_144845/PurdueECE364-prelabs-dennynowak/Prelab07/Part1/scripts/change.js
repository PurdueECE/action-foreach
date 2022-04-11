function changecontent() {

    // Get desired user info
    var row = prompt("Enter row number");
    var col = prompt("Enter column number");
    var content = prompt("Enter string to change content")
 
    // Retrieve specific element
    currBody = document.getElementsByTagName("body")[0];
    currTable = currBody.getElementsByTagName("table")[0];
    currRow = currTable.getElementsByTagName("tr")[row-1];
    currCol = currRow.getElementsByTagName("td")[col-1];
    cell = currCol.childNodes[0];
    
    // Replace content
    cell.data = content;   
}