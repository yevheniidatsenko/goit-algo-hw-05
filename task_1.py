class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return

    def __contains__(self, key):
        return self.get(key) is not None

    def __str__(self):
        items = []
        for bucket in self.table:
            for pair in bucket:
                items.append(f"{pair[0]}: {pair[1]}")
        return "\n".join(items)


# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("Вся таблиця до видалення елемента:\n", H)
print(H.get("apple"))  # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30

H.delete("orange")

print("Вся таблиця після видалення елемента:\n", H)
print(H.get("orange"))  # Виведе: None