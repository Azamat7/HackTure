
function postReq(searchQuery){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000",
<<<<<<< HEAD
        data: { query: searchQuery }
    });
}

document.getElementById("searchInput").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        postReq(document.getElementById('searchInput').value);
        window.location="lectureView";
  }})

=======
        json: { "query" : searchQuery }
    });
}
function keyDownEvent(e) {
    if (e.keyCode == 13) {
        var tb = document.getElementById("srch");
        console.log(tb.value);
        postReq();
        location.href = 'lectureView';
    }
}
>>>>>>> 9eb85c0d1c845cdfca884090e75928f29ad135a4
function getReq(){
    $.getJSON("http://localhost:5000", function(data) {
    console.log(data)
    });
}
