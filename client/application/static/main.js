
function postReq(searchQuery, nextPage){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000/videos",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ query: searchQuery }),
        success: function(data, textStatus) {
            $.when(setData(data)).then(window.location = nextPage);
        }
    });
}

function setData(data){
    localStorage.setItem("searchResults", JSON.stringify(data)); 
}

document.getElementById("searchInput").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        postReq(document.getElementById('searchInput').value, "lectureList");
  }})

function getReq(){
    $.getJSON("http://localhost:5000", function(data) {
    console.log(data)
    });
}
