/* Main JavaScript file */

const input = document.getElementById("input");
const container = document.getElementById("container");
const button = document.getElementById("button");
const spinner = document.getElementById('spinner');

const displayInputValue = () => {
    /* Display the user's input value */
    let div = document.createElement("div");
    div.setAttribute("id", "input_value");
    container.appendChild(div);
    div.innerHTML = input.value;
    input.value = ''; // reset user input
    setTimeout(function(){ div.scrollIntoView({behavior: "smooth"}); }, 100); // delay scrolling
}

const displayAdress = (answer) => {
    /* Display adress from google */
    let div1 = document.createElement("div");
    div1.setAttribute("id", "adress");
    container.appendChild(div1);
    div1.innerHTML = "Ah oui! Je connais bien, voici l'adresse : " + answer['adress'];
}

const messageError = () => {
    /* Displayed if no answers are found */
    let div = document.createElement("div");
    div.setAttribute("id", "adress");
    container.appendChild(div);
    div.innerHTML = "Je n'ai rien trouvé à ce sujet, peux tu préciser?";
}

const displayWiki = (answer) => {
    /* Display Wikipedia article */
    let div2 = document.createElement("div");
    div2.setAttribute("id", "wiki");
    container.appendChild(div2);
    div2.innerHTML = "D'ailleurs, je ne t'ai pas raconté... " + answer['page'];

    /* Display url attached to Wikipedia article */
    let a = document.createElement('a');
    let link = document.createTextNode(" En savoir plus sur Wikipedia");
    a.appendChild(link);
    a.title = " En savoir plus sur Wikipedia";
    a.href = answer['url'];
    div2.append(a);
}

const initMap = (lat, lng) => {
    /* Display the google's map */
    let div3 = document.createElement("div");
    div3.setAttribute("id", "map");
    container.appendChild(div3);
    let place = {lat: lat, lng: lng};
    let map = new google.maps.Map(div3, {zoom: 10, center: place});
    let marker = new google.maps.Marker({position: place, map: map});
}

const emptyInput = () => {
    /* Displayed if user validated without writing anything */
    let div = document.createElement("div");
    div.setAttribute("id", "adress");
    container.appendChild(div);
    div.innerHTML = "Tu n'as rien saisi...";
}

const papybot = () => {
    /* Main function for displaying answers */
    if (input.value == ""){
        displayInputValue();
        emptyInput();
    }
    else{
        let request = new XMLHttpRequest();
        spinner.style.display = 'block';

        /* Escaping special chars for Xss security */
        input.value = input.value.replace(/<|>|#|&/g, "");

        request.open("get", "/api?question=" + input.value);
        request.responseType = "json";
        request.send();
        request.onload = function(){
            spinner.style.display = 'none';
            let answer = this.response;

            if (Object.keys(answer).length > 1){
                displayInputValue();
                displayAdress(answer);
                displayWiki(answer);
                initMap(answer['lat'], answer['lng']);
            }
            else{
                displayInputValue();
                messageError();
            }
        }
    }
}

button.addEventListener("click", () => {
    /* In case of click */
    papybot();
});

input.addEventListener('keyup', (event) => {
    /* In case of using enter's key */
    if (event.key == 'Enter') {
        papybot();
    }
});
