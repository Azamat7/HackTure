
function postReq(searchQuery){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000",
        data: { query: searchQuery }
    });
}

document.getElementById("searchInput").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        postReq(document.getElementById('searchInput').value);
        window.location="lectureView";
  }})

function getReq(){
    $.getJSON("http://localhost:5000", function(data) {
    console.log(data)
    });
}
