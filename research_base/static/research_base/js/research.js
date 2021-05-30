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

