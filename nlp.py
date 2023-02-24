def choose_file():
    pass

# returns translated input
def translate(input_text, in_language_key, out_language_key):
    if in_language_key | out_language_key != "valid language":
        return False
    if in_language_key == out_language_key:
        return False
    if len(input_text) == 0:
        return False

# returns summary of input
def summary(input_text):
    if len(input_text) == 0:
        return False
    else:
        return True

# returns general sentiment of input
def sentiments(input_text):
    if len(input_text) == 0:
        return False
    else:
        return True

# returns if input contains searched for information
def search_file(keywords):
    if len(keywords) == 0:
        return False
    else:
        return True

# returns list of key words withing document and their definitions
def key_words(input_text):
    if len(input_text) == 0:
        return False
    else:
        return True
    return "List of key words withing document and their definitions"