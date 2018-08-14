// Clean all div, to delete previous request informations
function clean_all_div(){
    $("#address").empty();
    $("#map").empty();
    $("#map").removeClass();
    $("#wiki").empty();
    $("#wiki").removeClass();
}

function add_class_to(div_id, css_class){
    if (!$(div_id).hasClass(css_class)) {
        $(div_id).addClass(css_class);
    }
}