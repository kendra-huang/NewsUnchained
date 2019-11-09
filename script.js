/**
 * Javascript ~~~
 * 
 * 
 * var url;
    chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function(tabs){
        url = tabs[0].url;
    });
 * 
 */

chrome.browserAction.onClicked.addListener(function(tab) {
    // Send a message to the active tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      var activeTab = tabs[0];
      chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
    });
  });

 this.document.getElementById("new-tab-button").addEventListener("click", function(){ chrome.tabs.create({"url": "http://google.com"}); })