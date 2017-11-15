import os
import os.path
import sys
import csv
import subprocess as sub

def isexec (fpath):
    if fpath == None: return False
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK) 

def which(program):
    fpath, fname = os.path.split(program)
    if fpath:
        if isexec (program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if isexec (exe_file):
                return exe_file
    return None

if __name__ == '__main__':
    option = sys.argv[1]
    repopath = sys.argv[2]
    mvn = which('mvn')
    git = which('git')
    os.chdir(repopath)
    
    if option == 'compile':
        ret = sub.call ([mvn, 'compiler:compile'])
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
    elif option == 'test':
        ret = sub.call ([git, 'checkout', 'b7b5e5e', 'pom.xml'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=SevenZOutputFileTest#testBCJX86Roundtrip'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=SevenZOutputFileTest#testBCJARMRoundtrip'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=SevenZOutputFileTest#testBCJARMThumbRoundtrip'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=SevenZOutputFileTest#testBCJPPCRoundtrip'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=SevenZOutputFileTest#testBCJSparcRoundtrip'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=SevenZOutputFileTest#testFilterRoundTrip'])
        print ret
        if ret == 1:
            sys.exit(1)
        ret = sub.call ([mvn, 'surefire:test', '-Dtest=SevenZOutputFileTest#testBCJIA64Roundtrip'])
        print ret
        if ret == 0:
            sys.exit(0)
        else:
            sys.exit(1)
