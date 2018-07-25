"""
 problem statement： https://community.topcoder.com/stat?c=problem_statement&pm=14992
"""
class AutomaticVacuumCleaner:
    def getPoistion(self, num, C):
        x = num // C + 1
        if x % 2 == 0:
            y = num % C
        else:
            y = C - (num % C) + 1
        po = [x, y]
        return po

    def getDistance(self,R,C,A,B):
        po1 = self.getPoistion(A,C)
        po2 = self.getPoistion(A+B,C)
        distance = abs(po1[0] - po2[0]) + abs(po1[1] - po2[1])
        return distance

if __name__ =="__main__":
    dis = AutomaticVacuumCleaner()
    re = dis.getDistance(7, 27, 80, 30)
    print(re)









