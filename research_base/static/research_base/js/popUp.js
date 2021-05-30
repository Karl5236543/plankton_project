function build_description(feature) {
    return "<table class='table'>"+
    "<tbody>"+
    "<tr>"+
    "<td> имя: </td>"+
    "<td><a href="+ feature.properties.url +">"+ feature.properties.name +"</a></td>"+
    "</tr>"+
    "<tr>"+
    "<td> координаты: </td>"+
    "<td>"+ feature.geometry.coordinates +"</td>"+
    "</tr>"+
    "<tr>"+
    "<td> дата прибытия: </td>"+
    "<td>"+ feature.properties.date +"</td>"+
    "</tr>"+
    "<tr>"+
    "<td> глубина: </td>"+
    "<td>"+ feature.properties.depth +"</td>"+
    "</tr>"+
    "<tr>"+
    "<td> количество образцов: </td>"+
    "<td>"+ feature.properties.title +"</td>"+
    "</tr>"+
    "<tr>"+
    "<td> исследование: </td>"+
    "<td><a href="+ feature.properties.research_url +">"+ feature.properties.research +"</a></td>"+
    "</tr>"+
    "<tr>"+
    "<td> время создания: </td>"+
    "<td>"+ feature.properties.create_time +"</td>"+
    "</tr>"+
    "<tr>"+
    "</tbody>"+
    "</table>"
}

map.on('click', 'earthquakes-layer', function (e) {
    var coordinates = e.features[0].geometry.coordinates.slice();
    console.log(build_description(e.features[0]));
    var description = build_description(e.features[0]);

    // Ensure that if the map is zoomed out such that multiple
    // copies of the feature are visible, the popup appears
    // over the copy being pointed to.
    while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
        coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
    }

    new mapboxgl.Popup()
        .setLngLat(coordinates)
        .setHTML(description)
        .addTo(map);
});

// Change the cursor to a pointer when the mouse is over the places layer.
map.on('mouseenter', 'earthquakes-layer', function () {
    map.getCanvas().style.cursor = 'pointer';
});

// Change it back to a pointer when it leaves.
map.on('mouseleave', 'earthquakes-layer', function () {
    map.getCanvas().style.cursor = '';
});