#1.Python Collections Counter: is a special collection from collections module, used to count how many times each item appears
#counter is a dictionary subclass

from collections import Counter
numbers=[1, 2, 3, 4, 3, 4, 1]
count=Counter(numbers)
print(count)

#2.Heap queue or heapq in Python: is a data structure that allows quick access to the smallest or largest element

import heapq
li=[23, 87, 13, 40]
heapq.heapify(li)
print("Heap queue", li)

import heapq
h = [10, 20, 15, 30, 40]
heapq.heapify(h)

# Appending an element
heapq.heappush(h, 5)
print(h)

# Pop the smallest element from the heap
min = heapq.heappop(h)
print("Smallest:", min)
print(h)

#replace and merge operations
import heapq
h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)

min = heapq.heapreplace(h1, 5)
print(min)
print(h1)

h2 = [2, 4, 6, 8]
h3 = list(heapq.merge(sorted(h1), sorted(h2)))
print("Merged heap:", h3)

#3. Deque in Python: stands for Double-Ended Queue. It is a type of data structure that allows to add and remove elements from both ends efficiently

from collections import deque
dq = deque([1, 2, 3, 4])

print(dq[0])
print(dq[-1])

from collections import deque
dq = deque([10, 20, 30])
dq.append(40)               #adds an element to the right end of the deque
print(dq)

from collections import deque
dq = deque([10, 20, 30])
dq.appendleft(5)        #appendleft(): adds an element to the left end of the deque
print(dq)

from collections import deque
dq = deque([10, 20, 30])
dq.extend([40, 50, 60])       #extend(): adds multiple elements to the right end of the deque
print(dq)

from collections import deque
dq = deque([10, 20, 30])
dq.extendleft([1, 2])       #extendleft(): adds multiple elements to the left end of the deque
print(dq)

from collections import deque
dq = deque([10, 20, 30, 20])
dq.remove(20)           #remove(): removes the first occurrence of a specified value
print(dq)

from collections import deque
dq = deque([10, 20, 30])
dq.pop()             #pop(): removes and returns the element from the right end
print(dq)

from collections import deque
dq = deque([10, 20, 30])
dq.popleft()         #popleft(): removes and returns the element from the left end
print(dq)

from collections import deque
dq = deque([10, 20, 30])
dq.clear()        # clear(): removes all elements from the deque
print(dq)

from collections import deque
dq = deque([1, 2, 3, 4, 5])          
print(len(dq))      # len(): returns the total number of elements in the deque

from collections import deque
dq = deque([10, 20, 30, 20, 40, 20])
print(dq.count(20))     #count(): returns how many times a specific element appears in the deque

from collections import deque
dq = deque([10, 20, 30, 40])
dq.rotate(1)             #rotate(): rotates the elements of the deque
print(dq)

from collections import deque
dq = deque([10, 20, 30, 40])
dq.reverse()        #reverse(): reverses the order of elements in the deque
print(dq)  

#4. OrderedDict in Python:is a subclass of Python’s built-in dictionary that remembers the order in which keys are inserted

from collections import OrderedDict
                                                        
od = OrderedDict()   
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3

print(list(od.items()))

#5. Defaultdict in Python:
#Defaultdict is a subclass of the built-in dict class from the collections module
#It automatically assigns a default value to keys that do not exist which means no need to manually check for missing keys and avoid KeyError.

from collections import defaultdict
d = defaultdict(list)

d['fruits'].append('apple')
d['vegetables'].append('carrot')
print(d)
print(d['juices'])

