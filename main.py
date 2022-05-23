import Studnie

if __name__ == "__main__":
    run = "1"
    while run == "1":
        print("Wybierz opcję, którą chcesz wykonać:")
        print("1) Przykładowe studnie i domy, które pokazują, że algorytm działa")
        print("2) Własne studnie i domy")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            print("TODO")
        elif choice == "2":
            S=[[-1,-1],[8,1]]
            D=[[-4,4],[-1,4],[1,1],[2,4],[3,7],[3,-4]]
            print(Studnie.hungarian(S,D))
            print("Szukamy połączenia dla następujących studni:")
            for i in range(len(S)):
                print(i+1, S[i][0], S[i][1])
            print("oraz domów:")
            for i in range(len(D)):
                print(i+1, D[i][0], D[i][1])
            M = Studnie.hungarian(S,D)
            print("Znaleziony minimalny koszt", "TODO", "\nprzy następujących połączeniach:")
            for i in range(len(S)):
                for j in range(len(D)):
                    if M[j][0] == i:
                        print(i+1, "->",M[j][1]-len(S)+1)
        else:
            print("Błędny wybór!")
        run = input("Czy chcesz kontynuować, jeśli tak, to wybierz 1: ")
