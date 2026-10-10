def count_calories(szivveres,testsuly,kor,edzeshossz,nem):
    if nem == "N":
        calories =calories = (
    (-20.4022 +
     (0.4472 * szivveres) -
     (0.1263 * testsuly) +
     (0.0740 * kor))
    / 4.184) * edzeshossz
    else:
        calories = (
                 (-55.0969 +
                 (0.6309 * szivveres) +
                    (0.1988 * testsuly) +
                    (0.2017 * kor))
                    / 4.184) * edzeshossz

    return calories
class Athlete:
    def __init__(self,nev,kor=18,testsuly = None,nem = None):
        self.nev = nev
        self.kor = kor
        self.testsuly = testsuly
        self.nem = nem
