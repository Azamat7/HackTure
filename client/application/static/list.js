dict = localStorage.getItem("searchResults");
console.log(JSON.parse(dict));

dict = JSON.parse(dict);

list1 = document.getElementById("lst1");
console.log(dict.items[0].snippet.thumbnails.default.url);
list1.children[0].src = dict.items[0].snippet.thumbnails.default.url;