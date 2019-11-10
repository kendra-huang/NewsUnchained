window.onload = function(){
    var arr = ["Syntax","Chrome","Blogger", "Photos", "Keep", "HTML", "Skip", "Literal"];
    for (var i = 0; i < arr.length; i++)
    {
        var re = new RegExp(arr[i],'g');
        this.document.body.innerHTML = this.document.body.innerHTML.replace(re, arr[i].strike());
    }
};
/*






*/