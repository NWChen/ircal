var graphDiv = 'plot'

$(document).ready(function() {
    console.log("DOC STARTED");
    var x = 0;
    var y = 0;
    var data = [{type: 'scatter'}];

    $("#upload").on("click", function(event) {
        $.getJSON('/_get_xaxis', {}, function(column) {
            data[x] = column.data;
        });
    });

    $(".header-label").on("click", function(event) {
        $.getJSON('/_get_data', {
            header: $(event.target)[0].innerText
        }, function(column) {
            Plotly.update(graphDiv, {y : column.data});
            console.log(column.data);
        }).done(function() {
            $(event.target).toggleClass("selected");
        });
    });

    // var data = [{x: x, y: y, type: 'scatter'}];
    Plotly.newPlot(graphDiv, data)
});
