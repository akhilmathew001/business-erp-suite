/**
 * Create Form View JS
 */


$(document).ready(function(){
	
	  $('#state,#country,#comapany').removeAttr('disabled');
	  $(':input').removeAttr('readonly')
	  $('.onchange-field').hide();
	  

	  $('.btn-create-save.mdl-button ').click(function(){
	    $(this).hide();
	    $('#form-jq').submit();
	  });

	  $('#checkbox-onchange-jq').click(function(event) {
	    $('.onchange-field').toggle(this.checked);
	  });

	  $(':input').focus(function(){

	    $(this).css('background-color','#cccccc');

	  });

	  $(':input').blur(function(){

	    $(this).css('background-color','#ffffff');

	  });

	
});