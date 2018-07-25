"""
problem statement:
https://community.topcoder.com/stat?c=problem_statement&pm=13642&rd=16312&rm=&cr=23077918

possible result:
3,2 ABB
2,0 BA
5,8 ""
10,12 BAABBABAAB
"""
from __future__ import print_function, division
import math

class AB:
    def createString(self, N, K):
        s = [1] * (N//2) + [0] * ((N+1)//2)
        while K:
            for i in range(N-1):
                if s[i] == 1 and s[i+1] == 0:
                    s[i] = 0
                    s[i+1] = 1
                    break
            else:
                return ""
            K -= 1
        return "".join("A" if i == 0 else "B" for i in s)

if __name__ =='__main__':
    sc = AB()
    re = sc.createString(3,2)
    print(re)




