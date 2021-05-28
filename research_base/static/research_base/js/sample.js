mapboxgl.accessToken = 'pk.eyJ1IjoidmFsZW50aW41MjM2NTQzIiwiYSI6ImNrcDV4cnlhejB6YXYycXIydzRwd2NkbTIifQ.idvBgM2HIpy8s_ob1G8JWw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-124.43115234375, 40.44694705960048],
    zoom: 5
});
/* 
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
}); */

table_container = document.getElementById("table_container")
create_form = document.getElementById("create_form")

edit_links = document.getElementsByClassName("edit_link")
delete_links = document.getElementsByClassName("delete_link")
default_links = document.getElementsByClassName("default_link")

add_btn = document.getElementById("add_btn")

delete_menu = document.getElementById("delete_menu")
delete_button = document.getElementById("delete_button")
back = document.getElementById("back")


for (var i = 0; i < edit_links.length; i++) {
    edit_links[i].onclick = function () {
        id = this.value
        edit_form = document.getElementById("edit_form_" + id)
        edit_form.style.display = 'block'
        table_container.style.display = 'none'
        add_btn.textContent = 'Изменить'

        url = 'http://localhost:8000/get_cell/' + id
        ajax_get(url, set_cell_params, id)

    }
}


document.getElementById("create").onclick = function () {
    create_form.style.display = 'block'
    table_container.style.display = 'none'
};

function ajax_get(url, callback, container_id) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            try {
                var data = JSON.parse(xmlhttp.responseText);
            } catch (err) {
                console.log(err.message + " in " + xmlhttp.responseText);
                return;
            }
            callback(data, container_id);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
};


function set_cell_params(cell, container_id) {
    edit_params_container = document.getElementById("edit_params_container_" + container_id)
    while (edit_params_container.firstChild) {
        edit_params_container.removeChild(edit_params_container.lastChild);
    }
    for (var i = 0; i < cell['params'].length; i++) {
        p = cell['params'][i]
        p_name = p["name"]
        p_value = p["value"]
        var div = document.createElement('div');
        div.innerHTML =  '<div class="mb-3 row"><div class="col-md-2 gx-0 param_label">'+ p_name +':</div><div class="col-md-10 gx-0"><input value="'+ p_value +'" type="number" class="form-control" name='+ p_name +'></div></div>'
        edit_params_container.append(div)
    }
};


function setparams(params, container_id) {
    container = document.getElementById(container_id)
    while (container.firstChild) {
        container.removeChild(container.lastChild);
    }
    for (var i = 0; i < params['params'].length; i++) {
        p = params['params'][i]
        var div = document.createElement('div');
        div.innerHTML =  '<div class="mb-3 row"><div class="col-md-2 gx-0 param_label">'+ p +':</div><div class="col-md-10 gx-0"><input type="number" class="form-control" name='+ p +' id="param_"'+ p +'></div></div>'
        container.append(div)
    }
}


document.getElementById("form_input").onchange = function () {
    id = this.value
    container_id = "params_container"
    url = 'http://localhost:8000/get_form_params/' + id
    ajax_get(url, setparams, container_id)
}

form_edit_input = document.getElementsByClassName("form_edit_input")
for (var i=0; i<form_edit_input.length; i++) {
    form_edit_input[i].onchange = function () {
        id = this.value
        container_id = this.id
        url = 'http://localhost:8000/get_form_params/' + id
        ajax_get(url, setparams, "edit_params_container_" + container_id)
    }
}

for (var i = 0; i < delete_links.length; i++) {
    delete_links[i].onclick = function () {
        id = this.value
        delete_menu.style.display = 'block'
        back.style.display = 'block'
        obj_name = delete_button.name
        delete_button.href = 'http://localhost:8000/' + obj_name + '_delete/' + id
    }

    document.getElementById("cancel_button").onclick = function () {
        back.style.display = 'none'
        delete_menu.style.display = 'none'
    }
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