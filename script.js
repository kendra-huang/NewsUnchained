/**
 * Javascript ~~~
 * 
 * 
 * var url;
    document.getElementById("display-url").addEventListener("click", function(){ 
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function(tabs){
        document.getElementById("text").innerHTML = tabs[0].url;
        url = tabs[0].url;
    });
});

 */




var current_url;

document.getElementById("display-url").addEventListener('click', () => {
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function(tabs){
        document.getElementById("text").innerHTML = current_url = tabs[0].url;
    });
    console.log("Popup DOM fully loaded and parsed");

    function getDOM() {
        return document.body.innerHTML;
    }
    //We have permission to access the activeTab, so we can call chrome.tabs.executeScript:
    chrome.tabs.executeScript({ code: '(' + getDOM + ')();' }, (results) => {
        //innerHTML of body logged
        // console.log stored as variable
        var str = results[0];
        chrome.tabs.create({ url: "data:text/html,"  + encodeURIComponent(parseText(str))});
    });
});

function parseText(str){
    console.log("bananaaaa");
    var arr = ["Syntax","Chrome","Blogger", "Photos", "Keep", "HTML", "Skip", "Literal"];
    for (var i = 0; i < arr.length; i++)
    {
        var re = new RegExp(arr[i],'g');
        str = str.replace(re, arr[i].strike());
    }
    return str;
};
