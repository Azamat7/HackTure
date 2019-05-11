// postReq(localStorage.getItem("videoID"));
postReq("g");

function postReq(ID){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000/subtitles",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ videoID: "VrMHA3yX_QI"}),
        success: function(data, textStatus) {
            console.log(data);
            console.log(JSON.stringify(data));
            // $.when(setData(data)).then();
        }
    });
}