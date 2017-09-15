var main = function() {
    
    btn = document.getElementById("btn");
    text = document.getElementById("text");
    text.style.color = "blue";
    
    btn.onclick = function() {
        if (text.style.color == "blue") {
            text.style.color = "yellow";
        }
        else {
            text.style.color = "blue";
        }
        
    }
    
}

$(document).ready(main)