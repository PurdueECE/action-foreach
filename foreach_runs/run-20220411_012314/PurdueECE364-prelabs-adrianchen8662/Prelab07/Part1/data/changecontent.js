function changeContent()
{
    rn = window.prompt("Input the row number");
    cn = window.prompt("Input the column number");
    content = window.prompt("Input the cell content");  

    var x=document.getElementById('myTable').rows[parseInt(rn,10)].cells;
    x[parseInt(cn,10)].innerHTML=content;
}