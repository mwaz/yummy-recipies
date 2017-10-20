$(document).ready(function() {
$('#submit').on('click',function(e) {
	var htg = $('#hashtag').val();
	var mid = $('#mid').val();
	
		$.post('hashtag.php', { hashtag : htg , member_id : mid} , function(data) {

			// $('#myhashtags').show();
			$.each(data, function() {
	$('#myhashtags').append('<a href="">'+ this.tname +'</a><br><hr style="margin-top: 3px;margin-bottom: 3px;">');

			} );
		}, "json");
	
});
});