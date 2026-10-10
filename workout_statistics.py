import matplotlib.pyplot as plt
import pandas as pd
from colorama import Fore,Style
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

def show_stats(df):
    plt.plot(df["Nap"],df["Kalória"])
    plt.xlabel("Nap")
    plt.ylabel("Kalória")
    plt.title("Kalóriaégetés")
    plt.show()

def main():
    print(Fore.CYAN +"---------ᕦ⁠ʕ⁠ ⁠•⁠ᴥ⁠•⁠ʔ⁠ᕤ---------", Style.RESET_ALL)
    nev = input("Név: ")
    kor = int(input("Kor: "))
    testsuly = float(input("Testsúly: "))
    nem = input("Nem (N/F): ")
    felhasznalo=Athlete(nev,kor,testsuly,nem)

    workout_df = pd.read_excel("Workout_Data.xlsx")
    workout_df["Kalória"] = count_calories(workout_df["Szívverés(bpm)"],felhasznalo.testsuly,felhasznalo.kor,workout_df["Edzéshossz(perc)"],felhasznalo.nem)
    print(workout_df)
    show_stats(workout_df)

main()