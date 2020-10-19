import requests


def test_html():
    url = "https://www.google.hr/"
    html_page = requests.get(url).text

    assert type(html_page) == str
