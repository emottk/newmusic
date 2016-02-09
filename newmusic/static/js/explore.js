var animationDone = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';

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
      });
  });


  $('#dislike').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        type: form.attr('method'),
        url: e.target.action,
        data: form.serialize()
      })
      .done(function() {
        $('#artist_explore')
          .addClass('animated fadeOutRight')
          .one(animationDone, function() {
            location.reload(true);
          });
      });
  });

  $('#next').on('click', function(e) {
    e.preventDefault();
    $('#artist_explore')
      .addClass('animated fadeOutRight')
      .one(animationDone, function() {
        location.reload(true);
      });
  });
});
