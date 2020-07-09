#https://atcoder.jp/contests/abc103/tasks/abc103_a
#A = sorted([int(x) for x in input().split()])
#cost = 0
#cost += abs(A[2]-A[1])
#print (cost)

a,b,c = map(int,input().split())
ans = max(a,b,c) - min(a,b,c)
print (ans)