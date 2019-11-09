/**
 * Javascript ~~~
 * 
 * 
 * var url;
    
 * 
 */
var url;

this.document.getElementById("display-url").addEventListener("click", function(){ 
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function(tabs){
        document.getElementById("text").innerHTML = tabs[0].url;
        url = tabs[0].url;
    });
});

function parseText(text){

};