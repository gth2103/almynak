const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

var date = function(){

	var d = new Date();

	$('#currentDate1').html(monthNames[d.getMonth()] + " " + d.getDate())
}

var date_correction = function(){

	setTimeout(function(){

		$('#todayButton1').trigger('click')	
	}, 300)
}




$(document).ready(function(){

	date()
	
	date_correction()
    
});
