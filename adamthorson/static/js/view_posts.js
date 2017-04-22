$(document).ready(function(){
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

    var blog_posts = [];


    var getSearchText = function(){
        var text = $('#search_input').val();

        if(!checkAlphanumeric(text)){
            if(isPromptVisible("ane")){
                showPrompt(
                    "Use alphanumeric characters and spaces",
                    "ane",
                    1750);
            }

            $('#search_input').val('');

            return false;
        }

        return text;
    };


    var clearTable = function(table){
        $('#' + table + ' tr').remove();
    };


    var clearDataAndTable = function(data_array, table){
        for(var i=data_array.length; i > 0; --i){
            data_array.pop();
        }
        clearTable(table);
    };


    var createTableRow = function(post){
        // Post attributes
        var slug = post['slug'];
        var title = post['title'];
        var img_url = "/static/img/blogging.jpg";
        var post_url = "/blog/" + slug;
        // UI setup
        // Left div
        // Post image & link
        var img_div = $('<div/>', {'class': 'img'});
        img_div.css('background-image', "url('" + img_url + "')");
        
        var a_img = $('<a/>', {'href': post_url});
        a_img.append(img_div);

        var left_div = $('<div/>', {'class': 'left'});
        left_div.append(a_img);

        // Right div
        // Attributes
        var title_div = $('<div/>', {
            'class': 'title',
            'text': title
        });
        var tags_div = $('<div/>', {'class': 'tags', 'text': 'tags'});
        var date_p = $('<p/>', {
            'text': formatDate(post['created_date'])
        });
        var bottom_div = $('<div/>', {'class': 'bottom'});
        bottom_div.append(date_p);

        var a_title = $('<a/>', {'href': post_url});
        a_title.append(title_div);
    
        var right_div = $('<div/>', {'class': 'right'});
        right_div.append(a_title);
        right_div.append(tags_div);
        right_div.append(bottom_div);

        // Combine left and right divs
        var post_div = $('<div/>', {'class': 'td_div_search_post'});

        post_div.append(left_div);
        post_div.append(right_div);

        var cell = $('<td/>').append(post_div);
        var row = $('<tr/>').append(cell);

        return row;
    };


    var storeTableData = function(data_array, result){
        for(var i=0; i < result.length; ++i){
            var post = result[i];
            var row = createTableRow(post);
            
            data_array.push({
                'title': post['title'],
                'html': row
            });
        }
    };


    var pushDataToTable = function(data_array, table){
        for(var i=0; i < data_array.length; ++i){
            $('#' + table + ' tbody').append(
                data_array[i]['html']);
        }
    };


    var loadTable = function(data_array, table){
        var search_text = getSearchText();

        if(!search_text){
            return;
        }

        $.ajax({
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            },
            method: 'POST',
            url: 'search/',
            'dataType': 'json',
            data: {'text': search_text},
            success: function(result){
                console.log(JSON.stringify(result));
                clearDataAndTable(data_array, table);
                storeTableData(data_array, result);
                pushDataToTable(data_array, table);
            }
        });
    };


    /*var sort = function(data_array, table){
        for(var i=0; i < (data_array.length - 1); ++i){
            var row_a = data_array[i];
            var row_b = data_array[i + 1];

            if(row_a['title'].toLowerCase() < row_b['title'].toLowerCase()){
                data_array[i] = row_b;
                data_array[i + 1] = row_a;
            }
        }

        clearTable(table);
        pushDataToTable(data_array, table);
    }*/


    $('#search_input').keydown(function(event){
        switch(event.which){
            case 13:
                loadTable(blog_posts, 'search_table')
                break;
            /*case 90:
                sort(blog_posts, 'search_table');
                break;*/
        }
    });
});