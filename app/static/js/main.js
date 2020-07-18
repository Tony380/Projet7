var input = document.getElementById("input");
var container = document.getElementById("container");
var button = document.getElementById("button");
var spinner = document.getElementById('spinner');


function displayInputValue(){
    var div = document.createElement("div");
    div.setAttribute("id", "input_value");
    container.appendChild(div);
    div.innerHTML = input.value;
    input.value = '';
}

function displayAdress(answer){
    var div1 = document.createElement("div");
    div1.setAttribute("id", "adress");
    container.appendChild(div1);
    div1.innerHTML = "Ah oui! Je connais bien, voici l'adresse : " + answer['adress'];
}

function messageError(){
    var div = document.createElement("div");
    div.setAttribute("id", "adress");
    container.appendChild(div);
    div.innerHTML = "Je n'ai rien trouvé à ce sujet, peux tu préciser?";
}

function displayWiki(answer){
    var div2 = document.createElement("div");
    div2.setAttribute("id", "wiki");
    container.appendChild(div2);
    div2.innerHTML = "D'ailleurs, je ne t'ai pas raconté... " + answer['page'];

    var a = document.createElement('a');
    var link = document.createTextNode(" En savoir plus sur Wikipedia");
    a.appendChild(link);
    a.title = " En savoir plus sur Wikipedia";
    a.href = answer['url'];
    div2.append(a);
}

function emptyInput(){
    var div = document.createElement("div");
    div.setAttribute("id", "adress");
    container.appendChild(div);
    div.innerHTML = "Tu n'as rien saisi...";
}

function papybot(){
    if (input.value == ""){
        displayInputValue();
        emptyInput();
    }
    else{
        var request = new XMLHttpRequest();
        spinner.style.display = 'block';
        request.open("get", "/api?question=" + input.value);
        request.responseType = "json";
        request.send();
        request.onload = function(){
            spinner.style.display = 'none';
            var answer = this.response;
            if (Object.keys(answer).length > 1){
                displayInputValue();
                displayAdress(answer);
                displayWiki(answer);
                function initMap(lat, lng){
                    var div3 = document.createElement("div");
                    div3.setAttribute("id", "map");
                    container.appendChild(div3);
                    var place = {lat: lat, lng: lng};
                    var map = new google.maps.Map(div3, {zoom: 10, center: place});
                    var marker = new google.maps.Marker({position: place, map: map});
                }
                initMap(answer['lat'], answer['lng']);
            }
            else{
                displayInputValue();
                messageError();
            }
        }
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
