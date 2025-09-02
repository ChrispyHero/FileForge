

def _add_newline(text: list[str]): 
    for i in range(0, len(text)): 
        text[i] = text[i] + "\n"
    return text


def append_list_to_textfile(text: list[str], filepath: str):
    """
    Takes list as a parameter because the program stores everything in a list,
    even if the user only inputs one line of text
    Improving reusability of this function
    """
    text_new = _add_newline(text)
    try:
        with open(filepath, mode='a') as f:
            f.writelines(text_new)  
    except FileNotFoundError as e: 
        print(f"There is a problem with the file: {e}")
