
# returns the number of words in the text
def get_word_count(whole_text):
    wcount = 0
    for word in whole_text.split():
        wcount += 1
    return wcount


# returns a dict of every chara + their number in the text : 
# {'t': 29493, 'h': 19176, 'e': 44538, .... }
def get_character_count_dict(text):
    ccount = {}
    for chara in text :
        # .lower so we don't have duplicates between uper and lower cases 
        if chara.lower() in ccount:
            ccount[chara.lower()] += 1
        else:
            ccount[chara.lower()] = 1
    return ccount



# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on_num(dict):
    return dict["num"]



# takes an unsorted dict and returns a sorted list of dicts of every chara + their number
# unsorted dict :  {'t': 29493, 'h': 19176, 'e': 44538, .... }
def get_sorted_dict (unsorted_dict):

    sorted_dicts_list = []

    for key in unsorted_dict:
        udic = {"char": key, "num": unsorted_dict[key]}
        sorted_dicts_list.append(udic)

    # sorts the list of dicts from higher to lower "num" 
    # [{'char': 'ZZ', 'num': '11'}, {'char': '//', 'num': '22'}, {'char': 'XX', 'num': '33'}] 
    sorted_dicts_list.sort(reverse=True, key=sort_on_num)   

    return sorted_dicts_list

















