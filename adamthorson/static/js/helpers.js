var showError = function(message, tag, ms){
    var $body = $(document.body);
    var message_p = $('<p/>', {'text': message});
    var error_div = $('<div/>', {
        'class': ('error_window float_center ' + tag)
    });

    error_div.append(message_p);

    $(document.body).append(error_div);

    var removeError = function(){
        error_div.remove();
    };

    setTimeout(function(){ 
        error_div.fadeOut("slow", removeError);
    }, ms );
};


var isErrorVisible = function(tag){
    return ($('.error_window, .' + tag).length < 1);
}


var checkAlphanumeric = function(str){
    var pattern = /[^a-zA-Z0-9\s]/g;
    return (!pattern.test(str));
};


var formatDate = function(epoch){
    var utcDate = new Date(epoch);
    var year = utcDate.getFullYear();
    var month = utcDate.getMonth();
    var day = utcDate.getDate();

    return (month + "/" + day + "/" + year);
};