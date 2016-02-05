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
        form.closest('div.col-lg-3').remove();
      })
    })
  });
