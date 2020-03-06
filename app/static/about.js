var modal_dynamic_select = function(){

    $('#exampleModal').on('show.bs.modal', function (event) {
  
	var button = $(event.relatedTarget) // Button that triggered the modal
  
	var recipient = button.data('name') // Extract info from data-* attributes

	var roll = button.data('title')

	var body = button.data('about')
	
	// If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  
	// Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  
	var modal = $(this)
  
	modal.find('.modal-title').html('<span class="board-member font-weight-bold">' + recipient + '</span><br><span class="board-member-roll">' + roll + '</span>')
  	modal.find('.modal-body').html('<p>' + body + '</p>')
    })
};

$(document).ready(function(){

    modal_dynamic_select();

});
