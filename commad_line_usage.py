#!/usr/bin/python
#coding=utf-8
"""
注意  分析串 冒号： 等号=
"""
import sys,getopt
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts,args = getopt.getopt(argv,"hi:o:",['ifile=',"ofile="])
    except getopt.GetoptError:
        print("Error")
        sys.exit(2)
    for opt,arg in opts:
        if opt =='-h':
            print('help')
            sys.exit()
        elif opt in ('-i','--ifile'):
            inputfile = arg
        elif opt in("-o",'--ofile'):
            outputfile = arg
    print("input file",inputfile)
    print("ouput file",outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])