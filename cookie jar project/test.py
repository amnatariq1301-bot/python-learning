class jar:
    def __init__(self, capacity = 12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size
    
    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("must deposit a positive integer of cookies")
        if self._size + n > self._capacity:
            raise ValueError("Exceeded cookie jar capacity")
        self._size+=n
    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Must withdraw a positive integer of cookies")
        if self._size - n < 0:
            raise ValueError("jar does not contain enough cookies")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

       
       
       

    