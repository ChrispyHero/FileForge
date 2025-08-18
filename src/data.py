import json


def load_data_from_json(file_path:str):
    with open(file_path) as file:
        data = json.load(file)
    return data

