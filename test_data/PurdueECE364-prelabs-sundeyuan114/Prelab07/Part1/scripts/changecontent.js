// function changecontent(){
//     var row = prompt("input the row number to be changed ");
//     var col = prompt("input the column number to be changed ");
//     var cont = prompt("input the content to be changed ");
//     mytable = document.getElementsByTagName("table")[0];
//     myrow = document.getElementsByTagName("tr")[row];
//     myobj = document.getElementsByTagName("td")[col].innerHTML=cont;
// }
// changecontent()
var row;
var col;
var cont;
function changecontent(){
    row = prompt("input the row number to be changed ");
    col = prompt("input the column number to be changed ");
    cont = prompt("input the content to be changed ");
    //myobj = document.getElementsByTagName("td")[row*col - 1].innerHTML=cont;
}


function usure(){
    alert("this is ur input row: " + row +" col : "+ col +" content : " + cont)
    mytable = document.getElementsByTagName("table")[0]
    myrows = mytable.getElementsByTagName("tr")[row-1]
    myobj = myrows.getElementsByTagName("td")[col-1].innerHTML=cont;
}
