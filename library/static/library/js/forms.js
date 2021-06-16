buttons = document.getElementsByClassName("show_description_btn")
for(var i=0; i<buttons.length; i++) {
    buttons[i].onclick = function() {
        description_container = document.getElementById("description_container_" + this.value)
        if (description_container.style.display == "table-row") {
            this.classList.add("btn-success");
            this.classList.remove("btn-outline-success")
            description_container.style.display = "none"
        }
        else {
            this.classList.add("btn-outline-success")
            this.classList.remove("btn-success");
            description_container.style.display = "table-row"
        }
    }
}

edit_type_forms = document.getElementsByClassName("edit_form_form")

edit_links = document.getElementsByClassName("edit_btn")
delete_links = document.getElementsByClassName("delete_btn")
default_links = document.getElementsByClassName("show_description_btn")

delete_button = document.getElementById("delete_button")

create_form = document.getElementById("create_form_form")

document.getElementById("create").onclick = function () {
    for(var i=0; i<edit_type_forms.length; i++) {
        edit_type_forms[i].style.display = 'none'
    }

    if (create_form.style.display == 'block') {
        create_form.style.display = 'none'
    } else {
        create_form.style.display = 'block'
    }

};

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

for (var i = 0; i < edit_links.length; i++) {
    edit_links[i].onclick = function () {
        create_form.style.display = 'none'
        for(var i=0; i<edit_type_forms.length; i++) {
            edit_type_forms[i].style.display = 'none'
        }
        id = this.value
        edit_form = document.getElementById("edit_form_form_" + id)
        edit_form.style.display = 'block'
    }
}

for (var i = 0; i < delete_links.length; i++) {
    delete_links[i].onclick = function () {
        id = this.value
        delete_menu.style.display = 'block'
        back.style.display = 'block'
        delete_button.href = 'http://localhost:8000/library/delete_form/' + id
    }

    document.getElementById("cancel_button").onclick = function () {
        back.style.display = 'none'
        delete_menu.style.display = 'none'
    }
}