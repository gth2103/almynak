var send_mail = function(new_email){
	var email_to_add = new_email
    $.ajax({
        type: "POST",
        url: '/' + group_id + '/send_mail',               
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(email_to_add),
        success: function(result){
            alert("Message sent.")
        },
        error: function(request, status, error){
            alert("Ooops! Something went wrong. Please try again.")
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var eager_eval = function(form){

    form.validate({

        onkeyup: function(element, event) {
            if (event.which === 9 && this.elementValue(element) === "" ) {
                return;
            } else {
                this.element(element);
            }
        },
        onfocusout: function(element) {
            this.element(element); 
        }
    })
}

var contact = function(){

    var form = $('#mail-form')

    eager_eval(form)

	$('#contact').on('click', function(e){

		e.preventDefault()

		var fname = $('#fname').val().trim();
		var lname = $('#lname').val().trim();
		var email = $('#email').val().trim();
		var subject = $.trim($('#subject').val()).replace(/\"/g, "\\\"").replace(/\n/g, "\\n")
		var message = $.trim($('#message').val()).replace(/\"/g, "\\\"").replace(/\n/g, "\\n")

		var new_email = jQuery.parseJSON( '{ "fname": "' + fname + '", "lname": "' + lname + '", "email": "' + email + '", "subject": "' + subject + '",  "message": "' + message + '" }')

        if($('#mail-form').validate().numberOfInvalids() == 0){

            if(confirm("Please verify that you are ready to send this message to CUBPS.")){

                send_mail(new_email)
            }
        }
        else{
            alert("Invalid Input. Please check the highlighted fields.")
        }
    })
}

$(document).ready(function(){

    contact()

});
