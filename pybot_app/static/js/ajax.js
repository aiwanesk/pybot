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
        add_class_to('#address', 'col-8 p-3 rounded text-center');
        $("#address").append('<i class="fas fa-circle-notch fa-spin fa-2x"></i>');

        // Ajax call
        $.post('/ajax', {
            // Call the ajax view in Flask views.py
            address_request : address_request
        }).done(function(response){
            // If API calls return data...
            $("#address").empty();
            $("#address").removeClass('text-center');

            if (response['answer_error']){
                clean_all_div()

                $('#address').append(
                    '<span>Je ne vois pas ce que tu veux dire. Tu es sûr·e de chercher un endroit du monde ? <i class="fas fa-grimace"></i></span>'
                );
                add_class_to('#address', 'answer');
            }

            else if (response['address']){
                var latitude = response['address']['latitude'];
                var longitude = response['address']['longitude'];
                var address_details = response['address']['details'];
                var address_answer = response['address']['address_answer'];
                var wiki_entity = response['address']['wiki_entity'];
                var wiki_informations = response['address']['wiki_informations'];
                var wiki_link = response['address']['wiki_link'];
                var wiki_answer = response['address']['wiki_answer'];

                if(typeof address_details['road'] == 'undefined'){
                    var address_road = ', plus précisement dans la rue ' + address_details['road'];
                    var road = true;
                }
                
                // Display the address
                $("#address").append(
                    '<span>' + address_answer + 
                    '<span class="font-weight-bold">' + wiki_entity + 
                    '</span> se situe dans la région ' + address_details['state'] +
                    ' en ' + address_details['country'] +
                    // If road is declared in API, display it
                    (typeof address_details['road'] == 'undefined' ? '' : ', plus précisement dans la rue ' + address_details['road']) + 
                    '. <i class="fas fa-grin-alt"></i></span>'
                );
                add_class_to('#address', 'answer');

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

                add_class_to('#map', 'col-8 map')
                
                // Display the Wiki informations
                $('#wiki').empty();
                // If there is no wiki informations
                if(wiki_informations.length == 0){
                    $('#wiki').append(
                        '<p>Cependant, je ne suis pas encore allée là-bas, alors je te laisse découvrir sur Wikipédia cet endroit : <a href="' + wiki_link + 
                        '" target="_blank">' + wiki_link + 
                        '</a> <i class="fas fa-smile-wink"></i></p>'
                    );
                }
                else{
                    $('#wiki').append('<p>' + wiki_answer + wiki_informations + '</p>');
                    $('#wiki').append(
                        '<span>Si tu veux être incollable sur le sujet, je laisse Wikipédia t\'en dire plus : <a href="' + wiki_link + 
                        '" target="_blank">' + wiki_link + 
                        '</a> <i class="fas fa-smile-wink"></i></span>'
                    );
                }
                
                add_class_to('#wiki', 'col-8 p-3 rounded answer')
            }
            else{
                // If API calls don't return data...
                var error_answer = response['error_answer'];
                var address_keyword = response['address_keyword'];
                
                clean_all_div()

                add_class_to('#address', 'answer')
                $('#address').append(
                    '<span>' + error_answer + 
                    ' Malheureusement, <span class="font-weight-bold">' + address_keyword + 
                    '</span> ne semble pas encore repertorié sur OpenStreetMap. Si tu connais l\'endroit, tu peux contribuer en le rajoutant toi-même ici : <a href="https://www.openstreetmap.org/" target="_blank">https://www.openstreetmap.org/</a></span>'
                );
                $('#address').append('<p class="p-margintop">Le monde entier te dira merci, crois-en mon expérience ! <i class="fas fa-smile-wink"></i></p>');
            }
        }).fail(function(response){
            console.log(response)
        });
    });
});
