/**
 * Javascript ~~~
 */

var arr = ["trump", "racist", "america", "african", "money", "businesses"];

document.getElementById("display-url").addEventListener('click', function (tabs)
{
    function getDOM()
    {
        return document.body.innerHTML;
    }
    var e = document.getElementById("option-type");
    var selected = e.options[e.selectedIndex].value;

    //We have permission to access the activeTab, so we can call chrome.tabs.executeScript:
    chrome.tabs.executeScript({ code: '(' + getDOM + ')();' }, (results) =>
    {
        console.log("Popup DOM fully loaded and parsed");
        //innerHTML of body logged
        // console.log stored as variable
        var str = results[0];
        var new_body = selected == '1' ? parseText(str) : highlightSearchTerms(str);// the new innerHTML
        
        console.log(new_body);
        //func to update the contents of the page to be 
        chrome.tabs.query({ 'active': true, 'lastFocusedWindow': true }, function (tabs)
        {
            chrome.tabs.sendMessage(tabs[0].id, { body: new_body }, function (response)
            {
                console.log(response.result);
            });
        });
    });
        
});

/** 
 * Strikeout text function
 */
function parseText(str)
{
    for (var i = 0; i < arr.length; i++)
    {
        var re = new RegExp('('+arr[i]+')','gi');
        str = str.replace(re, "$1".strike());
    }
    return str;
};

/*
 * This is the function that actually highlights a text string by
 * adding HTML tags before and after all occurrences of the search
 * term. You can pass your own tags if you'd like, or if the
 * highlightStartTag or highlightEndTag parameters are omitted or
 * are empty strings then the default <font> tags will be used.
 */
function doHighlight(str, searchTerm, highlightStartTag, highlightEndTag)
{
  // the highlightStartTag and highlightEndTag parameters are optional
    if ((!highlightStartTag) || (!highlightEndTag))
    {
        highlightStartTag = "<font style='color:blue; background-color:yellow;'>";
        highlightEndTag = "</font>";
    }

  // find all occurences of the search term in the given text,
  // and add some "highlight" tags to them (we're not using a
  // regular expression search, because we want to filter out
  // matches that occur within HTML tags and script blocks, so
  // we have to do a little extra validation)
  var newText = "";
  var i = -1;
  var lcSearchTerm;
  var lcstr;

  lcSearchTerm = searchTerm.toLowerCase();
  lcstr = str.toLowerCase();

    while (str.length > 0)
    {
        i = lcstr.indexOf(lcSearchTerm, i+1);
        if (i < 0)
        {
          newText += str;
            str = "";
        }
        else
        {
            // skip anything inside an HTML tag
            if (str.lastIndexOf(">", i) >= str.lastIndexOf("<", i))
            {
                // skip anything inside a <script> block
                if (lcstr.lastIndexOf("/script>", i) >= lcstr.lastIndexOf("<script", i))
                {
                    newText += str.substring(0, i) + highlightStartTag + str.substr(i, searchTerm.length) + highlightEndTag;
                    str = str.substr(i + searchTerm.length);
                    lcstr = str.toLowerCase();
                    i = -1;
                }
            }
        }
    }
  return newText;
}

/*
 * This is sort of a wrapper function to the doHighlight function.
 * It takes the searchText that you pass, optionally splits it into
 * separate words, and transforms the text on the current web page.
 * Only the "searchText" parameter is required; all other parameters
 * are optional and can be omitted.
 */
function highlightSearchTerms(str, highlightStartTag, highlightEndTag)
{
    for (var i = 0; i < arr.length; i++)
    {
      str = doHighlight(str, arr[i], highlightStartTag, highlightEndTag);
    }
    return str;
}