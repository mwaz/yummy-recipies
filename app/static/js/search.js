$(document).ready(function() {
$('#keyword').on('input', function() {
	var searchKeyword = $(this).val();
	if (searchKeyword.length >=1) {
		// 	$("#topics").hide("slow");
		$.post('search.php', { keywords: searchKeyword }, function(data) {
			$('#content').empty();

			$('#content').append('<div style="margin-top:15px;">search pattern '+
				'<span style="margin-left: 10px;color:red; font-size:18px"> "' + searchKeyword+ '"</span>'+
				' <button id="searchhide" class="pull-right">X</button></div>'+
				'<br><hr style="margin-bottom: 3px;">')
$('#searchhide').on('click', function() {
$('#content').hide();
});

			$.each(data, function() {
				$('#content').append(
			'<a href="myprofile.php?b='+this.b+this.a+'&a='+this.a + '&pid='+ this.mid+'&a='+this.a +'">'+
					'<div class="row">'+

					'<div class="pull-left">'+
					'<img src='+ this.img + ' class="img img-thumbnail" style="width:10%;"/>'+

					
					'<span style="margin-left: 10px;">' + this.fn +' '+ this.ln + '</span>'+
					'<span style="margin-left: 10px;">(' + this.county +')</span>'+
					
					'</div>'+

					'</div>'+

			'</a><br>'+
					'<hr style="margin-top: 3px;margin-bottom: 3px;">');

			} );
		}, "json");
	}
});
});