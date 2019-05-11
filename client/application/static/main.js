
function postReq(){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000",
        data: { name: "John", location: "Boston" }
    });
}

function getReq(){
    $.getJSON("http://localhost:5000", function(data) {
    console.log(data)
    });
}
