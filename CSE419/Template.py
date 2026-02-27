import sys, os
import bisect

#---------------------------------
#making an array
#arr = list(map(int, input().split()))

# lowerBound
#pos = bisect.bisect_left(arr, x)  --> x er shoman ba boro First Index
#pos = bisect.biseect_right(arr,x) --> x er boro First Index
#---------------------------------
# ---------- FAST IO ----------
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")

input = sys.stdin.readline
# --------------------------------

def solve():
    t = int(input())   # number of test cases
    #t = 1
    for _ in range(t):
        print("Hello World")

if __name__ == "__main__":
    solve()



