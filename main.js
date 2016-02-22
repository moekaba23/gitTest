var gpa100 = document.getElementById("gpa-100");
var result1 = document.getElementById("result1");

var gpa4 = document.getElementById("gpa-4");
var result2 = document.getElementById("result2");

gpa100.addEventListener("input", math);
gpa4.addEventListener("input", math2);

	
function math() {
	var input1 = parseFloat(gpa100.value) || 0;
	result1.innerHTML = "= "+((input1 / 100) * 4);
}

function math2() {
	var input2 = parseFloat(gpa4.value) || 0;
	result2.innerHTML = "= "+((input2 * 100) / 4);
}










