import pathlib
from bs4 import BeautifulSoup


def test_nav_list_items_count():
    html_path = pathlib.Path(__file__).resolve().parents[1] / "Com-M5.copyweb" / "index.html"
    html = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    nav_ul = soup.find("nav").find("ul")
    assert nav_ul is not None, "Navigation list not found"
    items = nav_ul.find_all("li")
    assert len(items) == 6

