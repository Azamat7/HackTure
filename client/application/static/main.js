
function postReq(searchQuery){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000",
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
function getReq(){
    $.getJSON("http://localhost:5000", function(data) {
    console.log(data)
    });
}
