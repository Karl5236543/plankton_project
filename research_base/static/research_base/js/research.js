research_id = document.getElementById("research_id").value

map.on('load', function () {
    map.addSource('earthquakes', {
        type: 'geojson',
        data: 'http://localhost:8000/map/research_stations_json/' + research_id
    });
    map.addLayer({
        'id': 'earthquakes-layer',
        'type': 'circle',
        'source': 'earthquakes',
        'paint': {
            'circle-radius': 10,
            'circle-stroke-width': 2,
            'circle-color': ['get', 'color'],
            'circle-stroke-color': 'white',
        }
    });
});

function onDragEnd() {
    var lngLat = marker.getLngLat();
    document.getElementById("lat").value = lngLat.lat
    document.getElementById("lng").value = lngLat.lng
}



var marker;
function add_draggable_marker() {
    coords = map.getCenter()
    marker = new mapboxgl.Marker({
        draggable: true
    })
        .setLngLat([coords.lng, coords.lat])
        .addTo(map)
        .on('dragend', onDragEnd);
}

document.getElementById("set_coords").onclick = function () {
    if (this.classList.contains('active')) {
        this.classList.remove("active")
        marker.remove();
    }
    else {
        this.classList.add("active")
        add_draggable_marker();
    }
}