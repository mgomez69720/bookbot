

def get_word_count(whole_text):
    wcount = 0
    for word in whole_text.split():
        wcount += 1
    return wcount



def get_character_count(text):
    ccount = {}
    for chara in text :
        if chara.lower() in ccount:
            ccount[chara.lower()] += 1
        else:
            ccount[chara.lower()] = 1
            print(f"<<<< Initialize {chara.lower()}")
    return ccount




