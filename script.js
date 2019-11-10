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
        console.log(results[0]);
    });
});

function parseText(text){

};
