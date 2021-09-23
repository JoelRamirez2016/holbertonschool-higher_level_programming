const helloRequest = (lang) => {
  const url = 'https://fourtonfish.com/hellosalut';
  $.get(url + '/?lang=' + lang, function (data) {
    $('div#hello').text(data.hello);
  });
};

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    helloRequest($('input#language_code').val());
  });
  $('input#language_code').keyup(function (e) {
    if (e.keyCode === 13) helloRequest($(this).val());
  });
});
