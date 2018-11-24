#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_last(n, m):

    dictionary_circle = [[[x, 0 ], 0] for x in range(1,n+1)]
    current_index = 0

    while(len(dictionary_circle)>1):
    	n = (len(dictionary_circle))
    	for i in range(0,m):
    		dictionary_circle[(current_index) % n][0][1] += 1
    		dictionary_circle[(current_index) % n][1] += 1
    		current_index += 1
    		
    	for i in dictionary_circle:
    		if i[1] == 0:
    			i[0][1] += 2
    		else:
    			i[1] = 0
    	current_index -= 1
    	current_index = (current_index) % (n)
    	dictionary_circle[(current_index + 1) % n][0][1] += \
    		dictionary_circle[(current_index ) % n ][0][1]
    	del dictionary_circle[(current_index ) % n]
    return (dictionary_circle[0][0][0], dictionary_circle[0][0][1])


print(find_last(5, 1), (5, 24))
print(find_last(8, 3), (7, 51))
print(find_last(75, 34), (35, 4238))
print(find_last(82, 49), (48, 5091))
print(find_last(73, 38), (61, 3996))
print(find_last(86, 71), (10, 6275))
print(find_last(61, 17), (26, 3000))
print(find_last(42, 38), (12, 1578))
print(find_last(29, 5), (28, 740))
print(find_last(64, 49), (43, 3327))
print(find_last(61, 20), (32, 2922))
print(find_last(88, 52), (59, 5856))