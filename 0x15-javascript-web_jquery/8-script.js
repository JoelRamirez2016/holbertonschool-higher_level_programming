$.get('https://swapi-api.hbtn.io/api/films', function (data) {
  data.results.forEach(movie => $('ul#list_movies').append('<li>' + movie.title + '</li>'));
});
