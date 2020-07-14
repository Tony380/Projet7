var input = document.getElementById("input");
var map = document.getElementById("container");
var button = document.getElementById("button");

button.addEventListener("click", function(){
    var div = document.createElement("div");
    var div1 = document.createElement("div");
    var div2 = document.createElement("div");
    var div3 = document.createElement("div");
    div.setAttribute("id", "input_value");
    div1.setAttribute("id", "adress");
    div2.setAttribute("id", "wiki");
    div3.setAttribute("id", "map");
    map.appendChild(div);
    map.appendChild(div1);
    map.appendChild(div2);
    map.appendChild(div3);
    function initMap(lat, lng){
        var place = {lat: lat, lng: lng};
        var map = new google.maps.Map(div3, {zoom: 10, center: place});
        var marker = new google.maps.Marker({position: place, map: map});
}

    var request = new XMLHttpRequest();
    request.open("get", "/api?question=" + input.value);
    request.responseType = "json";
    request.send();

    request.onload = function(){
        var answer = this.response;
        div.innerHTML = input.value
        div1.innerHTML = "Bien sûr mon poussin, voici l'adresse : " + answer['coords']['adress'];

        var a = document.createElement('a');
        var link = document.createTextNode(" En savoir plus sur Wikipedia");
        a.appendChild(link);
        a.title = " En savoir plus sur Wikipedia";
        a.href = answer['url'];

        div2.innerHTML = "Au fait, je ne t'ai pas raconté. " + answer['page'];
        div2.append(a);
        initMap(answer['coords']['lat'], answer['coords']['lng']);
    }
});


