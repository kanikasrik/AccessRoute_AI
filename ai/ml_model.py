def predict_route_quality(route):
    score = 100

    if route["stairs"]:
        score -= 30

    if not route["elevator"]:
        score -= 20

    if not route["accessible_path"]:
        score -= 25

    if route["walking_distance"] > 2:
        score -= 15

    if route["obstacles"]:
        score -= 20

    score = max(0, min(score, 100))

    if score >= 80:
        recommendation = "Highly Accessible"
    elif score >= 60:
        recommendation = "Moderately Accessible"
    elif score >= 40:
        recommendation = "Less Accessible"
    else:
        recommendation = "Not Recommended"

    return {
        "score": score,
        "recommendation": recommendation
    }