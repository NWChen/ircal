$(document).ready(function() {
    console.log("DOC STARTED");

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
