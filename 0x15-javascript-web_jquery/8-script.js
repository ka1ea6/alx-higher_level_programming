$(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/films/?format=json",
    function (data) {
      $.each(data.results, function (i, movie) {
        const listItem = `<li>${movie.title}</li>`;
        $("#list_movies").append(listItem);
      });
    }
  );
});
