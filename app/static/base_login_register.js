var clear_flash = function(){

	if ($('.flashes').length > 0){

		setTimeout(function(){

			$('.flash-containter').fadeOut(1000)
		}, 5000)
	}
}


$(document).ready(function(){

	clear_flash()
});
