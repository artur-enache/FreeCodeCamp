class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str) -> int:
        return sum(ord(char) for char in key)

    def add(self, key: str, value: str) -> None:
        key_hash = self.hash(key)
        if key_hash not in self.collection:
            self.collection[key_hash] = value
        else:
            if isinstance(self.collection[key_hash], dict):
                self.collection[key_hash].update(dict([(key, value)]))
            else:
                self.collection[key_hash] = dict([(key, value)])

    def remove(self, key: str) -> None:
        key_hash = self.hash(key)
        if key_hash in self.collection:
            del self.collection[key_hash]
        else:
            pass

    def lookup(self, key: str) -> str | None:
        key_hash = self.hash(key)
        return self.collection.get(key_hash)

def main():
    table = HashTable()
    table.add('dear', 'friend')
    print(table.collection)
    table.add('read', 'book')
    print(table.collection)
    table.add('arde', 'test')
    print(table.collection)
    table.add('golf', 'partner')
    table.remove('dear')
    print(table.collection)
    table.remove('reads')
    print(table.collection)
    table.remove('arde')
    print(table.collection)
    print(table.lookup('golf'))

if __name__ == '__main__':
    main()