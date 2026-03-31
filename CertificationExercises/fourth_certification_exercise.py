"""https://www.freecodecamp.org/learn/python-v9/lab-hash-table/build-a-hash-table"""

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key: str) -> int:
        return sum(ord(char) for char in key)

    def add(self, key: str, value: str) -> None:
        key_hash = self.hash(key)
        if key_hash not in self.collection:
            self.collection[key_hash] = {key: value}
        else:
            self.collection[key_hash].update({key: value})

    def remove(self, key: str) -> None:
        key_hash = self.hash(key)
        try:
            del self.collection[key_hash][key]
        except KeyError:
            pass

    def lookup(self, key: str) -> str | None:
        key_hash = self.hash(key)
        try:
            return self.collection[key_hash].get(key, None)
        except KeyError:
            return None

def main():
    table = HashTable()
    table.add('dear', 'friend')
    table.add('read', 'book')
    table.add('arde', 'test')
    table.add('golf', 'partner')
    print(table.collection)
    table.remove('dera')
    print(table.collection)
    print(table.lookup('golf'))
    print(table.lookup('lgof'))
    print(table.lookup('lgofe'))

if __name__ == '__main__':
    main()