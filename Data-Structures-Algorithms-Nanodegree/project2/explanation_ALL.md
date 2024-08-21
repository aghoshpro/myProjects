## 1. LRU Cache

Uses Python's OrderedDict as a cache, keeping track of the order entries are added. Delete and reinsert an entry to move it to the end.
If a key's value is altered, the key position remains unchanged. Ordered Dictionaries are implemented using hash tables. Check out https://mail.python.org/pipermail/python-dev/2017-December/151283.html. Hash tables should give search, insertion, and delete times that are on average `O(1)`. If m is the size of the data stored in the cache, each set operation causes it to increase by m until it reaches the maximum size of the cache capacity: `O(m\*m)`, where n represents the cache capacity.

## 2. File Recursion

The problem requires the use of a list containing the paths. Lists are ideal for this situation because they enable quick access and easy iteration for both displaying output and building the list. Appending to a list takes `O(1)`, whereas extending a list takes `O(k)` - where 'k' represents the number of members.

Recursion was utilized since the situation required it; nonetheless, recursion incurs more overhead because it takes additional stack space for the function parameters, rewinding the stack, returning control to where the function was called, and so on. Additionally, completing these tasks will take some extra time. This particular problem lacks a deep directory structure. The memory or space used is determined by the number of recursive calls multiplied by the space required for each stack frame. That would be `O(n\*m)`, where n is the number of calls and m is the amount of space needed for each frame.

## 3. Huffman Encoding

I used a tree. Why? Because the problem specified "Build the Huffman Tree". So the tree stores and counts the letters. On average, trees take `O(log(n))` time to access, insert, and delete. The worst-case scenario is `O(n)` - where n is the number of tree nodes.

There are also other structures in here, such as a dictionary to keep track of the letters and counts (`O(1)` average, `O(n)` worst case), which is iterated over to build a list of tuples.

There is also a priority queue, with worst-case access and searching times of `O(n)` and insert times of `O(1)`. A priority queue is ideal for this scenario since it maintains track of the minimum value. Items with the greatest priority are dequeued before items with lesser priorities. Items with the same priority are served in the order they appear in the queue. This alleviates some of the workload associated with managing the tree's nodes.

During encoding, each iteration of a tree node adds one element to the dictionary, thus it grows by the number (n) of items encoded plus the size of the encoding string, which is proportional to the depth or number of levels (d) in the tree `O(n+d)`. Decoding entails recreating the output string to the same size (n) as the original data: `O(n)`.

## 4. Active Directory.

We decided to utilize sets for groups and users since they have less overhead than lists and are faster. However, due to the small size of the test sample, the real time difference was insignificant. They also do not allow duplicates, which seems to be necessary when keeping actual user IDs. The function is_user_in_group(), which searches over a set using x in s, takes `O(1)` on average and `O(n)` in the worst case. At least in this case, we don't care about the order in which the entries are saved, and a set handles that effectively. If the initial group being searched has a sub-group, a recursive call is made to search that group for the user. The function performs some fundamental actions such as setting a flag, checking if the user is in the group (`O(1)` search time), and determining whether the object is a Group before making the recursive call, so that a recursive call is only made when necessary.

The is_user_in_group() method takes up the majority of the time; the time complexity has already been mentioned. The only additional memory overhead required to execute this function is a single boolean flag indicating if the user is a member of the group or any sub-groups: `O(1)`.

## 5. Blockchain

The problem requires a linked list. Hmm, I see a pattern here. This is a single-linked list that includes a tail pointer. New blocks are added, and the tail always refers to the most recently added block. The blocks contain a previous pointer, allowing for backward traversal across the block chain. Insertions have an average and worst-case time complexity of Big `O(1)`, whereas searches take `O(n)`. If there are n items in the list (blockchain) and each item occupies m bytes of memory, the space complexity is `O(n\*m)`. As a side aside, the data stored is just a random integer.

## 6. Union and Intersection

Again, the problem requires for the use of linked lists to simulate the activities of a set's union and intersection functions. Insertions and deletions (which are not done in this example) have an average and worst-case time complexity of Big `O(1)`. A method for determining whether a value is in the list (in_list) has been implemented, and it may take `O(n)` to find an item because the full list/chain must be searched.

Using the union and intersect approach necessitates several searches. To avoid duplicates, the union traverses each list element by element `O(n)` and looks for it in the union list. The worst case for the union list search is `O(n)`, while the worst case for the intersection might be `O(n^2)`. The intersect goes through one list element by element, `O(n)`, then searches for it in the second list as well as the intersect list before adding it - worst case `O(n^2)`per search. Adding all elements from the lists to either the union or intersection could result in a worst-case space complexity of`O(n^2)`.
