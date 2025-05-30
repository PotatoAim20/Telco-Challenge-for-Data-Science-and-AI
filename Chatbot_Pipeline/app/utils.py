def merge_json(original, updates):
    for k, v in updates.items():
        if v is not None:
            original[k] = v
    return original

def get_missing_fields_json(json_data):
    missing_fields = {k: v for k, v in json_data.items() if v is None}
    return missing_fields