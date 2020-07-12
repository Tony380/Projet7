var input = document.getElementById("input");
var map = document.getElementById("container");
var button = document.getElementById("button");

button.addEventListener("click", function(){
    var div1 = document.createElement("div")
    var div2 = document.createElement("div")
    var div3 = document.createElement("div")
    div1.setAttribute("id", "adress");
    div2.setAttribute("id", "map");
    div3.setAttribute("id", "wiki");
    map.appendChild(div1);
    map.appendChild(div2);
    map.appendChild(div3);
    function initMap(lat, lng){
        var place = {lat: lat, lng: lng};
        var map = new google.maps.Map(div2, {zoom: 15, center: place});
        var marker = new google.maps.Marker({position: place, map: map});
}

    var request = new XMLHttpRequest();
    request.open("get", "/api?question=" + input.value);
    request.responseType = "json";
    request.send();

    request.onload = function(){
        var coords = this.response;
        div1.innerHTML = coords['adress'];
        initMap(coords['lat'], coords['lng']);
    }
});


