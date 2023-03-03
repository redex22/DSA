MAX_HASH_TABLE_SIZE = 4096


class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        # Use Python's in-built `hash` function and implement linear probing
        index = hash(key) % len(self.data_list)
        while True:
            # Get the key-value pair stored at idx
            key_value = self.data_list[index]

            # If it is None, return the index
            if not key_value:
                return index

            k, val = key_value
            # If the stored key matches the given key, return the index
            if k == key:
                return index

            # Move to the next index
            index += 1

            # Go back to the start if you have reached the end of the array
            if index == len(self.data_list):
                index = 0

    def __getitem__(self, key):
        index = self.get_valid_index(key)
        k, val = self.data_list[index]
        return val if k else None

    def __setitem__(self, key, value):
        index = self.get_valid_index(key)
        self.data_list[index] = (key, value)

    def __iter__(self):
        return (x for x in self.data_list if x is not None)

    def __len__(self):
        return len([x for x in self])

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    # Create a hash table
    table = HashTable()

    # Insert some key-value pairs
    table['a'] = 1
    table['b'] = 34

    # Retrieve the inserted values
    print(table['a'] == 1 and table['b'] == 34)

    # Update a value
    table['a'] = 99

    # Check the updated value
    print(table['a'] == 99)

    # Get a list of key-value pairs
    print((list(table) == [('a', 99), ('b', 34)]))

    print(table)
