#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tickets(people):
	print(people)
	answer = "NO"
	vasya_pocket={25:0, 50:0, 100:0}
	while len(people)!=0:
		current_customer=people[0]
		change = current_customer - 25
		vasya_pocket[current_customer]+=1
		hand = 0
		for k,v in vasya_pocket.items():
			hand += k * v
			if hand == change:
				answer = "YES"
				break;		
		del people[0]
	return answer


print(tickets([25, 25, 50]), "YES")
print(tickets([25, 100]), "NO")
print(tickets([25, 25, 50, 50, 100]), "NO")