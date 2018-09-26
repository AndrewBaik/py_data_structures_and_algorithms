from py_data_structures_and_algorithms.data_structures.hashtable.hash_table import HashTable


def repeated_words(user_input):
    """ taks a string, return repeated word
    """
    words = user_input.split()
    ht = HashTable()

    for word in words:
        if ht.get(word.lower()):
            return word.lower()
        else:
            ht.set(word.lower(), word.lower())
