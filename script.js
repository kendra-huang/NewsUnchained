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

 * 
 */

/**
 * Javascript ~~~
 * 
 * 
 * var url;
    
 * 
 */

 var str = "";

document.getElementById("display-url").addEventListener('click', () => {
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function(tabs){
        document.getElementById("text").innerHTML = tabs[0].url;
    });
    console.log("Popup DOM fully loaded and parsed");

    function modifyDOM() {
        return document.body.innerHTML;
    }
    //We have permission to access the activeTab, so we can call chrome.tabs.executeScript:
    chrome.tabs.executeScript({ code: '(' + modifyDOM + ')();' }, (results) => {
        //innerHTML of body logged
        // console.log stored as variable
        str = results[0];
        console.log(str);
    });
});

function parseText(str){
    
    var arr = ["hello", "hi", "banana"];
    var arrVal = "";
    var str = "";
    for (var i = 0; arr.length(); i++)
    {
        arrVal = arr[i];
        text = document.write("<p>Strike: " + txt.strike() + "</p>");
        str.replace(str, text);
    }
    
    // arrayBiased = xmlDoc.getElementsByTagName('sentence')[0].childNodes[0].nodeValue;


};
