// gets data from link and updates a div

$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
  $('DIV#hello').text(data.hello);
});
