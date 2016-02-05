$(function() {
  $('#next').hide();
  $('#success').hide();
  $('#like').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        type: form.attr('method'),
        url: e.target.action,
        data: form.serialize()
      })
      .done(function() {
        $('form').hide();
        $('#next').show();
        $('#success').show();
      })
      .fail(function() {
        document.getElementById("fail").innerHTML = 'failed to save :(';
      });
  });
});


$(function() {
  $('form.delete').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        type: form.attr('method'),
        url: e.target.action,
        data: form.serialize()
      })
      .done(function() {
        $('#delete_notice').show();
        form.closest('div').remove();
      })
    })
  });
