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
        ajax_get(url, set_cell_params, id, id)

    }
}


document.getElementById("create").onclick = function () {
    create_form.style.display = 'block'
    table_container.style.display = 'none'
};

function ajax_get(url, callback, container_V_id, container_P_id) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            try {
                var data = JSON.parse(xmlhttp.responseText);
            } catch (err) {
                console.log(err.message + " in " + xmlhttp.responseText);
                return;
            }
            callback(data, container_V_id, container_P_id);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
};


function set_cell_params(cell, container_V_id, container_P_id) {
    edit_params_V_container = document.getElementById("edit_params_V_container_" + container_V_id)
    while (edit_params_V_container.firstChild) {
        edit_params_V_container.removeChild(edit_params_V_container.lastChild);
    }
    edit_params_P_container = document.getElementById("edit_params_P_container_" + container_P_id)
    while (edit_params_P_container.firstChild) {
        edit_params_P_container.removeChild(edit_params_P_container.lastChild);
    }

    V_text = document.createElement('h6')
    V_text.innerHTML = "параметры для расчёта объема (V):<br>"
    edit_params_V_container.append(V_text)
    for (var i = 0; i < cell['params_V'].length; i++) {
        p = cell['params_V'][i]
        p_name = p["name"]
        p_value = p["value"]
        var div_V = document.createElement('div');
        div_V.innerHTML =  '<div class="mb-3 row"><div class="col-md-2 gx-0 param_label">'+ p_name +':</div><div class="col-md-10 gx-0"><input value="'+ p_value +'" type="number" class="form-control" name=V_'+ p_name +'></div></div>'
        edit_params_V_container.append(div_V)
    }
    P_text = document.createElement('h6')
    P_text.innerHTML = "параметры для расчёта площади поверхности (P):<br>"
    edit_params_P_container.append(P_text)
    for (var i = 0; i < cell['params_P'].length; i++) {
        p = cell['params_P'][i]
        p_name = p["name"]
        p_value = p["value"]
        var div_P = document.createElement('div');
        div_P.innerHTML =  '<div class="mb-3 row"><div class="col-md-2 gx-0 param_label">'+ p_name +':</div><div class="col-md-10 gx-0"><input value="'+ p_value +'" type="number" class="form-control" name=P_'+ p_name +'></div></div>'
        edit_params_P_container.append(div_P)
    }
};


function setparams(params, container_V_id, container_P_id) {
    console.log(container_V_id);
    console.log(container_P_id);
    container_V = document.getElementById(container_V_id)
    container_P = document.getElementById(container_P_id)
    while (container_V.firstChild) {
        container_V.removeChild(container_V.lastChild);
    }
    while (container_P.firstChild) {
        container_P.removeChild(container_P.lastChild);
    }
    V_text = document.createElement('h6')
    V_text.innerHTML = "параметры для расчёта объема (V):<br>"
    container_V.append(V_text)
    for (var i = 0; i < params['params_V'].length; i++) {
        p = params['params_V'][i]
        var div_V = document.createElement('div');
        div_V.innerHTML =  '<div class="mb-3 row"><div class="col-md-2 gx-0 param_label">'+ p +':</div><div class="col-md-10 gx-0"><input type="number" class="form-control" name=V_'+ p +' id="param_"'+ p +'></div></div>'
        container_V.append(div_V)
    }
    P_text = document.createElement('h6')
    P_text.innerHTML = "параметры для расчёта площади поверхности (P):<br>"
    container_P.append(P_text)
    for (var i = 0; i < params['params_P'].length; i++) {
        p = params['params_P'][i]
        var div_P = document.createElement('div');
        div_P.innerHTML =  '<div class="mb-3 row"><div class="col-md-2 gx-0 param_label">'+ p +':</div><div class="col-md-10 gx-0"><input type="number" class="form-control" name=P_'+ p +' id="param_"'+ p +'></div></div>'
        container_P.append(div_P)
    }
}


document.getElementById("form_input").onchange = function () {
    id = this.value
    container_V_id = "params_V_container"
    container_P_id = "params_P_container"
    url = 'http://localhost:8000/get_form_params/' + id
    ajax_get(url, setparams, container_V_id, container_P_id)
}

form_edit_input = document.getElementsByClassName("form_edit_input")
for (var i=0; i<form_edit_input.length; i++) {
    form_edit_input[i].onchange = function () {
        id = this.value
        container_id = this.id
        url = 'http://localhost:8000/get_form_params/' + id
        ajax_get(url, setparams, "edit_params_V_container_" + container_id, "edit_params_P_container_" + container_id)
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