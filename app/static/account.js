var validation_errors = function(errors, parent){
	$(".error-container").empty();
	for (var key in errors){
		var value = errors[key];
		if (value.length > 0) {
			var err;
			if (parent === true){
				err = $("#"+key).parent().children(".error-container");
			} else{
				err = $("#"+key).next();
			}
			err.html("<div class='validation-error'>" + value + "</div>");
		}
	}
}

var update_data = function(data){

	for (var key in data){

		var value = data[key];
		
		$("#" + key + "-value").html(value);
	}
}

var add_email_validation = function(){

	var email = new RegExp('^([a-zA-Z0-9_\\\-\\\.]+)@([a-zA-Z0-9_\\\-\\\.]+)\\\.([a-zA-Z]{2,5})$')

	jQuery.validator.addMethod("email", function(value) {
    
    	return email.test(value);
	}, "Please enter a valid email address.");
}

var add_password_validation = function(){

	jQuery.validator.addMethod("equal", function(value) {
    
    	return $('#new').val() === value
	}, "Passwords must match.");
}

var validate_account = function(form){

	form.validate({
  		rules: {
    		username: {
      			required: true
    		},
    		email: {
      			required: true
    		}
    	},
    	onkeyup: function(element, event) {
            if (event.which === 9 && this.elementValue(element) === "") {
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

var validate_password = function(form){

	form.validate({
  		rules: {
    		new: "required",
    		repeat: {
      			equalTo: "#new"
    		}
    	},
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

var update_account = function(form){

	var url = "/update_account"

	$.ajax({
		type: "POST",
		url: url,
		data: form.serialize(),
		success: function(data) {
			if (data[0] == "error") {
				validation_errors(data[1], true);
				if (data[2] !== false){
					validation_errors(data[2], true);
				}
			} else {
				console.log(data[1])
				update_data(data[1]);
				$(".error-container").empty();
				alert("Account updated.")
			}	
		},
		error: function(request, status, error){
            console.log("Error");
          	console.log(request)
   			console.log(status)
           	console.log(error)
       	}
	});
}

var update_password = function(form){

	var url = "/update_password"

	$.ajax({
		type: "POST",
		url: url,
		data: form.serialize(),
		success: function(data) {
			if (data[0] == "error") {
				validation_errors(data[1], true);
				if (data[2] !== false){
					validation_errors(data[2], true);
				}
			} 
			else if (typeof data == "string"){
				$("#update-password-form input[type='password']").val('');
				$(".error-container").empty();
				alert("Password updated.")
			} else {
				validation_errors(data, false);
			}
		},
		error: function(request, status, error){
            console.log("Error");
            console.log(request)
           	console.log(status)
           	console.log(error)
        }
	});
}

var remove_account = function(){

	var url = "/delete_account"

	$.ajax({
        type: "POST",
   		url: url,               
        success: function(result){
     		alert("Account deleted.")

     		$('body').fadeOut(300, function(){

     			window.location = "/login"
     		})
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


var account = function(){

	var form = $('#update-account-form')

	validate_account(form)
    
	$('#update-account').on('click', function (e) {

		e.preventDefault();

		if(form.validate().numberOfInvalids() == 0){

			if(confirm("Are you sure you want to update your account?")){

				update_account(form)
			}		
		}
		else {

			alert("Invalid input. Please check the highlighted fields.")
		}
	});
}


var remove = function(){

	$('#delete-account').on('click', function (e) {

		e.preventDefault()

		if(confirm('Are you sure you want to delete your account?')){

			remove_account()
		}	
	});
}

var password = function(){

	var form = $('#update-password-form')

    validate_password(form)

	$('#update-password').on('click', function (e) {

		e.preventDefault()

		if(form.validate().numberOfInvalids() == 0){

			if (confirm("Are you sure you want to update your password?")){

				update_password(form)
			}
		}
		else {

			alert("Invalid input. Please check the highlighted fields.")
		}
	});
}

$(document).ready(function(){

    account()
    password()
    remove()
    add_email_validation()
    add_password_validation()
	
});
