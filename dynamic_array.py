class DynamicArray:
    def __init__(self, initial_capacity=10, resize_factor=2):
        self.__array = [None] * initial_capacity
        self.__size = 0
        self.__capacity = initial_capacity
        self.__resize_factor = resize_factor

    def insert(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert_at_index(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(self.capacity * self.resize_factor)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0


    def reverse(self):
        for i in range(self.size): 
            for j in range(self.size - 1, i, -1):
                self.array[i], self.array[j] = self.array[j], self.array[i]

    def append(self, element):
        if self.size == self.capacity:
            self._resize(self.capacity * self.resize_factor)
        self.array[self.size] = element
        self.size += 1

    def prepend(self, element):
        self.insert_at_index(0, element)


    def middle_element(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, element):
        for i in range(self.size):  
            for j in range(i): 
                if self.array[j] == element: 
                    return j
        return -1



