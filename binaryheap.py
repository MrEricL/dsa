# To change it from a min heap to max heap
# Change less, so that True > False and False > True

class binaryheap:
	heap = [None]

	def insert(self, x):
		self.heap.append(x)
		self.swim(self.size())

	def heapsort(self, unsorted):
		for each in unsorted:
			self.insert(each)

	def delete_min(self):
		min_val = self.heap[1]
		self.swap(1, self.size())
		self.sink(1)
		self.heap.pop()
		return min_val

	def get_min(self):
		return heap[1]

	def sink(self, x, s):
		while (2*x < s):
			y = 2*x
			#checks which child it's greater than
			if (not self.less(y, y+1)):
				y+=1
			if (self.less(x, y)):
				break
			self.swap(x,y)
			x = y

	def swim(self, x):
		while (self.less(x,x/2) and x > 1):
			self.swap(x,x/2)
			x = x/2

	def size(self):
		# account for None start
		return len(self.heap) - 1

	def swap(self, x, y):
		self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

	# Returns true if val at x is less than val at y
	def less(self, x, y):
		if self.heap[x] < self.heap[y]:
			return True
		else:
			return False

	def get_heap(self):
		return self.heap[1:]

	#not exactly working :(
	def pretty_print(self):
		level = 0
		curr = self.size()
		while (curr != 0):
			level+=1
			curr = curr/2
		
		curr = self.size()
		ret = ""
		olevel = level

		while (level >= 0):
			space = " " * (olevel - level + 1)
			ret += " " * (olevel - level )
			while curr >= 2**(level-1):
				ret+= (str(self.heap[curr]) + space)
				curr -= 1
			ret += "\n"
			level -= 1
		return ret


test = binaryheap()
test.heapsort([5,4,1,6,4,9,0,2])
print test.get_heap()
'''
test.insert(5)
print test.pretty_print()
test.insert(2)
print test.pretty_print()
test.insert(3)
print test.pretty_print()
test.insert(6)
print test.pretty_print()
test.insert(4)
print test.pretty_print()
test.insert(1)
print test.pretty_print()
test.delete_min()
print test.pretty_print()
test.delete_min()
print test.pretty_print()
test.delete_min()
print test.pretty_print()
'''




