function newElement() {
    input = document.getElementById("myInput");
    text = document.createTextNode(input.value);
    li = document.createElement("li");
    li.appendChild(text);
    
    
    if (input.value == "") alert("You must write something!");
    else document.getElementById("myUL").appendChild(li);
    input.value = "";

    
    var span = document.createElement("span");
    var txt = document.createTextNode("\u00D7");
    span.appendChild(txt);
    span.className = "close";
    li.appendChild(span);


    span.onclick = function() {
        this.parentElement.style.display = "none";
    }
    li.onclick = function() {
        this.classList.toggle('checked');
    }
}