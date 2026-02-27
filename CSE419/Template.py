import sys, os

#---------------------------------
#making an array
#arr = list(map(int, input().split()))

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
        #code

if __name__ == "__main__":
    solve()



