$(document).ready(function(){

  $('.submit-jq').hide();
  $('.btn-save').hide();
  $('.onchange-field').hide();

  $('.btn-edit.mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect').click(function(){
    $(this).hide();
    $(':input').removeAttr('readonly');
    $('#state,#country,#comapany').removeAttr('disabled');
    $('#checkbox-onchange-jq').show();
    $('.btn-dlt').hide();
    $('.btn-prnt').hide();
    $('.submit-jq').show();
    $('.btn-save').show();
    $('.form-button-group').css('margin-left', '178px');
    $(':input').css('background-color','rgba(180, 231, 229, 0.32)');

  });

  $('.btn-save').click(function(){
    $(this).hide();
    $(':input').attr('readonly','readonly');
    //$('#state,#country,#comapany').attr('disabled', 'disabled');
    $('.btn-dlt').show();
    $('.btn-prnt').show();
    $('.submit-jq').hide();
    $('.btn-save').show();
    $('#form-jq').submit();
    $(':input').css('background-color','#e8eeef');
  });

  $('#checkbox-onchange-jq').click(function(event) {
    $('.onchange-field').toggle(this.checked);
  });

});
