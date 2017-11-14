$(document).ready(function() {
  var postid = $("#lovevalue").val();
   
$('#love'+postid).on('click', function() {
 alert(postid);
     $.post('like_exec.php', { pid: postid }, function(data) {
      var no_of_lovers=data.lovebool;
var color_of_icon=data.type;
var pd=data.postid;
 alert(pd);
    }, "json");
  
});
});