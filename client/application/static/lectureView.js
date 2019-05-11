id = sessionStorage.getItem("videoID");
postReq(id);
document.getElementById('video').src = "https://www.youtube.com/embed/" + id;

function postReq(ID){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000/subtitles",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ videoID: ID}),
        success: function(data, textStatus) {
            console.log(data);
            console.log(JSON.stringify(data));
            // $.when(setData(data)).then();
        }
    });
}