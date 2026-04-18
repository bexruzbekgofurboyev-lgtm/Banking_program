def balance(balanc):
    print(f"Your balance is: {balanc}")

def deposit(balanc):
    depo=float(input("How much do you want to deposit: "))
    if depo>0:
        print("--Deposit successfully--")
        return depo
    else:
        print("--Only positive number--")
        return 0
def withdraw(balanc):
    withdraw=float(input("How much do you want withdraw:"))

    if withdraw>0 and withdraw<balanc:
        print("--Withdraw successfully--")
        return withdraw
    else:
        print("--Balance insuficient--")
        return 0

def main():
    again=True
    balanc=10.0
    while again:
        print("-"*20)
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice=int(input("Biror amaliyotni tanlang: "))
        if choice==1:
            balance(balanc)
        elif choice==2:
            balanc+=deposit(balanc)
        elif choice==3:
            balanc-=withdraw(balanc)
        elif choice==4:
            again=False
        else:
            print("Mavjud bo'lmagan amaliyot :(")
    print("alvida!")
if __name__=="__main__":
    main()
