(function() {

  'use strict';

  $('.form__button').on('click', function(){
  	var inputList = $(this).closest('.form').find('.js-form-input');
  	var i = 0;
  	var name;
  	name = $('.js-form-input').val();
  	debugger;
  	// var formValidation = {};
  	// for(i; i < inputList.length; i ++) {
  	// 	formValidation.push(i);

  	// }


  });

})();


$(document).ready(function() {
	$('#contact_name').on('input', function() {

		var input=$(this);
		var re = /^[A-Za-z]+$/;
		var is_name=re.test(input.val());
		if(is_name){input.removeClass("invalid").addClass("valid");}
		else{input.removeClass("valid").addClass("invalid");}
});


	$('#contact_email').on('input', function() {
	var input=$(this);
	var re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
	var is_email=re.test(input.val());
	if(is_email){input.removeClass("invalid").addClass("valid");}
	else{input.removeClass("valid").addClass("invalid");}
});
$('#contact_address').on('input', function() {
	var input=$(this);
	var re = /^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$/;
	var is_email=re.test(input.val());
	if(is_email){input.removeClass("invalid").addClass("valid");}
	else{input.removeClass("valid").addClass("invalid");}
});


$('#contact_number').on('input', function() {
	var input=$(this);
	var re = /^[[0-9]+$/;
	var is_email=re.test(input.val());
	if(is_email){input.removeClass("invalid").addClass("valid");}
	else{input.removeClass("valid").addClass("invalid");}
});


	$("#contact_submit button").click(function(event){

var form_data=$("#contact").serializeArray();
	var error_free=true;
	for (var input in form_data){
		var element=$("#contact_"+form_data[input]['name']);
		var valid=element.hasClass("valid");
		var error_element=$("span", element.parent());
		if (!valid){error_element.removeClass("error").addClass("error_show"); error_free=false;}
		else{error_element.removeClass("error_show").addClass("error");}
	}
	if (!error_free){
		event.preventDefault(); 
	}
	else{
		alert('No errors: Form will be submitted');
	}


}); 

});



$(document).ready(function () {
    $("li").click(function () {
        //Toggle the child but don't include them in the hide selector using .not()
        $('li > ul').not($(this).children("ul").toggle()).hide();

    });
});


$(document).ready(function() {
    $('input[type="text"]').addClass("error");
	$('input[type="text"]').focus(function() {
		$(this).removeClass("valid").addClass("focusField");
        
    });
    $('input[type="text"]').blur(function() {
    	
    		
        
    });
});

$(document).ready(function () {
 
    $('#wrapper').resizable();
});

