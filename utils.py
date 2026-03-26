def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path and path[0] == start:
        return path
    return []
def generate_google_maps_link(start, end):
    base_url = "https://www.google.com/maps/dir/"
    start = start.replace(" ", "+")
    end = end.replace(" ", "+")
    return base_url + start + "/" + end