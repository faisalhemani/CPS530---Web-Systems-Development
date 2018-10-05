var count = 1;
var container = document.getElementById("info");
var albumArt = document.getElementById("pic");
var other = document.getElementById("other");
var btn = document.getElementById("btn");
btn.addEventListener("click", function(){
        var ourRequest = new XMLHttpRequest();
        ourRequest.open('GET', 'text.json');
        ourRequest.onload = function(){
                if(ourRequest.status>=200 && ourRequest.status<400){
                        var ourData = JSON.parse(ourRequest.responseText);
                        renderHTML(ourData);
                }
                else{
                        console.log("server error");
                }
};
ourRequest.onerror = function(){
        console.log("connection fail");
}
ourRequest.send();
count++;
if (count >1){
	btn.classList.add("hide-me");
}
});

function renderHTML(data){
        var htmlString = "";
	var picString = "<img src=" + data.tracks.track.cover + " height=100% width=100%;>";
        var otherString = "<p>Current Rank: " + data.tracks.track.current  + "<br>Unique ID: " + data.tracks.track.uniqueid + "<br>Start Time: " + data.tracks.track.starttime  + "<br>Play Duration: " + data.tracks.track.playduration  + "<br>Call Me Back: " + data.tracks.track.callmeback  + "</p>" ;
	htmlString += "<p>" + data.tracks.track.title + " <br>by " + data.tracks.track.artists + "</p>";
        albumArt.insertAdjacentHTML('beforeend', picString);
	container.insertAdjacentHTML('beforeend', htmlString);
	other.insertAdjacentHTML('beforeend',otherString);
}

