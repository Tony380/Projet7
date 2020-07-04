const input = document.getElementById("input");
const map = document.getElementById("map");
const button = document.getElementById("button");

button.addEventListener("click", function(){
    div = document.createElement("div");
    map.appendChild(div);
    div.textContent = input;
});


