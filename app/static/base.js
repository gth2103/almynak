var colors = ['dark', 'light', 'black']

var upload_image = function(){

    var page = location.href.split("/")[location.href.split("/").length - 1]

    $('#upload-image-form').attr('action', '/upload-image/brand-image/' + page)
}

var fade_navbar = function(){

    $(window).scroll(function(){
        if ($(window).scrollTop() > 200){
            $('.title').fadeOut(750);
        }
        else {
            $('.title').fadeIn(750);
        }
        if ($(window).scrollTop() > 350){
            $('.banner').fadeOut(650);
            $('.banner-about').fadeOut(650);
        }
        else {
            $('.banner').fadeIn(650);
            $('.banner-about').fadeIn(650);
        }
    });
}

var theme_color = function(){

    var background = {

        'dark': '#343a40',
        'light': '#f8f9fa',
        'black': '#1a1e21'
    }

    $('#theme-color').empty()

    colors.forEach(function(color){

        if(!$('body').hasClass('bg-' + color)){

            $('#theme-color').append('<div id="' + color + '" class="color d-inline-block bg-' + color + ' rounded-circle m-2"></div>')
            $('#' + color).css('box-shadow',  background[color] + ' 0px 0px 4px')
        }
    })
}

var update_theme_color = function(new_color){

    var color_to_add = new_color

    $.ajax({
        type: "POST",
        url: '/update_color',               
        dataType : "text",
        data : color_to_add,
        success: function(result){

            remove_theme_color()

            add_theme_color()

            theme_color()

            alert("Theme has been changed.")

            $('body').fadeOut(100, function(){

                window.location.reload()
            })   
        },
        error: function(request, status, error){
            alert("Ooops! Something went wrong. Please try again.")
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var update_theme = function(){

    colors.forEach(function(color){

        $('#' + color).on('click', function(){

            if(confirm("Are you sure you want to change the base color? Changes will take effect immediately.")){

                update_theme_color(color)
            }
        });
    })
}

var add_theme_color = function(color){

    $('body').addClass('bg-' + color)

    $('.base').addClass('bg-' + color)

    $('#enter').addClass('btn-' + color)

    $('#contact').addClass('btn-' + color)

    $('.update').addClass('btn-' + color)
}

var remove_theme_color = function(){

    colors.forEach(function(color){

        if($('body').hasClass('bg-' + color)){

            $('body').removeClass('bg-' + color)
        }
        if($('.base').hasClass('bg-' + color)){

            $('.base').removeClass('bg-' + color)
        }
        if($('#enter').hasClass('btn-' + color)){

            $('#enter').removeClass('btn-' + color)
        }
        if($('#contact').hasClass('btn-' + color)){

            $('#contact').removeClass('btn-' + color)
        }
        if($('.update').hasClass('btn-' + color)){

            $('.update').removeClass('btn-' + color)
        }
    })
}

var show_brand_file_selected = function(){

	$('#brand-image').on('change', function(){

		var file = $(this)[0].files[0].name;

		$(this).next('label').text(file);
	})
}

var send_menu = function(new_menu){
	var menu_to_add = new_menu
    $.ajax({
        type: "POST",
        url: '/update_menu',               
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(menu_to_add),
        success: function(result){
            $('body').fadeOut(150, function(){

                window.location.reload()
            })
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var add_path_validation = function(){

    jQuery.validator.addMethod("path", function(value) {
    
        var path = ['/about', '/members', '/calendar', '/contact'];

        return $.inArray(value, path) != -1;
    }, "Path provided is invalid");
}

var update_menu = function(){

    var form = $('#menu-form')

    form.validate()

	$('#update-menu').on('click', function(e){

		e.preventDefault()

		var item1_name = $('#name1').val().trim();
		var item1_path = $('#path1').val().trim();
		var item2_name = $('#name2').val().trim();
		var item2_path = $('#path2').val().trim();
		var item3_name = $('#name3').val().trim();
		var item3_path = $('#path3').val().trim();
		var item4_name = $('#name4').val().trim();
		var item4_path = $('#path4').val().trim();

		var new_menu = jQuery.parseJSON( '{ "' + item1_name + '": "' + item1_path + '", "' + item2_name + '": "' + item2_path + '", "' + item3_name + '": "' + item3_path + '", "' + item4_name + '": "' + item4_path + '" }')

		if($('#menu-form').validate().numberOfInvalids() == 0){

            if(confirm("Are you sure you want to update the menu? Changes will take effect immediately.")){

                send_menu(new_menu)
            }	
		}
	})
}

var quick_scroll_up = function(){

    $('.up-arrow-adjust').on('click', function(){

        $('html, body').animate({

            scrollTop : 0
        }, 'slow')

        return false;
    })

    $('.up-arrow').on('click', function(){

        $('html, body').animate({

            scrollTop : 0
        }, 'slow')
        
        return false;
    })
}


$(document).ready(function(){

    show_brand_file_selected()
    update_menu()
    fade_navbar()
    add_path_validation()
    theme_color()
    update_theme()
    quick_scroll_up()
    upload_image()
});
