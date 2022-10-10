import os
import hashlib

def find_longest_word(ff):
    longest_word = ""
    for word_line in open(ff):
        for word in word_line.split():
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word
def find_all_longest_words(dir):
    a = {f : find_longest_word(os.path.join(dir,f))
        for f in os.listdir(dir)
        if os.path.isfile(os.path.join(dir,f))
    }    
    for key,value in a.items():        
        md = hashlib.md5(value.encode("utf-8")).hexdigest()        
        print(f"{key} : {md}")
# f = open("/Users/kyu-deokkim/Downloads/books/43-0.txt","r")
dirname = "/Users/kyu-deokkim/Downloads/books/"
if __name__ == "__main__":
    find_all_longest_words(dirname)
