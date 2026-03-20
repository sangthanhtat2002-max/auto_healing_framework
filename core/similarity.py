from difflib import SequenceMatcher

def text_similarity(a, b):
    if not a or not b:
        return 0
    return SequenceMatcher(None, str(a), str(b)).ratio()


def compute_score(element, target_value):
    score = 0

    text = element.get_text(strip=True)

    # text similarity
    score += text_similarity(target_value, text) * 2

    # attribute similarity
    attrs = element.attrs

    for attr in ["id", "name", "placeholder", "class"]:
        if attr in attrs:
            score += text_similarity(target_value, str(attrs[attr])) * 3

    # tag bonus
    if element.name in ["input", "button"]:
        score += 1

    return score