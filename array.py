class Array:
    def __init__(self, length, dataType):
        self.length = length
        self.ar = [''for i in range(length)]
        self.dataType = dataType
    def append(self, item):
        if type(item) != self.dataType:
            raise TypeError('You cannot append ' + str(type(item)) + ' to this array.')
        for i in range(self.length):
            if self.ar[i]=='':
                self.ar[i] = item
                return
        raise IndexError('Cannot append item to full array.')
    def set(self, item, pos):
        if not(0<=pos<self.length):
            raise IndexError('Array index out of range.')
        if type(item) != self.dataType:
            raise TypeError('You cannot append ' + str(type(item)) + ' to this array.')
        self.ar[pos] = item
    def get(self, pos):
        if not(0<=pos<self.length):
            raise IndexError('Array index out of range.')
        if self.ar[pos] == '':
            return None
        return self.ar[pos]
    def remove(self, pos):
        if not(0<=pos<self.length):
            raise IndexError('Array index out of range.')
        self.ar[pos] = ''
    def delete(self, item):
        if not(item in self.ar):
            raise ValueError('Item not in array.')
        self.ar[self.ar.index(item)] = ''
    def addList(self, l):
        for item in l:
            if type(l) != self.dataType:
                raise TypeError('You cannot append ' + str(type(item)) + ' to this array.')
        spaces = 0
        for item in self.ar:
            if item=='':
                spaces+=1
        if len(l)>spaces:
            raise ValueError('List too long to append to array.')
        for item in l:
            self.append(item)
    def addToEnd(self, item):
        x = 0
        for i in range(self.length-1, -1, -1):
            if self.ar[i]!='':
                x=i
        self.ar[x]=item
    def __str__(self):
        arrayToPrint = '['
        for i in range(self.length):
            if self.ar[i] == '':
                arrayToPrint += 'None'
            elif self.dataType == str:
                arrayToPrint+='\'' + self.ar[i] + '\''
            elif self.dataType == int or self.dataType == float:
                arrayToPrint += str(self.ar[i])
            if i != (self.length-1):
                    arrayToPrint+=', '
        arrayToPrint+=']'
        return arrayToPrint
    def __getitem__(self, pos):
        if not(0<=pos<self.length):
            raise IndexError('Array index out of range.')
        if self.ar[pos] == '':
            return None
        return self.ar[pos]


#   USAGE

# Declaring the Array
# a = Array(length, dataType)
# eg a = Array(5, int)

# Array Methods
# a.get(5) will return the item in index 5, None if empty.
# a[5] will return the item in index 5, None if empty.
# a.set('hello', 3) will put the string 'hello' into index 3, provided the array is long enough and supports strings.
# a.append('hello') will add 'hello' to the array in the first available free spot, provided the array isn't full.
# a.addToEnd('hello') will add 'hello' to the array, skipping all spaces between full spots.
# print(a) will print out the array, 'None' in positions that are empty.
# a.remove(3) will delete the item at index 3.
# a.delete('hello') will delete the string 'hello' from the list.
# a.addList([1, 2, 3]) will append the list to the array in the first available spot for each item, provided there is enough space.
