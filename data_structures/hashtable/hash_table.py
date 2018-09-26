from .linkedlist import LinkedList


class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = []

    def __repr__(self):
        return f'Hashtable | Size: {self.table_size} |'

    def _hash_key(self, key):
        """Create a hash from a given key.
        args:
            key: a string to hash
        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """
        hashed = self._hash_key(key)
        values = self.get(key)
        if values == []:
            ll = LinkedList()
            ll.append(hashed)
            ll.append(value)
            self.hashtable.append(ll)
        else:
            for ll in self.hashtable:
                # import pdb; pdb.set_trace()
                if ll.head.val == hashed:
                    index = self.hashtable.index(ll)
                    selected_linkedlist = ll
                    selected_linkedlist.append(value)
                    self.hashtable[index] = selected_linkedlist
                    return

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        hashed = self._hash_key(key)
        for ll in self.hashtable:
            if ll.head.val == hashed:
                values = ll
        try:
            if values:
                pass
        except UnboundLocalError:
            return []

        output_values = []
        current = ll.head._next
        while current is not None:
            output_values.append(current.val)
            current = current._next
        return output_values

    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        hashed = self._hash_key(key)
        if self.get(key) == []:
            raise KeyError
        for ll in self.hashtable:
            if ll.head.val == hashed:
                index = self.hashtable.index(ll)
                self.hashtable[index] = None
                pass
