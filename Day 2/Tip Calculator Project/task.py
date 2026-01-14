print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# --- Prima versiune (mai scurtă, dar mai greu de înțeles) ---
bill_plus_tip = bill * (tip/100 + 1)                    # Calculează suma totală (nota + bacșiș)
pay_each_person = round(bill_plus_tip / people, 2)      # Calculează suma de plată per persoană (rotunjită la 2 zecimale)

print(f"Each person should pay: {pay_each_person}$")    # Afișează suma finală pentru fiecare persoană

# --- A doua versiune (mai clară și mai lizibilă) ---
tip_as_percent = tip / 100  # Transformă procentul de bacșiș într-o fracție (ex: 12% → 0.12)
total_tip_amount = bill * tip_as_percent    # Calculează suma bacșișului
total_bill = bill + total_tip_amount        # Calculează totalul final de plată (nota + bacșiș)
bill_per_person = total_bill / people       # Împarte totalul între persoanele participante
final_amount = round(bill_per_person, 2)    # Rotunjește suma finală per persoană la 2 zecimale

print(f"Each person pays: {final_amount}$") # Afișează suma finală pentru fiecare persoană
