import sys
sys.path.append('../../hashtable')
from hashtable import HashTable

def no_dups(s, dup_set = None):
    if dup_set is None:
        dup_set = set()

    ret = []

    for w in s.split(" "):
        if w not in dup_set:
            dup_set.add(w)
            ret.append(w)
            
    return " ".join(ret)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))