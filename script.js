/**
 * Javascript ~~~
 * 
 * 
 * var url;
    
 * 
 */

this.document.getElementById("display-url").addEventListener("click", function(){ 
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function(tabs){
        document.getElementById("text").innerHTML = tabs[0].url;
    });
});

