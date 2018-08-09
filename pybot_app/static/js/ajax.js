$(document).ready(function(){

    var mymap;

    $("form").submit(function(e){
        // Stop data sending to server
        e.preventDefault();
        // Get the request from input
        var address_request = $("input").val();

        $("#map").addClass('map');
        $("#map").html('<i class="fas fa-circle-notch fa-spin fa-2x"></i>');

        $.post('/ajax-osm', {
            address_request : address_request
        }).done(function(response){
            
            if (response['address']){
                var latitude = response['address']['latitude'];
                var longitude = response['address']['longitude'];
                var address_details = response['address']['details']

                if (typeof mymap !== 'undefined'){
                    mymap.remove();  
                }

                // Display the request as a chat message
                $('#address').addClass('answer');
                $("#address").append('<p>' + address_request + '</p>');

                mymap = L.map('map').setView([latitude, longitude], 15);
                var marker = L.marker([latitude, longitude]).addTo(mymap);                        

                L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibXZiLWhkZiIsImEiOiJjams1ZTdlNXQxN3lpM2txcXBlMHM1a3I0In0.T77BUlkk9mb8FDqlKRS3ZA', {
                    maxZoom: 18,
                    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
                        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                    id: 'mapbox.streets',
                }).addTo(mymap);
                
                // Display the Wiki informations
                $('#wiki').addClass('answer');
                $('#wiki').append('<p>' + response['address']['wiki_informations'] + '</p>');
                $('#wiki').html('<a href="' + response['address']['wiki_link'] + '" target="_blank">' + response['address']['wiki_link'] + '</a>');
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
