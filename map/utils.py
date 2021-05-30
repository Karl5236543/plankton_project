from research_base.models import Station, Cell

def get_stations_json(res_id=None, st_id=None):
    stations = {
        "type": "FeatureCollection",
        "features": []
    }
    station_list = Station.objects.all()
    for station in station_list:
        if res_id:
            point_color = 'blue' if station.research_id == res_id else 'grey'
        elif st_id:
            point_color = 'red' if station.id == st_id else 'grey'
        else:
            point_color = 'blue'
        stations["features"].append({
            "type": "Feature",
            "properties": {
                "color":  point_color,
                "title": station.samples.count(),
                "name": station.name,
                "depth": station.depth,
                "date": station.date,
                "url": station.get_absolute_url(),
                "research": station.research.name,
                "research_url": station.research.get_absolute_url(),
                "create_time": station.create_time,
            },
            "geometry": {
                "type": "Point",
                "coordinates": station.coords
            }
        })
    return stations


def get_cells_data_json(type_id):
    json_data = {
        "type": "FeatureCollection",
        "features": []
    }

    st_cell_count_list = []
    for st in Station.objects.all():
        st_cell_count_list += [sample.get_cell_count_with_type(type_id=type_id) for sample in st.samples.all()]

    max_cell_count = max(st_cell_count_list)
    min_cell_count = min(st_cell_count_list)

    stations = Station.objects.all()
    for station in stations:
        cell_count = sum(sample.get_cell_count_with_type(type_id) for sample in station.samples.all())
        json_data["features"].append({
            "type": "Feature",
            "properties": {
                "color":  __get_color(min_cell_count, max_cell_count, cell_count),
                "cell_type_count": cell_count,
                "title": station.samples.count(),
                "name": station.name,
                "depth": station.depth,
                "date": station.date,
                "url": station.get_absolute_url(),
                "research": station.research.name,
                "research_url": station.research.get_absolute_url(),
                "create_time": station.create_time,
            },
            "geometry": {
                "type": "Point",
                "coordinates": station.coords
            }
        })
    return json_data


def __get_color(start, stop, value):
    if not value:
        return "#878787"
    collor_range = ["#34D800", "#95EC00", "#D2F700", "#FFF800", "#FFDA00", "#FFBF00", "#FFA500", "#FF8700", "FF5F00", "#FF1E00"]
    step = int((stop - start) / len(collor_range))
    for index, section in enumerate(range(start, stop, step)):
        if section <= value <= section + step or index == 9:
            return collor_range[index]
