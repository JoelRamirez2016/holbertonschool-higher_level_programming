$.get('https://swapi-api.hbtn.io/api/people/5', function (data) {
  $('div#character').text(data.name);
});
