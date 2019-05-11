
function postReq(searchQuery){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ query: searchQuery })
    });
}

document.getElementById("searchInput").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        postReq(document.getElementById('searchInput').value);
        window.location="lectureList";
  }})

function getReq(){
    $.getJSON("http://localhost:5000", function(data) {
    console.log(data)
    });
}
