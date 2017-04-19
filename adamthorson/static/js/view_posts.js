$(document).ready(function(){
    var clearTable = function(table){
        $('#' + table + ' tr').remove();
    }


    var createTableRow = function(post){
        // Post attributes
        var title = post['title'];
        var img_url = "/static/img/blogging.jpg"
        // UI setup
        var img_div = $('<div/>', {
            'class': 'img',
            'css': 'background-image: url(\'' + img_url + '\')',
        });
        var title_div = $('<div/>', {
            'class': 'title',
            'text': title
        });
        var left_div = $('<div/>', {'class': 'left'});
        var right_div = $('<div/>', {'class': 'right'});

        left_div.append(img_div);
        right_div.append(title_div);

        var post_div = $('<div/>', {'class': 'td_div_search_post'});

        post_div.append(left_div);
        post_div.append(right_div);

        var cell = $('<td/>').append(post_div);
        var row = $('<tr/>').append(cell);

        return row;
    }


    var loadTable = function(table, result){
        clearTable(table);

        /*$.each(result, function(){
            $.each(this, function(k, v){
                str += k + " " + v + "\n";
            });
        });*/
        for(var i=0; i < result.length; ++i){
            var post = result[i];
            for(var j=0; j < 4; ++j){
                var row = createTableRow(post);
                $('#' + table + ' tbody').append(row);
            }
        }
    }


    $('#search_input').keydown(function(event){
        if(event.which === 13){
            $.ajax({
                url: 'search/',
                success: function(result){
                    loadTable('search_table', result);
                }
            });
        }
    });
});