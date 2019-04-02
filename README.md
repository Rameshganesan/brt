# brt

This is an example to implement the least recently used cache using python. 
The logic is as follows.

It is cache size as parameter the fuction and list of values passed to the cache. When cache is free it will add the values till
it is full. once cache is full it will evict the least recently used value and add the new value. When new value added it is called
page fault and, when existing value added that is called page hit. The function will print the page fault and page it.

The function returns the final snapshot of after adding all the values from list also print all the sequence of movement in cache.
