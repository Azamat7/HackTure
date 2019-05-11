console.log("Hello")
$.getJSON("http://localhost:5000", function(data) {
    console.log("Hey")
    console.log(data)
}).error(function() { console.log("Heдд") });