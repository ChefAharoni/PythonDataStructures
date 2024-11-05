class ArrayList:
    def __init__(self):
        self.capacity = 1  # Initial capacity
        self.size = 0  # Number of elements
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def append(self, item):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # Double capacity if full
        self.array[self.size] = item
        self.size += 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index out of bounds")

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"


# Example usage:
arr_list = ArrayList()
arr_list.append(1)
arr_list.append(2)
arr_list.append(3)
print(arr_list)  # Output: [1, 2, 3]
print(arr_list[1])  # Output: 2
print(len(arr_list))  # Output: 3
