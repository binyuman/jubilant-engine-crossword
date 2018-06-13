
function createBoard(numRows) {
    var parent = document.getElementById("body");
    var oldBoard = document.getElementById("board");
    var newTable = document.createElement("TABLE");
    if (oldBoard) {
	//alert("table exists");
	parent.replaceChild(newTable,oldBoard);
	newTable.setAttribute("id","board");
	var board = newTable;
	board.setAttribute("border","1");
	board.setAttribute("width","50%");

    }
    else {
	newTable.setAttribute("id","board");	
	document.body.appendChild(newTable);
	var board = document.getElementById("board");
	board.setAttribute("border","1");
	board.setAttribute("width","50%");
    }
    var i;
    for (i = 0; i < numRows; i++) { 
	var row = board.insertRow(i);
	var x;
	for (x = 0; x < numRows; x++) {
	    var cell = row.insertCell(x);
	}
    }
}

function smallBoard() {
    createBoard(15);
}


function bigBoard() {
    createBoard(21);
}


    

