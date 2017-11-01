$(document).ready(function() {
	$("#newuser").prop("disabled",true);
$('#keyword').on('focusout', function() {
		var searchKeyword = $(this).val();
		var searchlength = searchKeyword.length;
		var pass,repass;
		$.post('reg.php', { keywords: searchKeyword }, function(data) {
			var error = parseInt(data);
			// alert(error);
			if (error>0 ) {
				$('#error').html('<p style="color: red;">'+"Username is already taken!" +'</p>');
				$("#newuser").prop("disabled",false);
				 			}
			else if (searchKeyword=='') {
				$("#newuser").prop("disabled",true);
$('#error').html('<p style="color: red;">'+"Username too long!" +'</p>');
							}
							else if (searchlength>15) { 
$("#newuser").prop("disabled",true);
$('#error').html('<p style="color: red;">'+"Username too long!" +'</p>');
							}
							else{

                $('#error').html('<i class="glyphicon glyphicon-ok-sign" style="color:green;font-size:30px;"></i>');

			}

		});
	});
$('#pass').on('focusout', function() {
	pass=$('#pass').val();

	if(pass.length<5){
		$("#newuser").prop("disabled",true);
$('#errorpass').html('<p style="color:red;">'+"Password must be more than 5 characters." +'</p>');
	} else{ 
		$("#newuser").prop("disabled",false);
		$('#errorpass').html('<i class="glyphicon glyphicon-ok" style="color:green;"></i>'); 
	}
});

$('#repass').on('focusout', function() {
	repass=$('#repass').val();
	if(pass !=repass){
		$("#newuser").prop("disabled",true);
$('#errorrepass').html('<p style="color:red;">'+"Password did not match" +'</p>');
	} else{ 
$("#newuser").prop("disabled",false);
		$('#errorrepass').html(''); }
});
});

function deletel(postid){
	var post_d=postid
	var con=confirm("Are you sure you want to delete?");
	if (con==true)
	{
	$('#postt'+post_d).hide();
	$('#wait'+post_d).html('<p style="color:red;">Deleting...</p>');
		$.ajax({
			url: 'deletepost.php',
			data: {post_id:post_d},
			type: 'POST',
			dataType:'html'
		})
.done(function(data){
	$('#wait'+post_d).hide();
$('#deleteinfo'+post_d).html('<p style="color:red;">'+data+'</p>');
	})
	.fail(function(){
		alert('Technical failure ...'); 

	});
}
		
}
