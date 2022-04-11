function changecontent() {
	var row = parseInt(prompt("Enter the row number:")) - 1;
	var col = parseInt(prompt("Enter the column number:")) - 1;
	var string = prompt("Enter what to replace with:");
	var tag = document.getElementById("myTable").childNodes[1];
	tag.childNodes[row * 2].childNodes[col * 2].innerHTML = string;
}
