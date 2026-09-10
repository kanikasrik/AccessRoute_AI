def detect_risks(route):
    risks = []

    if route["stairs"]:
        risks.append("Stairs present")

    if not route["elevator"]:
        risks.append("Elevator unavailable")

    if not route["accessible_path"]:
        risks.append("Accessible path unavailable")

    if route["walking_distance"] > 2:
        risks.append("Long walking distance")

    if route["obstacles"]:
        risks.append("Obstacles detected")

    if len(risks) == 0:
        return ["No major accessibility risks"]

    return risks