mapboxgl.accessToken = 'pk.eyJ1IjoidmFsZW50aW41MjM2NTQzIiwiYSI6ImNrZGcydDdrODJtYnUyenM4NTU1ZjJ4bGgifQ.Sj1H6D61OzVW7fm6WZ7xcA';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-124.43115234375, 40.44694705960048],
    zoom: 5
});
map.on('load', function () {
    map.addSource('earthquakes', {
        type: 'geojson',
        // Use a URL for the value for the `data` property.
        data: 'https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson'
    });

    map.addLayer({
        'id': 'earthquakes-layer',
        'type': 'circle',
        'source': 'earthquakes',
        'paint': {
            'circle-radius': 8,
            'circle-stroke-width': 2,
            'circle-color': 'blue',
            'circle-stroke-color': 'white'
        }
    });
});

table_container = document.getElementById("table_container")

name_input = document.getElementById("name_input")
depth_input = document.getElementById("depth_input")
date_input = document.getElementById("date_input")

edit_links = document.getElementsByClassName("edit_link")
delete_links = document.getElementsByClassName("delete_link")
default_links = document.getElementsByClassName("default_link")

main_form = document.getElementById("main_form")
add_btn = document.getElementById("add_btn")

delete_menu = document.getElementById("delete_menu")
delete_button = document.getElementById("delete_button")
back = document.getElementById("back")


for(var i = 0; i < edit_links.length; i++){
    edit_links[i].onclick = function() {
        id = this.value
        st_name = document.getElementById("td_name_" + id).textContent.trim();
        depth = document.getElementById("td_depth_" + id).textContent.trim();
        date = document.getElementById("td_date_" + id).textContent.trim();
        main_form.action = 'http://localhost:8000/station_edit/' + id
        main_form.style.display = 'block'
        table_container.style.display = 'none'
        add_btn.textContent = 'Изменить'

        name_input.value = st_name
        depth_input.value = depth
        // пока так
        date_input.value = 'May/7/2021 1:05'
    }
}


document.getElementById("create").onclick = function () {
    main_form.action = 'http://localhost:8000/station_create/'
    main_form.style.display = 'block'
    add_btn.textContent = 'Создать'
    table_container.style.display = 'none'
    
};


for(var i = 0; i < delete_links.length; i++){
    delete_links[i].onclick = function() {
        id = this.value
        name = document.getElementById("td_name_" + id).textContent.trim();
        depth = document.getElementById("td_depth_" + id).textContent.trim();
        date = document.getElementById("td_date_" + id).textContent.trim();

        delete_menu.style.display = 'block'
        back.style.display = 'block'
        delete_button.href = 'http://localhost:8000/station_delete/' + id
    }
}

document.getElementById("cancel_button").onclick = function() {
    back.style.display = 'none'
    delete_menu.style.display = 'none'
}


document.getElementById("edit").onclick = function () {
    if (edit_links[0].style.display == 'inline') {
        for (var i = 0; i < default_links.length; i++) {
            default_links[i].style.display = 'inline';
        }
        for (var i = 0; i < edit_links.length; i++) {
            edit_links[i].style.display = 'none';
        }
    }
    else {

        for (var i = 0; i < default_links.length; i++) {
            default_links[i].style.display = 'none';
        }
        for (var i = 0; i < delete_links.length; i++) {
            delete_links[i].style.display = 'none';
        }
        for (var i = 0; i < edit_links.length; i++) {
            edit_links[i].style.display = 'inline';
        }
    }
};



document.getElementById("delete").onclick = function () {
    if (delete_links[0].style.display == 'inline') {
        for (var i = 0; i < default_links.length; i++) {
            default_links[i].style.display = 'inline';
        }
        for (var i = 0; i < delete_links.length; i++) {
            delete_links[i].style.display = 'none';
        }
    }
    else {

        for (var i = 0; i < default_links.length; i++) {
            default_links[i].style.display = 'none';
        }
        for (var i = 0; i < edit_links.length; i++) {
            edit_links[i].style.display = 'none';
        }
        for (var i = 0; i < delete_links.length; i++) {
            delete_links[i].style.display = 'inline';
        }
    }
};

