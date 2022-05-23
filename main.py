import Studnie

if __name__ == "__main__":
    run = "1"
    while run == "1":
        print("Wybierz opcję, którą chcesz wykonać:")
        print("1) Własne studnie i domy")
        print("2) Przykładowe studnie i domy, które pokazują, że algorytm działa")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            print("TODO")
        elif choice == "2":
            S = [[4,10],[-3,20]]
            D = [[0,0],[12,9],[-7,15],[-9,16]]
            Studnie.print_info(S,D)
        else:
            print("Błędny wybór!")
        run = input("Czy chcesz kontynuować, jeśli tak, to wybierz 1: ")
