duration = 10;

//video = document.getElementsByTagName("video");

var div = document.createElement("div");
var content;
div.setAttribute("style", ""
  +"color: black;"
  +"padding: 15px;"
  +"width: 50%;"
  +"height: 100px;"
  +"overflow: scroll;"
  +"border: 1px solid black;");
document.body.appendChild(div);
var inext;
for (var i = 0; i < duration; i = i + inext) {
	inext = Math.floor(Math.random()*duration)
	setTimeout(addElement(i,i+inext,document),500);
	
}
function addElement(integer,inext,document) {
	if (inext > duration) return;
	var text = document.createTextNode("Timestamp: " + integer + "s - " + inext + "s");
	var content = document.createElement("a");
	var br = document.createElement("br");
	content.appendChild(text);
	content.appendChild(br);
	content.setAttribute("href","");
	div.appendChild(content);
}