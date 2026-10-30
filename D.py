class HashTable:
    def __init__(self):
        self.capacity = 8
        self.count = 0
        self.buckets = [] 
        for i in range(self.capacity):
            self.buckets.append([])

    def _get_index(self, key):
        h = 0
        for ch in key:
            h = h * 31 + ord(ch)
        return h % self.capacity

    def put(self, key, value):
        idx = self._get_index(key)
        bucket = self.buckets[idx]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                return

        bucket.append([key, value])
        self.count += 1

        if self.count > self.capacity * 0.75:
            self.resize()

    def get(self, key):
        idx = self._get_index(key)
        bucket = self.buckets[idx]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
                
        return None

    def delete(self, key):
        idx = self._get_index(key)
        bucket = self.buckets[idx]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                val = bucket[i][1]
                bucket.pop(i)
                self.count -= 1
                return val
                
        return None

    def size(self):
        return self.count

    def resize(self):
        old_buckets = self.buckets
        
        self.capacity = self.capacity * 2
        self.buckets = []
        for i in range(self.capacity):
            self.buckets.append([])
        
        for bucket in old_buckets:
            for pair in bucket:
                key = pair[0]
                value = pair[1]
                idx = self._get_index(key)
                self.buckets[idx].append([key, value])


q = int(input())
data = [input().split() for i in range(q)]

table = HashTable()
res = []

for parts in data:
    cmd = parts[0]
    if cmd == 'put':
        table.put(parts[1], int(parts[2]))
    elif cmd == 'get':
        val = table.get(parts[1])
        res.append('Error' if val is None else str(val))
    elif cmd == 'del':
        val = table.delete(parts[1])
        res.append('Error' if val is None else str(val))
    elif cmd == 'size':
        res.append(str(table.size()))

print('\n'.join(res))