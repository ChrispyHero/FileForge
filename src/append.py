
# Takes list as a parameter because the program stores parameters for "-q" in a list
def _add_newline(text: list[str]): 
    for i in range(0, len(text)): 
        text[i] = text[i] + "\n"
    return text


def append_list_to_textfile(text: list[str], filepath: str):
    text_new = _add_newline(text)
    try:
        with open(filepath, mode='a') as f:
            f.writelines(text_new)  
    except FileNotFoundError as e: 
        print(f"There is a problem with the json file: {e}")
