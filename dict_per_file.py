#!/usr/bin/env python

import sys
from pprint import pprint
import tag_per_line as tpl

def main():
    inputfile = sys.argv[1]
    try:
        print inputfile+'\n'
        f = open(inputfile)
        line=f.readline()
        d=dict()
        while line:
            tags_all=tpl.get_tags(line)
            for w in tags_all:
                w=w.lower()
                if w in d:
                    d[w]+=1
                else:
                    d[w]=1
       # print "dictionary size: "+ len(d) + '\n'
        f.close()
        sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1),reverse=True)
        for i in range(0,len(sorted_d)):
            print sorted_d[i][0] + ' ' + sorted_d[i][1] + '\n'
        return sorted_d
    except Exception:
         print "Cannot open inputfile: "+ inputfile + '\n'

if __name__ == '__main__':
    main()

