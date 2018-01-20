$('#las_form_button').on('click', function() {
  var from_send = $("#hot-form-from").val();
  var to_send = $("#hot-form-to").val();
  var date_start = $("#hot-form-start-date").val();
  var date_finish = $("#hot-form-finish-date").val();
  var night = $("#hot-form-nights").val();
  var adults = $("#hot-form-adults").val();
  var child = $("#hot-form-children").val();

  localStorage.setItem("from_send", from_send);
  localStorage.setItem("to_send", to_send);
  localStorage.setItem("date_start", date_start);
  localStorage.setItem("date_finish", date_finish);
  localStorage.setItem("night", night);
  localStorage.setItem("adults", adults);
  localStorage.setItem("child", child);

  from_send = localStorage.getItem("from_send");
  to_send = localStorage.getItem("to_send");
  date_start = localStorage.getItem("date_start");
  date_finish = localStorage.getItem("date_finish");
  night = localStorage.getItem("night");
  adults = localStorage.getItem("adults");
  child = localStorage.getItem("child");

  $('#from_send').val(from_send);
  $('#to_send').val(to_send);
  $('#date_start').val(date_start);
  $('#date_finish').val(date_finish);
  $('#night').val(night);
  $('#adults').val(adults);
  $('#child').val(child);
});
