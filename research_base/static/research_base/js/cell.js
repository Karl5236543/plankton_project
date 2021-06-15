mapboxgl.accessToken = 'pk.eyJ1IjoidmFsZW50aW41MjM2NTQzIiwiYSI6ImNrcDV4cnlhejB6YXYycXIydzRwd2NkbTIifQ.idvBgM2HIpy8s_ob1G8JWw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/satellite-v9',
    center: [-122.50923156738281,37.805986463750315],
    zoom: 7
});

map.addControl(new mapboxgl.NavigationControl());
