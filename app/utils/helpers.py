from datetime import datetime, timezone

def process_response(data: dict):
    gender = data.get("gender")
    probability = data.get("probability", 0)
    count = data.get("count", 0)

    is_confident = probability >= 0.7 and count >= 100

    return {
        "name": data.get("name"),
        "gender": gender,
        "probability": probability,
        "sample_size": count,
        "is_confident": is_confident,
        "processed_at": datetime.now(timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
    }
