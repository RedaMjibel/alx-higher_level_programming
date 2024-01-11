// translates Hello

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
    const lang = $('INPUT#language_code').val();
    const request = url + lang;
    $.getJSON(request, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});

