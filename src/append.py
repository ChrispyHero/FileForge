

def add_newline(list: list[str]): 
    for i in range(0, len(list)): 
        list[i] = list[i] + "\n"
    return list


def append_list_to_textfile(text: list[str], filepath: str):
    with open(filepath, mode='a') as f:
        f.writelines(text) #TODO: find a way to add a new line automatically when appending text 
