# import hashtable


def repeated_words(user_input):
    """ taks a string, return repeated word
    """
    ht = Hashtable()
    words = user_input.split()

    for word in words:
        hash = ht.hash(word.lower())
        if ht.get(hash):
            return word.lower()
        else:
            ht.set(hash, word.lower())
