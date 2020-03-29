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

var remove_member  = function(){

	$('.remove-user').on('click', function(){

		var member_id =  $(this).data('member')

		if(confirm("Are you sure you want to remove this member from the group? This operation cannot be undone." )) {

			remove(member_id)
		}
	})
}

var remove  = function(member_id){

	var member_to_add = member_id

    $.ajax({
        type: "POST",
        url: '/remove_member/' + member_id,               
        dataType : "text",
        success: function(result){
            alert("Member removed successfully.")
            window.location.reload();
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

var set_upload_member_img  = function(){

	$('#upload-user-image').attr('data-about', '<form class="dropdown-form d-inline-block" action="/upload_image/background-image/home" method="POST" enctype="multipart/form-data" onsubmit="return confirm(\'Are you sure you want to upload this background image? Changes will take effect immediately.\');"><div class="form-group"><label class="form-label pl-1">Select&nbsp;background&nbsp;image:</label><div class="custom-file d-block"><input type="file" class="custom-file-input" name="background-image" id="background-image"><label class="custom-file-label label pt-2" for="background-image">Image...</label></div></div><button id="upload-image" class="update btn btn-light mt-2 float-right" type="submit">Upload</button></form>')
}

$(document).ready(function(){

    modal_dynamic_select();
    remove_member();
    set_upload_member_img();

});
