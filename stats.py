def get_num_words(file_path):
    try:
        with open(file_path) as f:
            contents=f.read()
            num_words=len(contents.split())

        return num_words
    except FileNotFoundError:
        raise FileNotFoundError("file not found")
def get_char_count(file_path):
    count = {}
    
    with open(file_path) as n:
        f = n.read()
        clean_string = f.replace(" ", "").lower()
    for letter in clean_string:
        if letter.isalpha():
            if letter in count:
                count[letter] += 1
            else: 
                count[letter] = 1

    char_list = []
    for char, nums in count.items():
        char_list.append({"char": char, "num": nums})

    char_list.sort(reverse=True, key=lambda count: count["num"])          
    

    return char_list


