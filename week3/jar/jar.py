class Jar:
    def __init__(self, capacity=12):
        # Capacity must be a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Represent the current contents as a row of cookie emoji
        return "🍪" * self.size

    def deposit(self, n):
        # Adding cookies must not exceed the jar's capacity
        if self.size + n > self.capacity:
            raise ValueError("Deposit would exceed capacity")
        self._size += n

    def withdraw(self, n):
        # Can't take out more cookies than are currently in the jar
        if n > self.size:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(2)
    print(f"Capacity: {jar.capacity}")
    print(f"Size: {jar.size}")
    print(f"Contents: {jar}")


if __name__ == "__main__":
    main()
