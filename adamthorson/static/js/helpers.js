var formatDate = function(epoch){
    var utcDate = new Date(epoch);
    var year = utcDate.getFullYear();
    var month = utcDate.getMonth();
    var day = utcDate.getDate();

    return (month + "/" + day + "/" + year);
}