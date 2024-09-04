def get_num_pages(html):
    """
    Finds the number of pages that must be iterated over

    :param html: html contents of the page
    :return: number of pages
    """

    num_start = html.rfind("/page/") + 6
    num_end = num_start + html[num_start:].find("/")
    try:
        return int(html[num_start:num_end])
    except ValueError:
        return 1

def get_film_name_from_list_page(html, film):
    """
    Returns the name of a film

    :param html: html contents of page with films
    :param film: re iter of each film entry on a page
    :return: name of a film
    """
    start = film.start() + html[film.start():].find("alt=\"") + 5
    end = start + html[start:].find("\"")
    return html[start:end]

def get_film_url_from_list_page(html, film):
    """
    Returns the extension of a url needed to ping the actual page of an individual film

    :param html: html contents of page with films
    :param film: re iter of each film entry on a page
    :return: url ending of a film page
    """
    start = film.start() + html[film.start():].find("data-film-slug") + 16
    end = start + html[start:].find("\"")
    return "film/" + html[start:end] + "/"