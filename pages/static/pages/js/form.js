$('#but-func-input').on('click', function() {
  var star = $("input[name='score']").val();
  localStorage.setItem("score", star);
  star = localStorage.getItem("score");
  $('#star_inp').val(star);
});
