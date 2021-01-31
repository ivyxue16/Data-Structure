class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        return key % self.size
    def rehash(self,oldhash):
        return (oldhash + 1) % self.size
    def put(self,key,data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else: 
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data # replace
    def get(self,key):
        startslot = self.hashfunction(key)
        position = startslot
        data = None
        while self.slots[position] != None:
            if self.slots[startslot] == key:
                return self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    break
        return data
