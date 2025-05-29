
from stats import get_word_count
from stats import get_character_count_dict
from stats import get_sorted_dict

# import sys module, to have access to sys.argv and use argument when we call the bookbot program
import sys

#filepath = "books/frankenstein.txt"
try:
    filepath = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    # sys.exit(1) = abnormal termination   (0) would be normal
    sys.exit(1) 



def get_book_text(fp):
    # work WITH the provided "fp" file 
    with open(fp) as f:
        # return the text from the fp file as a string 
        return str(f.read())
    



def main():
    # book_text is the text of the whole book
    book_text = get_book_text(filepath)

    # word_count is the number of words in the book
    word_count = get_word_count(book_text)
    print (f"============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    print (f"----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print (f"--------- Character Count -------")

    # unsorted_dict    {'t': 29493, 'h': 19176, 'e': 44538, .... }
    unsorted_dict = get_character_count_dict(book_text)

    # sorted_dict is ordered list of dicts :
    # [{'char': 'ZZ', 'num': '11'}, {'char': '//', 'num': '22'}, {'char': 'XX', 'num': '33'}] 
    sorted_dicts_list = get_sorted_dict(unsorted_dict)

    # prints each dict:chara+number in sorted_dicts_list if chara is an alphabetical character 
    for i in range (0, len(sorted_dicts_list)):        
        if sorted_dicts_list[i]["char"].isalpha():
            print(f"{sorted_dicts_list[i]["char"]}: {sorted_dicts_list[i]["num"]}")

    print("============= END ===============")

    sys.exit(0) 




# Print the name of the script
#print("The script name is:", sys.argv)

#print("The first command line argument is :", sys.argv[0])
#print("The second command line argument is :", sys.argv[1])


if len(sys.argv) == 2:
    try:
        main()
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

