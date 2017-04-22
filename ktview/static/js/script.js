$(document).ready(function() {
    console.log("DOC STARTED");

    $(".header-label").on("click", function(event) {
        var label = $(event.target)[0].innerText;
        console.log({ "label" : label });
        console.log(JSON.stringify({ "label" : label }));
        $.ajax({
            url: "/upload",
            type: "POST",
            data: JSON.stringify({ "label": label }),
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: function(response) {
                console.log("Successfully received parameter.");
            }
        });
    });

// Asynchronous (AJAX) file upload
/*
    $("#input").submit(function(e) {
        e.preventDefault();
        console.log("input received");

        $.ajax({
            url: "/upload",
            type: "POST",
            data: $("#input").serialize(),
            success: function(response) {
                console.log("File successfully uploaded.");
            }
        });
    });
*/

    var data = [{x: [1,2,3,4], y: [5,6,7,8], type: 'scatter'}];
    Plotly.newPlot('plot', data);

});
