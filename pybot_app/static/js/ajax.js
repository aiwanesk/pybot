$(document).ready(function(){

    var mymap;

    $("form").submit(function(e){
        // Stop data sending to server
        e.preventDefault();
        // Get the request from input
        var address_request = $("input").val();

        // Waiting for API response...
        $("#map").html('<i class="fas fa-circle-notch fa-spin fa-2x"></i>');
        $("#map").addClass('map');

        $.post('/ajax-osm', {
            address_request : address_request
        }).done(function(response){
            
            if (response['address']){
                var latitude = response['address']['latitude'];
                var longitude = response['address']['longitude'];
                var address_details = response['address']['details'];
                var wiki_entity = response['address']['wiki_entity'];
                var wiki_informations = response['address']['wiki_informations'];
                var wiki_link = response['address']['wiki_link'];

                // Clean the div in case of new request in the same session
                $("#address").empty();
                // Display the address
                $("#address").append('<span>' + wiki_entity + ' se situe dans la région de ' + address_details['state'] + ' en ' + address_details['country'] + '.</span>');
                $('#address').addClass('answer');

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
                
                // Display the Wiki informations
                $('#wiki').empty();
                $('#wiki').append('<p>' + wiki_informations + '</p>');
                $('#wiki').append('<span>Si tu veux en savoir plus : <a href="' + wiki_link + '" target="_blank">' + wiki_link + '</a></span>');
                $('#wiki').addClass('answer');
            }
            else{
                $('#address').addClass('answer');
                $('#address').append('<p>Malheureusement, il me semble que cet endroit n\'est pas encore repertorié sur OpenStreetMap. Nhésite pas à contribuer en le rajoutant toi-même : </p>');
                $('#address').append('<a href="https://www.openstreetmap.org/" target="_blank">https://www.openstreetmap.org/</a>');
            }
        }).fail(function(response){
            console.log(response)
        });
    });
});
