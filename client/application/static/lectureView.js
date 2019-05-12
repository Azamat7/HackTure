document.getElementById('videoTitle').innerText = sessionStorage.videoTitle;
id = sessionStorage.getItem("videoID");
postReq(id);
document.getElementById('video').src = "https://www.youtube.com/embed/" + id;
postReqForVideos("Deep Learning");


function postReq(ID){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000/subtitles",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ videoID: ID}),
        success: function(data, textStatus) {
            // console.log(JSON.stringify(data));
            // $.when(setData(data)).then();
        }
    });
}

function postReqForVideos(terminQuery){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000/videos",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ query: terminQuery }),
        success: function(data, textStatus) {
            console.log("inSuccess")
            renderResults(JSON.stringify(data));
            // $.when(setData(data)).then(window.location = nextPage);
        }
    });
}

function renderResults(data1){
    data = JSON.parse(data1);
    myList1 = data.items;
    myList = myList1.slice(0, 5);
    var arrayLength = myList.length;
    console.log(myList[0].id.videoId);
    console.log(myList[0].snippet.title);
    for (var i = 0; i < arrayLength; i++) {
        var result = '<div class="item" width = "93" style = "border-radius: 14px; background-color: rgba(0,0,0,0.21);">' +
    '<div class="image" style = "border-color:transparent;">' +
    '<img src="'+ myList[i].snippet.thumbnails.high.url + '" style = "border-radius: 14px; ">' +
    '</div>' + 
    '<div class="content">' +
    '<a class="header myClass" videoId = "'+ myList[i].id.videoId +'" videoTitle = "'+myList[i].snippet.title+'">'+ myList[i].snippet.title +'</a>' +
    '<div class="meta">' +
    '<span>'+myList[i].snippet.channelTitle+'</span>' +
    '</div>' +
    '<div class="description">' +
    ' <p>'+myList[i].snippet.description+'</p> ' +
    '</div>' +
    '</div>' +
    '</div>'
    $(result).insertAfter(".fxd");
    }
}

$('.myClass').on('click',function(event){
    event.preventDefault();
    var videoId = $(this).attr('videoId');
    var videoTitle = $(this).attr('videoTitle');
    console.log("inside of func")
    console.log(videoId);
    console.log(videoTitle);
    sessionStorage.setItem("videoID", videoId);
    sessionStorage.setItem("videoTitle", videoTitle);
    // location.href = "/lectureView";
})