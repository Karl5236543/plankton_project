
map.on('load', function () {
    map.addSource('earthquakes', {
        type: 'geojson',
        data: 'http://localhost:8000/map/stations_json'
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