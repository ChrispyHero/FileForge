import json
from pathlib import Path


def load_data_from_json(file_path:str):
    """
    Returns the json parsed from a json file
    """
    try: 
        with open(file_path) as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError as e: 
        print(f"There is a problem with the json file: {e}")

    
def load_path_from_json_file(json_data, path:str): 
    data_dict = dict(json_data) 
    target_path = data_dict.get(path, None)
    if target_path is None: 
        raise KeyError
    return target_path


def load_target_file_path():
    """
    Gets the the file path from the json file where the user input will be appended to. 
    """
    abs_path = Path(__file__).resolve()
    json_data_path = abs_path.parents[1] / "data.json" # parents[1] is the root folder of this repo
    json_data = load_data_from_json(str(json_data_path))
    target_file_path = load_path_from_json_file(json_data, path="target_file_path")

    return target_file_path