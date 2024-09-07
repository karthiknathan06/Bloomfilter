import hashlib

# bloom filter entity
class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def add(self, item):
        for i in range(self.hash_count):
            digest = self.hash_item(item, i)
            index = digest % self.size
            self.bit_array[index] = 1

    def check(self, item):
        for i in range(self.hash_count):
            digest = self.hash_item(item, i)
            index = digest % self.size
            if self.bit_array[index] == 0:
                return False
        return True

    def hash_item(self, item, seed):
        hash_result = hashlib.md5(item.encode())
        hash_result.update(str(seed).encode())
        return int(hash_result.hexdigest(), 16)

# Passing bucket size as 1000, passing 5 hashfunctions which results in 5 indices for single insertion
bloom = BloomFilter(size=1000, hash_count=5)

# Inserting into the bucket
bloom.add("Karthik")
bloom.add("Arun")
bloom.add("Kalai")

# Output: True
print(bloom.check("Arun"))  
# Output: False
print(bloom.check("Michael")) 

