
class SimpleDarts:
    def highestScore(self, F):
        if F <=9: # F * 3 < 25 --> F<9.3 but there is a problem when F got 9, with highest should be 50+ 25 + 9*3
            rd = F*3 + 50 + 25
        elif (F-2) * 3 > 50:
            rd = F * 3 + (F-1) *3 + (F-2) * 3
        else:
            rd = 50 + F*3 +(F-1) * 3
        return rd
class SimpleDarts2: # solution from Topcoder, good idea by creating an arry which include all score, then sort it.
    def higestScrore(self, F):
        arr = [i for i in range(1, F+1)] + [2 * i for i in range(1, F + 1)] + [3 * i for i in range(1, F+1)]
        arr.append(25)
        arr.append(50)
        arr.sort()
        ans = arr[-1] + arr[-2] + arr[-3]
        return ans

if __name__ == "__main__":
    test = SimpleDarts()
    result = test.highestScore(20)

    test2 = SimpleDarts2()
    result2 = test2.higestScrore(20)

    print(result)
    print(result2)