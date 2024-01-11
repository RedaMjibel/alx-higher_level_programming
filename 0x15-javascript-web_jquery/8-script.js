// gets data from link and updates a div

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  }
});
