## Type Hints

- In Python, type hints can be be added to method parameters & return type.
Ex: def example_method(self, value: int) -> bool:
  pass

## Abstraction

- It lets you hide complex implementation details, and only shows the essential features of an object or system
- Python implements abstraction through the abc module.

## Algorithms

- Algorithms have two key characteristics: 1) they must finish in a finite number of steps; 2) each step must be precise and unambiguous
- Page describing the process of approaching algorithmic challenges: https://www.freecodecamp.org/learn/python-v9/lecture-working-with-common-data-structures/what-are-good-problem-solving-techniques-and-ways-to-approach-algorithmic-challenges

## Big O Notation

- Big O notation describes the worst-case performance of an algorithm, as input increases
- In Big O notation, the input size is denoted with n. The term that has the greatest impact on performance will be the highest order term with n; ex: 7n + 20 > highest order is 7n; 20n^2 + 15n + 7 > highest order is 20n^2 (a.k.a. quadratic time complexity). Most common complexities:

O(1) is known as the "Constant Time Complexity" - when an algorithm has this, it takes the same amount of time to run, regardless of input size; ex. check if a number is odd or even (it always takes the same amount of time, regardless of the number checked)
O(log n) = Logarithmic Time Complexity; time req. by algo. increases slowly as the input size increases; ex. Binary Search has O(log n), because it discards half of the input in each comparison.
O(n) = Linear Time Complexity; increases proportionally to the input size; ex. a for loop over a list
O(n log n) = Log-Linear Time Complexity; common for efficient sorting algorithms, like Merge Sort and Quick Sort
O(n^2) = Quadratic Time Complexity; ex: nested loops
O(2^n) and O(n!) = Exponential / Factorial Time Complexities, both inefficient.

- Big O notation can also be applied to memory space requirements, not just time requirements.

O(1) = Constant Space Complexity, always requires a constant amount of memory space. Ex: an algo. with a few variables in memory
O(n) = Linear Space Complexity, mem. sp. req. increase proportionally to input size. Ex: an algo. that creates and stores a copy of a list with n items
O(n^2) = Quadratic Space Complexity, req. increase quadratically. Ex: 2D matrix that stores all possible combinations of an input n

## Sets

- Sets are unordered (can't be accessed via indices) collections of unique (adding two of the same keeps only one copy) elements
- Sets: avg. time complex. for add/remove/get length/check if element is in set = O(1); worst case for add/remove/check element is O(n), because sets are implemented as hash tables. Space complex. is same as hash maps.
- Python sets are implemented as hash maps, and can only contain immutable objects.

## Hash Maps

- Maps, hash maps, sets are abstract data types. ADT describe what operations can be performed, not how they are performed.
- A map ADT manages k-v pairs and their operations in a specific & efficient way. All keys must be unique, which allows direct, efficient lookups.
- A hash map / hash table is a concrete implementation of the map ADT. Hash maps generate a hash for each k-v pair, which is then used to calculate an index in the array.
- Hash maps: avg. time complex. for insert/retrieve/delete is O(1); worst case is O(n) when there are many hash collisions. Space complex. of inserting is O(1), but worst case O(n). Removing has a space complex. O(1)

## Dictionaries

- Python's dictionaries are implemented as hash maps.

## Arrays

- Arrays store ordered collections of data, and are of two types: static and dynamic arrays.
- Static arrays have a fixed size, and store elements in adjacent memory locations. Its size is determined when it is initialized, and is fixed in memory - it cannot be modified at runtime.
- Because the memory is fixed, the program can store the location of the first element & use indices to make simple calculations, or find other elements in the array. Thus, accessing values in a static array takes a constant time O(1).

Static arrays are useful when you know the number of elements that will be stored in advance.

- Python does not include traditional static arrays as built-in data structures.
- Dynamic arrays can grow/shrink automatically at runtime. They are resized automatically, by copying elements into a new array once the original is full.

Accessing elements of a dynamic array takes constant time O(1). Inserting an element in the middle takes linear time O(n), because the elements after it must be relocated. Inserting an element at the end takes O(1) time, if there is still space available in the dynamic array, but if it is full, then it take O(n) time.

## Stacks & Queues

- Stacks and queues are common linear data structures that follow specific rules for adding/removing elements.
- A stack is a LIFO data structure. Last element added is the first removed. Stacks have two ends: a top and bottom. Elements are added & removed from the top.
- Adding an element to a stack is called a "push" operation. Removing is "pop"
- The time complexity of push/pop is typically O(1)
- The space complexity of push/pop is usually O(1)
- A queue is a FIFO - first element added is the first to be removed. Queues have a front and a back. Elements are added to the back, and removed from the front.
- Adding an element is known as an "enqueue" operation. Removing is "dequeue"
- The time complexity of enqueue/dequeue is O(1), and the space complexity is O(1)

## Linked Lists

- A linked list is a data structure in which each node is connected to the next node in the sequence. Each node stores data and a reference to the next node in the linked list.
- In singly linked lists, traversal is allowed only in one direction (because each node contains a reference only to the next node in the sequence). A search in such a list starts from the first node ("head") and continues to the last node ("tail"). The head node is usually the only node that is directly accessible.
- Linked lists do not have a fixed size. You can insert a node anywhere.
- Inserting a node at the head of the linked list has a O(1) time complexity. At the tail, O(n) because the entire list has to be traversed.

Nodes can also be removed from anywhere. From head: constant time complexity O(1). From tail: O(n)

- In doubly linked lists, each node stores references both to the next & previous nodes.
- Doubly linked lists can be traversed in both directions.
- But doubly linked lists require more memory than singly linked lists, since each node stores two references instead of one.

## When to Use Each Data Structure

**Lists**: When you need ordered, indexed access and don't know size in advance
**Stacks**: For LIFO operations (undo functionality, expression evaluation, backtracking)
**Queues**: For FIFO operations (task scheduling, breadth-first search)
**Linked Lists**: When frequent insertion/deletion at beginning, unknown size, no random access needed
**Hash Maps**: For fast key-value lookups, counting occurrences, caching
**Sets**: For uniqueness checking, mathematical set operations, removing duplicates

## Official review of data structures
https://www.freecodecamp.org/learn/python-v9/review-data-structures/review-data-structures