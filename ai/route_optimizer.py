from accessibility_score import calculate_accessibility_score
from risk_detection import detect_risks
from ml_model import predict_route_quality


def find_best_route(routes):
    best_route = None
    best_score = -1

    for route in routes:
        score = calculate_accessibility_score(route)
        risks = detect_risks(route)
        prediction = predict_route_quality(route)

        route["accessibility_score"] = score
        route["risks"] = risks
        route["recommendation"] = prediction["recommendation"]

        if score > best_score:
            best_score = score
            best_route = route

    return best_route