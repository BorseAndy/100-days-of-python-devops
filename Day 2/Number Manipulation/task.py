# # Calculul indicelui de masă corporală (BMI) = greutate (kg) / (înălțime (m))^2
# bmi = 84 / 1.65 ** 2
#
# # Afișează valoarea calculată exactă a BMI
# print(bmi)
#
# # Afișează BMI ca număr întreg (fără zecimale)
# print(int(bmi))
#
# # Afișează BMI rotunjit la cel mai apropiat număr întreg
# print(round(bmi))
#
# # Afișează BMI rotunjit la 2 zecimale
# print(round(bmi, 2))

# Inițializare variabile
score = 0          # scorul jucătorului
height = 1.8       # înălțimea jucătorului (în metri)
is_winning = True  # status dacă jucătorul câștigă

# Jucătorul marchează un punct → scorul crește cu 1
score += 1
print(score)       # afișează scorul actualizat

# Folosirea unui f-string pentru a combina text și variabile într-un mesaj clar
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")