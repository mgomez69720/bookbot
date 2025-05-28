
from stats import get_word_count



filepath = "books/frankenstein.txt"

def get_book_text(fp):
    #print(f">>>>>>>>>>>>> running get_book_text : {fp}")
    with open(fp) as f:
        #print(">>>>>>>>>>>>> with open filepath")
        return str(f.read())
    
def get_word_count(whole_text):
    wcount = 0
    for word in whole_text.split():
        wcount += 1
    return wcount


def main():
    book_text = get_book_text(filepath)
    #print (f"{book_text}")
    word_count = get_word_count(book_text)
    print (f"{word_count} words found in the document")


main()