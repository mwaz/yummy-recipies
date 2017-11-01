$(document).ready(function(){

function getPid(pid,fname,lname,image){
 $("#pid").append(
  '<div style="margin-right:20px;">'+
  '<img src="'+image+'" class="img img-thumbnail" style="width:10%;margin-right:20px;"/>'+
  '<label> '+fname+' '+lname+'</label>'+
  '</div><br>'+
  '<input type="hidden" name="pid" value="'+pid+'"> '
  );
 $("#names").hide();
 $("#shownames").hide();
}

function getSpouse() {

  $('#names').on('input', function() {
    var image,person_id,fname,lname;  
    var searchKeyword = $(this).val();
    if (searchKeyword.length >=1) {
      $.post('search.php', { keywords: searchKeyword }, function(data) {
        $('#shownames').empty();
        $.each(data, function() {
          var image,person_id,fname,lname;
          image=this.img;
          person_id=this.mid;
          fname=this.fn;
          lname=this.ln;
          
          $('#shownames').append(
            '<div style="margin-right:20px;">'+
            '<a id="'+person_id+'">'+
            '<img src="'+image+'" class="img img-thumbnail" style="width:10%;margin-right:20px;"/>'+
            '<label> '+fname+' '+lname+'</label>'+
            '</a></div><br>'+
            '<hr style="margin-top: 3px;margin-bottom: 3px;">'
            );

          $("#"+person_id).click(function(){
            getPid(person_id,fname,lname,image);
          });
        });


      }, "json");
    }

  });
  return pid;
}


  $("#names").hide();
  $("#married").on('change',function(e){
    var selected=$(this).val();
    if(selected=='Married'){
      $("#names").show();
      var pid = getSpouse();
      $('#pid').append(pid);
    }
    else
    {
     $("#names").hide();
      $("#pid").hide();
       $("#shownames").hide();
   }
 });

//Editing personal info
 $("#dates").hide();
 $("#tel").hide();
 $("#county").hide();
 $("#rship").hide();
 $("#bio").hide();

 $("#1").on('click',function(e){
  $("#dates").fadeToggle("slow");
        // $("#1").hide();
      });

 $("#2").on('click',function(e){
  $("#county").fadeToggle("slow");
        // $("#2").hide();
      });
 $("#3").on('click',function(e){
  $("#tel").fadeToggle("slow");
        // $("#3").hide();
      });
 $("#4").on('click',function(e){
   $("#rship").fadeToggle("slow");
       // $("#4").hide();
     });
 $("#5").on('click',function(e){
  $("#bio").fadeToggle("slow");
        // $("#5").hide();
      });


  //show more/less post characters 
    var minielem = $('.postlength');
    minielem.each(function(){ 
      var t = $(this).text();
      if(t.length <500) 
        return; 
      $(this).html( t.slice(0,500)+'<span>...</span><a href="#" class="more"> read more</a>'+ '<span style="display:none;">'+ t.slice(500,t.length)+'<a href="#" class="less"> show less </a></span>' ); 
    }); 
    $('a.more', minielem).click(function(event){ 
      event.preventDefault(); 
      $(this).hide().prev().hide();
      $(this).next().show(); 
    }); 
    $('a.less', minielem).click(function(event){
      event.preventDefault(); 
      $(this).parent().hide().prev().show().prev().show();
    });


    //hide post
 //    $(document).ready(function(){
 //      var norows=$("#nrows").val();
 //    $("#hidep").click(function(e){
 //       var pid = document.getElementById('hpost').getAttribute('value');
 // $('.'+pid).fadeOut("slow");
 //      });

 //  });

 function hide(pid) {

   var item= pid;

   $("#hpost"+item).fadeOut("slow");

 }

      //show more/less comment characters  
        var minielem = $('.comlen');
        minielem.each(function(){ 
          var x = $(this).text();
          if(x.length <97) 
            return; 
          $(this).html( x.slice(0,97)+'<span> ...</span><a href="#" class="more"> read more</a>'+ '<span style="display:none;">'+ x.slice(97,x.length)+'<a href="#" class="less"> show less </a></span>' ); 
        }); 
        $('a.more', minielem).click(function(event){ 
          event.preventDefault(); 
          $(this).hide().prev().hide();
          $(this).next().show(); 
        }); 
        $('a.less', minielem).click(function(event){
          event.preventDefault(); 
          $(this).parent().hide().prev().show().prev().show();
        });
   



  $( ".loader" ).hide();
  $( ".sub" ).on('click',function(e){
    $( ".loader" ).show();
    $( ".ppspin" ).hide();

  });




//Posts, Followers and Following hide $ show
 $("#followers").hide();
 $("#following").hide();
 $("#pt").on('click',function(e){
  $("#posts").fadeToggle("slow");
  $("#followers").hide();
  $("#following").hide();
});

 $("#fws").on('click',function(e){
  $("#followers").fadeToggle("slow");
  $("#following").hide();
  $("#posts").hide();
});
 $("#fwg").on('click',function(e){
  $("#following").fadeToggle("slow");
  $("#posts").hide();
  $("#followers").hide();
});


  //Post tab hide $ show
   $("#postimage").hide();
   $("#postpost").hide();
   $("#daycomment").show();

   $("#post").on('click',function(e){
    $("#postpost").slideToggle();
    $("#postimage").hide();
    $("#daycomment").fadeOut("slow");
  });

   $("#camera").on('click',function(e){
    $("#postpost").hide();
    $("#postimage").slideToggle();
    $("#daycomment").fadeOut("slow");
  }); 


     //Reporting issue.
       $("#resultshow").hide();
       $("#result").on('click',function(e){
         $("#resultshow").fadeIn("slow");
       });


//fake/true input image post
  $("#trueinput").hide();
  $('#fakeinput').click(function(){
    $("#trueinput").click();
  });
 


   //Count characters
    $("#postbtn").prop("disabled",true);
    $("#imagebtn").prop("disabled",true);
    $('#writepost').on("keyup",function(e){
      var spacecheck = $(this).val();
      numchar=this.value.length;
      var maxchar=1500;
      if (numchar>0 && numchar<=maxchar && spacecheck!=" " ) {
       $('#countstr').css("color","green");
       document.querySelector('#countstr').innerHTML= numchar;
       $("#postbtn").prop("disabled",false);
     }
       else
     {
      $('#countstr').css({"color":"red","font-size":"80%"});
      document.querySelector('#countstr').innerHTML=numchar;
      $("#postbtn").prop("disabled",true);

    }

    // if (spacecheck='')
    // {
    //   $('#countstr').css({"color":"red","font-size":"80%"});
    //   document.querySelector('#countstr').innerHTML=numchar;
    //   $("#postbtn").prop("disabled",true);

    // }
  });


 $('#writecaption').on("keyup",function(e){
    var spacecheck = $.trim($(this).val().length);
    numchar=this.value.length;
    var maxchar=120;
    if (numchar>0 && numchar<=maxchar ) {
      $('#countcaption').css("color","green");
      document.querySelector('#countcaption').innerHTML= numchar;
      $("#imagebtn").prop("disabled",false);
    }
    else
    {
      $('#countcaption').css({"color":"red","font-size":"80%"});
      document.querySelector('#countcaption').innerHTML=numchar;
      $("#imagebtn").prop("disabled",true);

    }
  });

}); 



  //     $(document).ready(function(){
  //   $("#commentbtn").on('click',function(e){
  //     var pid = document.getElementById('commentarea').getAttribute('value');
  //     alert(pid);
  //     pid.hide();
  //       var textbox=document.getElementById('commentinput');
  //       textbox.focus();
  //       textbox.scrollIntoView();
  //     });
  // }); 
