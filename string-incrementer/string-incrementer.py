#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def increment_string(strng):
	m = re.search(r'([0-9]+$)', strng)
	try:
		number = int(m.group(1))
	except AttributeError:
		return strng + "1"
	right_end = len(str(number))
	if len(str(number + 1)) > right_end and m.group(1)[0] == "0":
		return strng[:-right_end-1] + str(number + 1)
	else:
		return strng[:-right_end] + str(number + 1)



print(increment_string("foobar00999"), "foobar01000")
print(increment_string("foo"), "foo1")
print(increment_string("foobar001"), "foobar002")
print(increment_string("foobar1"), "foobar2")
print(increment_string("foobar00"), "foobar01")
print(increment_string("foobar99"), "foobar100")
print(increment_string("foobar099"), "foobar100") # !!
print(increment_string(""), "1")