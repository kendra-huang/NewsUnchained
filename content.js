/**
 * Content file can access the DOM directly,
 * and can communicate to the scipt file through
 * message listeners, which send and receieve packaged data
 */
chrome.runtime.onMessage.addListener( function(request, sender, sendResponse) {
    document.body.innerHTML = request.body;
    sendResponse({result: "success"});
});



