mapboxgl.accessToken = 'pk.eyJ1IjoidmFsZW50aW41MjM2NTQzIiwiYSI6ImNrcDV4cnlhejB6YXYycXIydzRwd2NkbTIifQ.idvBgM2HIpy8s_ob1G8JWw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/satellite-v9',
    center: [-122.50923156738281, 37.805986463750315],
    zoom: 7
});

map.addControl(new mapboxgl.NavigationControl());

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
    }
}


document.getElementById("create").onclick = function () {
    create_form.style.display = 'block'
    table_container.style.display = 'none'
    console.log(table_container.style.display);

};

edit_form_return_btn_list = document.getElementsByClassName("edit_form_return_btn")
for (var i = 0; i < edit_form_return_btn_list.length; i++) {
    edit_form_return_btn_list[i].onclick = function () {
        location.reload()
    }

}

document.getElementsByClassName("create_form_return_btn")[0].onclick = function () {
    location.reload()
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