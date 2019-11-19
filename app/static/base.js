var show_selected_file = function(){

	$('#brand-image').on('change', function(){

		var file = $(this)[0].files[0].name;

		$(this).next('label').text(file);
	})
}


$(document).ready(function(){

    $('body').fadeIn(500);

    show_selected_file()

});
