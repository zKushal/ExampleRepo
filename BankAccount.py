class BankAccount:
    def __init__(self):
        self.amount = 0
    
    def depositAmount(self, amount):
        if amount <= 0:
            print("Please enter valid amount")
        else:
            self.amount += amount
            print(f"Deposited Amount: {self.amount}")
            print("Amount Deposited Successfully")
    
    def withdrawAmount(self, amount):
        if self.amount <= 0:
            print("Please enter valid amount")
        elif amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount
            print("Amount Withdrawn Successfully")
    
    def checkBalance(self):
        print(f"Your current balance is: {self.amount}")
        
        
obj = BankAccount()

while True:
  print("1. Deposit Amount")
  print("2. Withdraw Amount")
  print("3. Check Balance") 
  print("4. Exit")
  
  select = input("Please select an option (1-4): ")
  
  match select:
        
        case "1":
            deposit_amount = float(input("Enter the amount to deposit: "))
            obj.depositAmount(deposit_amount)
            obj.checkBalance()
            input("Press Enter to continue...")
            
        case "2":
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            obj.withdrawAmount(withdraw_amount)
            obj.checkBalance()
            input("Press Enter to continue...")

        case "3":
            obj.checkBalance()
            input("Press Enter to continue...")
   
            
        case "4":
            print("Thank you for using our banking services!")
            break
            
        case _:
            print("Invalid choice. Please try again.")
        
    
  