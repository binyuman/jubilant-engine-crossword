
function createBoard(numRows) {
    var parent = document.getElementById("body");
    var oldBoard = document.getElementById("board");
    var newTable = document.createElement("TABLE");
    if (oldBoard) {
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
	    cell.setAttribute("id","cell"+x+"-"+i);//each cell is named "cell*column*-*row* starting at 0 ofc
	}
    }
}

function smallBoard() {
    createBoard(15);
}


function bigBoard() {
    createBoard(21);
}


    

