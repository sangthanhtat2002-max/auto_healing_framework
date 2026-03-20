from core.dom_parser import get_dom_elements
from core.similarity import compute_score
from utils.logger import log

class Healer:

    def __init__(self, driver):
        self.driver = driver  # đây là HealedDriver

    def heal(self, by, value):
        log(f"Healing locator: {by}={value}")

        # 1. lấy toàn bộ DOM
        elements = get_dom_elements(self.driver.driver)

        scored = []

        # 2. chấm điểm từng element
        for el in elements:
            score = compute_score(el, value)
            scored.append((score, el))

        # 3. sort theo score
        scored.sort(key=lambda x: x[0], reverse=True)

        best_score, best_element = scored[0]

        log(f"Best score: {best_score}")

        if best_score < 0.5:
            raise Exception("Healing failed: low confidence")

        # 4. build xpath từ element
        xpath = self._build_xpath(best_element)

        log(f"Healed XPath: {xpath}")

        # 5. QUAN TRỌNG: dùng selenium driver thật
        return self.driver.driver.find_element("xpath", xpath)

    def _build_xpath(self, element):
        tag = element.name

        if element.get("id"):
            return f"//{tag}[@id='{element.get('id')}']"

        if element.get("name"):
            return f"//{tag}[@name='{element.get('name')}']"

        return f"//{tag}"