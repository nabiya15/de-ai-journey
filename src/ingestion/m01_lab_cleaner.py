raw_data = [
    {"id": 1, "temp": 22.5, "status": "ok"},
    {"id": 2, "temp": None, "status": "error"},
    {"id": 3, "temp": "31.2", "status": "OK"}, # String instead of float
    {"id": 4, "temp": 105.0, "status": "ok"}, # Outlier: too high!
]
def clean_data(raw_data):
    clean_list = []
    for row in raw_data:
        temp = row.get('temp')
        # 1. Skip rows where temp is None
        if temp is None:
            continue
        # 2. Convert string temps to floats
        if isinstance(temp, str):
            try:
                temp = float(temp)
            except ValueError:
                continue  # Skip if temp can't be converted to float
        # 3. Filter out temps above 100 as outliers
        if temp > 100:
            continue
        # 4. Upper-case all status codes
        status = row.get('status', '').upper()
        clean_list.append({'id': row.get('id'), 'temp': temp, 'status': status})
    return clean_list

clean_list = clean_data(raw_data)
print(clean_list)
