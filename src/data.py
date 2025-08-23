import json
import sys

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
    
def load_target_file_path(json_data): 
    data_dict = dict(json_data) 
    target_path = data_dict.get("target_file_path", None)
    if target_path is None: 
        raise KeyError
    return target_path
        