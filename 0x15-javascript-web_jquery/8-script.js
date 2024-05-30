// JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$("document").ready(function () {
    const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
    $.get(url, function (data) {
        for (const movie of data.results) {
            $("#list_movies").append("<li>" + movie.title + "</li>");
        }
    });
});
