import sys

for line in sys.stdin:
    m1,m2=map(int,line.split())
    if m1==0 and m2==0:
        break
    sys.stdout.write(str(m1+m2))