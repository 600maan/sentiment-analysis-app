
var corpus = {
    getConcordance : function() {
            // retrieve the search query
            var search_word = document.getElementById('search_word').value
            $.ajax({
                method  : "GET",
                url     :"http://localhost:8000/concordance/",
                data    : { param : search_word },
                success :  corpus.displayConcordanceData
            });
    },
    displayConcordanceData : function(data) {
            $("#tbody").empty();
            var tbody = document.getElementById('tbody');
            for (var i = 0; i < data.length; i++) {
                var tr = "<tr>";
                tr += "<td>" + data[i][4] + " <strong>" + data[i][1] + "</strong> " + data[i][5] + "</td></tr>";
                tbody.innerHTML += tr;
            }
    }
}

