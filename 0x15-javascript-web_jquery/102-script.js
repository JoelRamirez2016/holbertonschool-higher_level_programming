$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut';
  $('input#btn_translate').click(function () {
    $.get(url + '/?lang=' + $('input#language_code').val(), function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
