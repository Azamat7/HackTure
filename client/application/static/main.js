
function postReq(searchQuery){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000",
        data: { query: searchQuery }
    });
}
function keyDownEvent(e) {
    if (e.keyCode == 13) {
        postReq(document.getElementById('srch').value);
        // location.href="./lectureView.html";
    }
}
function getReq(){
    $.getJSON("http://localhost:5000", function(data) {
    console.log(data)
    });
}
