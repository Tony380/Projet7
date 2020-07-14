var input = document.getElementById("input");
var container = document.getElementById("container");
var button = document.getElementById("button");

function display(){
    var request = new XMLHttpRequest();
    request.open("get", "/api?question=" + input.value);
    request.responseType = "json";
    request.send();

    request.onload = function(){
        var answer = this.response;

        var div = document.createElement("div");
        var div1 = document.createElement("div");
        var div2 = document.createElement("div");
        var div3 = document.createElement("div");

        div.setAttribute("id", "input_value");
        div1.setAttribute("id", "adress");
        div2.setAttribute("id", "wiki");
        div3.setAttribute("id", "map");

        container.appendChild(div);
        container.appendChild(div1);
        container.appendChild(div2);
        container.appendChild(div3);

        div.innerHTML = input.value;
        div1.innerHTML = "Bien sûr mon poussin, voici l'adresse : " + answer['coords']['adress'];

        var a = document.createElement('a');
        var link = document.createTextNode(" En savoir plus sur Wikipedia");
        a.appendChild(link);
        a.title = " En savoir plus sur Wikipedia";
        a.href = answer['url'];

        function initMap(lat, lng){
        var place = {lat: lat, lng: lng};
        var map = new google.maps.Map(div3, {zoom: 10, center: place});
        var marker = new google.maps.Marker({position: place, map: map});
        }

        div2.innerHTML = "Au fait, je ne t'ai pas raconté. " + answer['page'];
        div2.append(a);
        initMap(answer['coords']['lat'], answer['coords']['lng']);
        input.value = '';
    }
}

function papybot(){
    if (input.value == ""){
        var div = document.createElement("div");
        div.setAttribute("id", "adress");
        container.appendChild(div);
        div.innerHTML = "Tu n'as rien saisi";
    }
    else{
        display();
    }
}

button.addEventListener("click", function(){
    papybot();
});

input.addEventListener('keyup', function(event) {
    if (event.key == 'Enter') {
        papybot();
    }
});
