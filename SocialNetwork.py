
class SocialNetwork:
    def averageFriends(self, interests):
        res = 0
        for i, x in enumerate(interests):
            for j, y in enumerate(interests):
                if i != j and len(set(x) & set(y)):
                    res += 1
        return 1.0 * res / len(interests)
if __name__ == '__main__':
    instring = ["ABC", "DE", "FGHIJA"]
    test = SocialNetwork()
    af = test.averageFriends(instring)
    print(af)