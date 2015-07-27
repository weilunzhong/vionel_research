$(function() {
    $('#submitBtn').click(function() {
        var userInput = $("[name='inputMovies']").val();
        var rcNum = $("[name='recommendNum']").val();

        if (userInput == "") {
            alert("Please input movie imdb ids, seperated by comma.");
            return false;
        } else if (rcNum == "") {
            alert("Please input number of recommend movies");
            return false;
        } else {
            return true;
        }
    });
});