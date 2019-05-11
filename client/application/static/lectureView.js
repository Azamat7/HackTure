//id = sessionStorage.getItem("videoID");
id = "VrMHA3yX_QI"
script = null
index = 1
prevTime = "00:00"
prevCaption = ""
//postReq(id);

function postReq(ID,target){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000/subtitles",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ videoID: ID}),
        success: function(data, textStatus) {
            //console.log(data);
            //console.log(JSON.stringify(data));
            // $.when(setData(data)).then();
            script = data;
            target.playVideo();
        }
    });
}


var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
    console.log("YAY");
  player = new YT.Player('player', {
    height: '360',
    width: '640',
    videoId: id,
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });

}

function onPlayerReady(event) {
    console.log("playerReady");
    postReq(id,event.target);

    //event.target.playVideo();
}    

var done = false;
function onPlayerStateChange(event) {

    var myVar = setInterval(myTimer, 1000);
    function myTimer() {
        time = player.getCurrentTime()

        if (parseFloat(script[index-1]['start'])<parseFloat(time)){
            if (script[index]['text']){
                var min = Math.floor(parseFloat(script[index]['start'])/60);
                // if (min.length==1){
                //     min = "0"+min
                // }
                var sec = (Math.round(parseFloat(script[index]['start'])-min*60));
                // if (sec.length==1){
                //     sec = "0"+sec
                // }
                currTime =  min.toString()+ ":" + sec.toString(); 


                var currCaption = script[index]['text'];
                if (currCaption.indexOf("* *") != -1){
                    currCaption = currCaption.replace("* *", " ");
                }
                while (currCaption.indexOf("*") != -1){
                    start = currCaption.indexOf("*");
                    currCaption = currCaption.replace("*","$");
                    end = currCaption.indexOf("*");
                    var key = currCaption.slice(start+1,end);
                    currCaption = currCaption.replace("$", `<b style="color:yellow;" onclick="postReqWiki(\'${key}\');">`);
                    currCaption = currCaption.replace("*", '</b>');
                    console.log(currCaption);
                }

                document.getElementById('time1').innerHTML = "<p style=\"color:white;\">" + prevTime + "</p>";
                document.getElementById('caption1').innerHTML = "<p style=\"color:white;\">" + prevCaption + "</p>";

                document.getElementById('time2').innerHTML = "<p style=\"color:white;\">" + currTime + "</p>";
                document.getElementById('caption2').innerHTML = "<p style=\"color:white;\">" + currCaption + "</p>";

                prevTime = currTime;
                prevCaption = currCaption;
            }
            index+=1
        }
    }
}

function stopVideo() {
    player.stopVideo();
}


function postReqWiki(searchQuery){
    $.ajax({
        method: "POST",
        url: "http://localhost:5000/wiki",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({ keyword: searchQuery }),
        success: function(data, textStatus) {
            console.log(data);
        }
    });
}




