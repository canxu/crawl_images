#!/usr/bin/env python

import sys, json
from pprint import pprint

def main():
	inputfile = sys.argv[1]
	f = open(inputfile)
	for l in f:
		try:
			j = json.loads(l)
		except Exception:
			continue
		pprint(j)


if __name__ == '__main__':
	main()
