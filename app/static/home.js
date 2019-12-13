var update_text = function(location, new_text){
	var text_to_add = new_text
    $.ajax({
        type: "POST",
        url: '/update_text/home/'  + location,               
        dataType : "html",
        data : text_to_add,
        success: function(result){
        	alert("Text was submitted.")
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

var commit_text = function(){

	$('#commit-banner').on('click', function(){

		var new_text = $('#banner').html().trim()

		update_text('banner', new_text)

	})

	$('#commit-tagline').on('click', function(){

		var new_text = $('#tagline').html().trim()

		update_text('tagline', new_text)

	})
}



$(document).ready(function(){

    $('body').fadeIn(500);

    commit_text()

});
