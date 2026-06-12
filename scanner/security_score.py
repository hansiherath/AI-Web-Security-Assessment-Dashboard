def calculate_score(headers):

    score = 100

    penalties = {
        "High": 20,
        "Medium": 10,
        "Low": 5
    }

    for header, info in headers.items():

        if info["status"] == "Missing":

            score -= penalties.get(
                info["severity"],
                0
            )

    return max(score, 0)