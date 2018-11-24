#!/usr/bin/env python
# -*- coding: utf-8 -*-

def game_winners(gryffindor, slytherin):
	if gryffindor[1]=="yes":
		gryffindor[0] += 150;
	if slytherin[1]=="yes":
		slytherin[0] += 150;
	if gryffindor[0] > slytherin[0]:
		return "Gryffindor wins!"
	elif gryffindor[0] < slytherin[0]:
		return "Slytherin wins!"
	else:
		return "It's a draw!"

print(game_winners([100, "yes"],[100, "no"]), "Gryffindor wins!")
print(game_winners([350, "no"],[250, "yes"]), "Slytherin wins!")
print(game_winners([100, "yes"],[250, "no"]), "It's a draw!")
print(game_winners([0, "yes"],[250, "no"]), "It's a draw!")
print(game_winners([150, "no"],[0, "yes"]), "It's a draw!")