from allure import tag

from core.dom_parser import get_dom_elements
from core.similarity import compute_score
from utils.logger import log

class Healer:

    def __init__(self, driver):
        self.driver = driver  # đây là HealedDriver

    def heal(self, by, value):
        log(f"Healing locator: {by}={value}")

        # 1. lấy toàn bộ DOM
        elements = get_dom_elements(self.driver)

        scored = []

        # 2. chấm điểm từng element
        for el in elements:
            tag = el.name.lower()

            # 🔥 CHỈ LẤY ELEMENT CÓ THỂ INTERACT
            if tag not in ["input", "textarea", "button", "a", "div", "span"]:
                continue

            score = compute_score(el, value)
            scored.append((score, el))

        if not scored:
            raise Exception("No valid elements found for healing")

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
        element = self.driver.find_element("xpath", xpath)

        # 🔥 VALIDATE
        tag = element.tag_name.lower()

        if not element.is_displayed() or not element.is_enabled():
            raise Exception(f"[HEALING] Element not interactable: {xpath}")

        if tag not in ["input", "textarea"]:
            raise Exception(f"[HEALING] Invalid tag: {tag}")

        return element

    def _build_xpath(self, element):
        tag = element.name

        if element.get("id"):
            return f"//{tag}[@id='{element.get('id')}']"

        if element.get("name"):
            return f"//{tag}[@name='{element.get('name')}']"

        def _build_xpath(self, element):
            tag = element.name

            if element.get("id"):
                return f"//{tag}[@id='{element.get('id')}']"

            if element.get("name"):
                return f"//{tag}[@name='{element.get('name')}']"

            if element.get("placeholder"):
                return f"//{tag}[@placeholder='{element.get('placeholder')}']"

    # fallback nhưng vẫn hạn chế
        return f"(//{tag})[1]"