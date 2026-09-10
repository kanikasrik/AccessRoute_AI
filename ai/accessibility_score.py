def calculate_accessibility_score(route):
    score = 100

    if route["stairs"]:
        score -= 30

    if not route["elevator"]:
        score -= 20

    if route["accessible_path"]:
        score += 10
    else:
        score -= 25

    if route["walking_distance"] > 2:
        score -= 15

    if route["obstacles"]:
        score -= 20

    score = max(0, min(score, 100))

    return score