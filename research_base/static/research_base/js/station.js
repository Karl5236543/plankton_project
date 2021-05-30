station_id = document.getElementById("station_id").value
station_coords = document.getElementById("station_coords").value
map.on('load', function () {
    map.addSource('earthquakes', {
        type: 'geojson',
        data: 'http://localhost:8000/map/station_json/' + station_id
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
    map.flyTo({center: JSON.parse(station_coords), zoom: 10});
});
