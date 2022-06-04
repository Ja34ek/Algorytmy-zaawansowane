import Studnie
from random import randrange

if __name__ == "__main__":
    run = "1"
    while run == "1":
        print("Wybierz opcję, którą chcesz wykonać:")
        print("1) Własne studnie i domy")
        print("2) Przykładowe studnie i domy, które pokazują, że algorytm działa")
        print("3) Losowe studnie i domy")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            print("Podaj kolejno studnie w postaci np: 25 -14. Jeśli chcesz zakończyć podawanie wpisz KONIEC")
            temp = ""
            S = input("- ")
            while S != "KONIEC" and S != "Koniec" and S != "koniec":
                temp += S
                temp += " "
                S = input("- ")
            S=[]
            temp = temp.split()
            for i in range(len(temp)//2):
                S.append([int(temp[2*i]), int(temp[2*i + 1])])
            print("Podaj kolejno domy w postaci np: 25 -14. Jeśli chcesz zakończyć podawanie wpisz KONIEC")
            temp = ""
            D = input("- ")
            while D != "KONIEC" and D != "Koniec" and D != "koniec":
                temp += D
                temp += " "
                D = input("- ")
            D=[]
            temp = temp.split()
            for i in range(len(temp)//2):
                D.append([int(temp[2*i]), int(temp[2*i + 1])])
            if len(D) % len(S) != 0:
                print("Podano błędną liczbę domów lub studni!")
                continue
            Studnie.print_info(S,D)
            
        elif choice == "2":
            S = [[4,10],[-3,20]]
            D = [[0,0],[12,9],[-7,15],[-9,16]]
            Studnie.print_info(S,D)


        elif choice == "3":
            n = randrange(1,10)
            k = randrange(1,5)
            S=[]
            D=[]
            for i in range(n):
                temp1 = randrange(-1000,1000)
                temp2 = randrange(-1000,1000)
                S.append([temp1, temp2])
                for i in range(k):
                    temp1 = randrange(-1000,1000)
                    temp2 = randrange(-1000,1000)
                    D.append([temp1, temp2])
            Studnie.print_info(S,D)



        else:
            print("Błędny wybór!")

        

        run = input("Czy chcesz kontynuować, jeśli tak, to wybierz 1: ")
