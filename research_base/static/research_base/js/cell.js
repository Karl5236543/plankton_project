mapboxgl.accessToken = 'pk.eyJ1IjoidmFsZW50aW41MjM2NTQzIiwiYSI6ImNrcDV4cnlhejB6YXYycXIydzRwd2NkbTIifQ.idvBgM2HIpy8s_ob1G8JWw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/satellite-v9',
    center: [-122.6981, 37.5478],
    zoom: 8
});

map.addControl(new mapboxgl.NavigationControl());

type_id = document.getElementById("type_id").value
map.on('load', function () {

    map.addSource('earthquakes', {
        type: 'geojson',
        data: 'http://localhost:8000/map/cell_data_json/' + type_id
    });
    map.addLayer({
        'id': 'earthquakes-layer',
        'type': 'circle',
        'source': 'earthquakes',
        "sort": ['get', 'title'],
        'paint': {
            'circle-radius': 20,
            'circle-stroke-width': 8,
            'circle-color': ['get', 'color'],
            'circle-stroke-color': ['get', 'color'],
            'circle-stroke-opacity': 0.5,
        },
        
    });

    map.addSource('points', {
        'type': 'geojson',
        'data': 'http://localhost:8000/map/cell_data_json/' + type_id
    });

    // Add a symbol layer
    map.addLayer({
        'id': 'points',
        'type': 'symbol',
        'source': 'points',
        'layout': {
            'icon-image': 'custom-marker',
            // get the title name from the source's "title" property
            'text-field': ['get', 'cell_type_count'],
            'text-font': [
                'Open Sans Semibold',
                'Arial Unicode MS Bold'
            ],
            //'text-offset': [0, 1.25],
            //'text-anchor': 'top'
        }
    });
});
