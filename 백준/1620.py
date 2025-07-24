import sys
n , m= map(int,sys.stdin.readline().split())

dic = {}
dic2 = {}
for i in range(1, n+1):
    a = sys.stdin.readline().rstrip()
    dic[i] = a
    dic2[a] = i
for i in range(m):
    b = sys.stdin.readline().rstrip()
    try:
        b = int(b)
        print(dic[b])
    except:
        print(dic2[b])