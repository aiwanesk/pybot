$(document).ready(function(){
    // Declare outside the assignement value zone to skip conflict between two requests
    var mymap;

    $("form").submit(function(e){
        // Stop data sending to server
        e.preventDefault();
        // Get the request from input
        var address_request = $("input").val();

        // Waiting for API response...
        $("#address").empty();
        $("#address").removeClass();
        if (!$("#address").hasClass('col-8 p-3 rounded text-center')) {
            $("#address").addClass('col-8 p-3 rounded text-center');
        }
        $("#address").append('<i class="fas fa-circle-notch fa-spin fa-2x"></i>');

        // Ajax call
        $.post('/ajax', {
            // Call the ajax view in Flask views.py
            address_request : address_request
        }).done(function(response){
            // If API calls return data...
            $("#address").empty();
            $("#address").removeClass('text-center');

            if (response['address']){
                var latitude = response['address']['latitude'];
                var longitude = response['address']['longitude'];
                var address_details = response['address']['details'];
                var address_answer = response['address']['address_answer'];
                var wiki_entity = response['address']['wiki_entity'];
                var wiki_informations = response['address']['wiki_informations'];
                var wiki_link = response['address']['wiki_link'];
                var wiki_answer = response['address']['wiki_answer'];

                // Clean the div in case of new request in the same session
                //$("#address").empty();
                // Display the address
                $("#address").append('<span>' + address_answer + '<span class="font-weight-bold">' + wiki_entity + '</span> se situe dans la région de ' + address_details['state'] + ' en ' + address_details['country'] + '.</span>');
                if (!$("#address").hasClass('answer')) {
                    $("#address").addClass('answer');
                }

                // Delete map reference to use the a new map when a new request come
                if (typeof mymap !== 'undefined'){
                    mymap.remove();  
                }
                
                // Set up the OSM map
                mymap = L.map('map').setView([latitude, longitude], 15);
                var marker = L.marker([latitude, longitude]).addTo(mymap);  

                // Mapbox tiles to display the map 
                L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibXZiLWhkZiIsImEiOiJjams1ZTdlNXQxN3lpM2txcXBlMHM1a3I0In0.T77BUlkk9mb8FDqlKRS3ZA', {
                    maxZoom: 18,
                    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
                        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                    id: 'mapbox.streets',
                }).addTo(mymap);

                if (!$("#map").hasClass('col-8 map')) {
                    $("#map").addClass('col-8 map');
                }
                
                // Display the Wiki informations
                $('#wiki').empty();
                $('#wiki').append('<p>' + wiki_answer + wiki_informations + '</p>');
                $('#wiki').append('<span>Si ça ne te suffit pas, je laisse Wikipédia t\'en dire plus : <a href="' + wiki_link + '" target="_blank">' + wiki_link + '</a></span>');
                if (!$("#wiki").hasClass('col-8 p-3 rounded answer')) {
                    $("#wiki").addClass('col-8 p-3 rounded answer');
                }
            }
            else{
                // If API calls don't return data...
                var error_answer = response['error_answer'];
                // Clean all div, to delete previous request informations
                $("#address").empty();
                $("#map").empty();
                $("#map").removeClass();
                $("#wiki").empty();
                $("#wiki").removeClass();

                if (!$("#address").hasClass('answer')) {
                    $("#address").addClass('answer');
                }
                $('#address').append('<span>' + error_answer + ' Malheureusement, <span class="font-weight-bold">' + address_request + '</span> ne semble pas encore repertorié sur OpenStreetMap. Si tu connais l\'endroit, tu peux contribuer en le rajoutant toi-même à OpenStreetMap : <a href="https://www.openstreetmap.org/" target="_blank">https://www.openstreetmap.org/</a></span>');
                $('#address').append('<p class="p-margintop">Le monde entier te dira merci, crois-en mon expérience ! :)</p>');
            }
        }).fail(function(response){
            console.log(response)
        });
    });
});
