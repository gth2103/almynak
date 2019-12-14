var send_mail = function(new_email){
	var email_to_add = new_email
    $.ajax({
        type: "POST",
        url: '/send_mail',               
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(email_to_add),
        success: function(result){
        	sent_flash()
            setTimeout(function(){
                window.location = "/contact"
            }, 4000)
        },
        error: function(request, status, error){
            error_flash()
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var send = function(){

    var form = $('#mail-form')

    form.validate()

	$('#contact').on('click', function(e){

		e.preventDefault()

		var fname = $('#fname').val().trim();
		var lname = $('#lname').val().trim();
		var email = $('#email').val().trim();
		var subject = $.trim($('#subject').val()).replace(/\"/g, "\\\"").replace(/\n/g, "\\n")
		var message = $.trim($('#message').val()).replace(/\"/g, "\\\"").replace(/\n/g, "\\n")

		var new_email = jQuery.parseJSON( '{ "fname": "' + fname + '", "lname": "' + lname + '", "email": "' + email + '", "subject": "' + subject + '",  "message": "' + message + '" }')

    send_mail(new_email)
	})
}

var error_flash = function(){

    $('#error_flash').removeClass('alert_show')
    $('#error_flash').addClass('alert_show')

    var flash_timer = setTimeout(function(){
        $('#error_flash').removeClass('alert_show')
        $('#error_flash').addClass('alert_hide')
        clearTimeout(flash_timer)
    }, 3500)
}

var sent_flash = function(){

    $('#sent_flash').removeClass('alert_show')
    $('#sent_flash').addClass('alert_show')

    var flash_timer = setTimeout(function(){
        $('#sent_flash').removeClass('alert_show')
        $('#sent_flash').addClass('alert_hide')
        clearTimeout(flash_timer)
    }, 3500)
}



$(document).ready(function(){

    $('body').fadeIn(500);

    send()

});
