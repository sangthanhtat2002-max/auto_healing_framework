from bs4 import BeautifulSoup

def get_dom_elements(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    elements = []

    for tag in soup.find_all(True):
        elements.append(tag)

    return elements