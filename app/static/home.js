var update_text = function(location, new_text){
	var text_to_add = new_text
    $.ajax({
        type: "POST",
        url: '/update_text/home/'  + location,               
        dataType : "html",
        data : text_to_add,
        success: function(result){
        	alert("Text updated.")
            console.log(result)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var background_file_selected = function(){

    $('#background-image').on('change', function(){

        var file = $(this)[0].files[0].name;

        $(this).next('label').text(file);
    })
}


var set_text = function(){

	$('#commit-banner').on('click', function(){

		var new_text = $('#banner').html().trim()

		update_text('banner', new_text)

	})

	$('#commit-tagline').on('click', function(){

		var new_text = $('#tagline').html().trim()

		update_text('tagline', new_text)

	})
}

var get_background = function(){

    $('#img-home').css('background-image', 'url(' + background + ')' )   
}

var get_banner = function(){

    var banner_html = banner.replace(/&lt;/g, '<').replace(/&gt;/g, '>').split('&amp;nbsp;').join('')

    $('#banner').html(banner_html)
}

var get_tagline = function(){

    var tagline_html = tagline.replace(/&lt;/g, '<').replace(/&gt;/g, '>').split('&amp;nbsp;').join('')

    $('#tagline').html(tagline_html)
}


$(document).ready(function(){

    set_text()
    get_background()
    get_banner()
    get_tagline()
    background_file_selected()

});
